# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python >= 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we used to handle the lightweight SQL database. Its configuration was defined in the `/flaskr` directory and also in`test_flaskr.py` file for development setup.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we used to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `/backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_DEBUG=True   # For development setup
flask run
```

---

---

## Backend Directory Structure

```
├── README.md
├── flaskr
│   └── __init__.py
├── models.py
├── requirements.txt
├── test_flaskr.py
└── trivia.psql
```

---

---

## Endpoints

The endpoints are prefixed with the domain that the project is running from. So for a local deployment setup, the endpoints will be prfixed by the localhost and port number, i.e `http://localhost:5000`.

Below are the endpoints the frontend sends requests to.

### List of Endpoints

`GET 'http://localhost:5000/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```
---

`GET 'http://localhost:5000/questions'`

- Fetches dictionaries of questions from the database, in which each dictionary has five key value pairs.
- The keys are; id, question, answer, difficulty, and category
- It takes an optional page number as request argument, ie `'/questions?page=<page_number>'`
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string. Example is shown below:

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 2
    }
  ],
  "totalQuestions": 100,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": "History"
}
```

---

`GET '/categories/${id}/questions'`

- Fetches questions for a cateogry specified by id request argument
- Request Arguments: `id` - integer
- Returns: An object with questions for the specified category, total questions, and current category string

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 4
    }
  ],
  "totalQuestions": 100,
  "currentCategory": "History"
}
```

---

`DELETE 'http://localhost:5000/questions/${id}'`

- Deletes a specified question using the id of the question
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions.

---


`POST 'http://localhost:5000/questions'`

- Sends a post request in order to add a new question
- Request Body:

```json
{
  "question": "Heres a new question string",
  "answer": "Heres a new answer string",
  "difficulty": 1,
  "category": 3
}
```

- Returns: Does not return any new data

---

`POST 'http://localhost:5000/searcQuestions'`

- Sends a post request in order to search for a specific question by search term
- Request Body:

```json
{
  "searchTerm": "this is the term the user is looking for"
}
```

- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 5
    }
  ],
  "totalQuestions": 100,
  "currentCategory": "Entertainment"
}
```

---
  
`POST 'http://localhost:5000/quizzes'`

- Sends a post request in order to get the next question
- Request Body:

```json
{
  'previous_questions': [1, 4, 20, 15]
    quiz_category': 'current_category'
 }
```

- Returns: a single new question object

```json
{
  "question": {
    "id": 1,
    "question": "This is a question",
    "answer": "This is an answer",
    "difficulty": 5,
    "category": 4
  }
}
```

---

---

## Contributors
    
To contribute to this project, you can create an issue and open a pull request. But your code should be written in accordance with our coding style:

### 1. Use test driven development 

by writting tests that the code will have to pass.

To setup the test server, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
```

And to deploy the test, run

```bash
python test_flaskr.py
```

### 2. PEP8

Your code should be in accordance with pep8 coding style. for details on pep8, checkout the [pep8 guide](https://peps.python.org/pep-0008/)

> **Recognition**
Once your code is reviewed and merged, we will include you in the list of contributors to the project.