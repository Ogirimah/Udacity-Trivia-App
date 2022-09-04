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

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    
    # =================================================================================
    # Test for all endpoints
    # =================================================================================
    def test_get_all_categories(self):
        res = self.client().get('/api/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['categories']), 6)

    def test_paginated_question(self):
        res = self.client().get('/api/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['categories']), 6)
        self.assertEqual(data['total_questions'], 19)
        self.assertTrue(data['current_category'])

    def test_delete_question(self):
        res = self.client().delete('/api/questions/5')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertEqual(question, None)

    def test_post_new_question(self):
        pass

    def test_get_question_by_search_term(self):
        pass

    def test_get_question_by_category(self):
        pass

    def test_get_question_to_play_the_quiz(self):
        pass

    # =================================================================================
    # Test for all errors
    # =================================================================================
    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()