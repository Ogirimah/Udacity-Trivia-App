from crypt import methods
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    """Seperate questions to 10 per page"""
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    page_questions = questions[start:end]

    return page_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, resources={r'/api/*' : {'origins' : '*'}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-type, Authorization'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, DELETE'
        )
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/api/categories', methods=['GET'])
    def get_all_categories():
        query = Category.query.all()
        output_data = [output.format() for output in query]

        if len(query) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': output_data,
            'message': 'Categories successfuly retrieved'
        })


    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/api/questions', methods=['GET'])
    def get_paginated_questions():
        query = Category.query.all()
        output_data = [output.format() for output in query]

        selection = Question.query.all()
        list_of_questions = paginate_questions(request, selection)

        if len(query) == 0:
            abort(404)
        elif len(selection) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'message': 'Questions successfully retrieved',
            'questions': list_of_questions,
            'total_questions': len(selection),
            'current_category': 1,
            'categories': output_data
        })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/api/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            question_detail = question.format()['question']

            if question is None:
                abort(404)

            question.delete()

            return jsonify({
                'success': True,
                'message': f'Question: "{question_detail}" has been deleted'
            })
        except:
            abort(422)
        


    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/api/questions', methods=['POST'])
    def post_new_question():
        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)

        try:
            insert_question = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty
            )
            insert_question.insert()

            all_questions = Question.query.order_by(Question.id).all()
            formated_question = [question.format() for question in all_questions]
            # print(f'{all_questions}')

            return jsonify({
                'success': True,
                'message': 'Question successfully created',
                'total_questions': len(formated_question),
                'questions': formated_question
            })
        except:
            abort(422)


    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/api/searchQuestions', methods=['POST'])
    def get_question_by_search_term():
        body = request.get_json()
        searchTerm = body.get('searchTerm', None)

        if searchTerm == None:
            abort(400)

        else:
            try:
                questions = Question.query.filter(Question.question.ilike('%{}%'.format(searchTerm))).all()
                formated_questions = [question.format() for question in questions]
                
                return jsonify({
                    'success': True,
                    'message': 'Questions successfully retrieved by searchTerm',
                    'questions': formated_questions,
                    'no_of_questions': len(formated_questions)
                })
            except:
                abort(422)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/api/categories/<int:category_id>/questions', methods=['GET'])
    def get_questions_by_category(category_id):
        try:
            questions = Question.query.filter(Question.category == category_id).all()
            formated_questions = paginate_questions(request, questions)


            return jsonify({
                'success': True,
                'message': f'All questions of category {category_id} were retrieved',
                'questions': formated_questions,
                'no_of_questions': len(formated_questions)
            })
        except:
            abort(404)


    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/api/quizzes', methods=['POST'])
    def get_question_to_play_the_quiz():
        pass

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

