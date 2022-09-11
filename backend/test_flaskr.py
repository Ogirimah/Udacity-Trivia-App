import os
import unittest
import json
from urllib import request
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # ====================================================================================
        # Define test variables
        # ====================================================================================

        # # Define list of questions for testing 
        # questions = Question.query.filter(Question.id.in_([2, 4])).all()
        
        # self.questions = [question.format() for question in questions]
        # print(f'{self.questions}')
        

        # Define question for testing post_new question
        self.test_question = {
            'question': 'About how many taste buds does the human tongue have',
            'answer': '10000',
            'category': '1',
            'difficulty': 3
            }
        # Negate bool for delete and post new question
        self.teardown_delete_question = False
        self.teardown_post_new_question = False

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        if self.teardown_delete_question:
            deleted_question = {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            }
            question = Question(
                # id=deleted_question['id'],
                question=deleted_question['question'],
                answer=deleted_question['answer'],
                category=deleted_question['category'],
                difficulty=deleted_question['difficulty']
            )
            question.insert()
        elif self.teardown_post_new_question:
            inserted_question = Question.query.filter(Question.answer.ilike('%10000%')).one_or_none()
            print(f'Inserted Question: {inserted_question}')
            inserted_question.delete()
        else: pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    
    # =================================================================================
    # Test for all endpoints
    # =================================================================================
    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['categories']), 6)
        self.assertTrue(data['message'])

        self.tearDown()

    def test_get_paginated_question(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['categories']), 6)
        # self.assertEqual(data['total_questions'], 19)
        self.assertTrue(data['current_category'])
        self.assertTrue(data['message'])

        self.tearDown()

    def test_delete_question(self):
        res = self.client().delete('/questions/5')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertEqual(question, None)

        self.teardown_delete_question = True
        self.tearDown()
        self.teardown_delete_question = False

    def test_post_new_question(self):
        res = self.client().post('/questions', json=self.test_question)
        print(f'{res}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertEqual(data['total_questions'], 20)
        self.assertTrue(data['questions'])

        self.teardown_post_new_question = True
        self.tearDown()
        self.teardown_post_new_question = False

    def test_get_question_by_search_term(self):
        res = self.client().post('/searchQuestions', json={'searchTerm': 'title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['message'])
        self.assertGreater(data['no_of_questions'], 0)

        self.tearDown()

    def test_get_question_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['message'])
        self.assertGreater(data['no_of_questions'], 0)

        self.tearDown()

    def test_get_question_to_play_the_quiz(self):
        res = self.client().post('/quizzes',
                                json={
                                    'previous_questions': [2, 4],
                                    'quiz_category':
                                    {'id': '5', 'type': 'Entertainment'}
                                    }
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['message'])


        self.tearDown()

    # =================================================================================
    # Test for all errors
    # =================================================================================
    def test_404_request_beyond_valid_page(self):
        res = self.client().get('/questions?page=50')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_422_unprocessable_post_post_new_question(self):
        res = self.client().post('/questions', json={
                                                    'question': 'About how many taste buds does the human tongue have',
                                                    'category': '1',
                                                    'difficulty': 3
                                                    })
        data = json.loads(res.data)
                
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_400_no_searchTerm(self):
        res = self.client().post('/searchQuestions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_422_invalid_category(self):
        res = self.client().get('/categories/50/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_422_no_question_to_delete(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Processable')

    def test_422_unprocessable_quizzes_request(self):
        res = self.client().post('/quizzes', json={
                                                    'previous_questions': [],
                                                    'quiz_category': {'id': 50}
                                                 })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Processable')

        
    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()