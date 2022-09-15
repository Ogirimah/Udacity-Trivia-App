<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Udacitrivia](#udacitrivia)
  - [Introduction](#introduction)
  - [Starting the Project](#starting-the-project)
  - [About the Stack](#about-the-stack)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [The Repository Tree Structure](#the-repository-tree-structure)
  - [Guide to Cloning the Repository](#guide-to-cloning-the-repository)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Udacitrivia

## Introduction

This is a project that requires each student to complete the backend implementation of a Trivia web app as part of the requirements to complete the Udacity Full-Stack Nono-degree program. The API needs to be capable of taking requests from the frontend, query the database, and return an appropriate and well-formated response to the frontend.

The project strengthens each student's ability to implement, test and document well structured APIs.

## Starting the Project

Before starting the project your device needs to have:
- Python3
- Postgresql
- Node
- and NPM

To run the project locally, follow the below steps:

1. Clone the repository to your device. If you need assistance doing this, use this [guide]()

1. Run the backend

1. Run the frontend

## About the Stack

### [Backend](./backend/README.md)

The [backend](./backend/README.md) was built using Flask and SQLAlchemy server. 

> View the [Backend README](./backend/README.md) for more details.

### [Frontend](./frontend/README.md)

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. It was built to send requests to the backend endpoints, and the responses it receives are used to run it

> View the [Frontend README](./frontend/README.md) for more details.

## The Repository Tree Structure

```
├── CODEOWNERS
├── LICENSE.txt
├── README.md
├── backend
│   ├── README.md
│   ├── flaskr
│   ├── models.py
│   ├── requirements.txt
│   ├── test_flaskr.py
│   └── trivia.psql
└── frontend
    ├── README.md
    ├── package-lock.json
    ├── package.json
    ├── public
    └── src
```

---

## Guide to Cloning the Repository

by running either of there in your terminal for mac and linux systems, and in git bash for windows systems.

    HTTPS:

>       clone https://github.com/Ogirimah/Udacity-Trivia-App.git

    SSH:

>       clone git@github.com:Ogirimah/Udacity-Trivia-App.git
