import os
import unittest
import json
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
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
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
    
    def test_get_all_categories(self):
        pass

    def test_paginated_question(self):
        pass

    def test_delete_question(self):
        pass

    def test_post_new_question(self):
        pass

    def test_get_question_by_search_term(self):
        pass

    def test_get_question_by_category(self):
        pass

    def test_get_question_to_play_the_quiz(self):
        pass




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()