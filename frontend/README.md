# Frontend - Trivia API

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend) so it will not load successfully if the backend is not working or not connected. So **stand up the backend first** before running the frontend.

### Installing Dependencies

1. **Installing Node and NPM**
   This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**
   This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: `npm i` is shorthand for `npm install`

## Required Tasks

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

if an error similar to `code: 'ERR_OSSL_EVP_UNSUPPORTED'` is encountered, run `export NODE_OPTIONS=--openssl-legacy-provider` and then try running the frontend again

### Request Formatting

The frontend should be fairly straightforward and disgestible. You'll primarily work within the `components` folder in order to understand, and if you so choose edit, the endpoints utilized by the components. While working on your backend request handling and response formatting, you can reference the frontend to view how it parses the responses.

After you complete your endpoints, ensure you return to the frontend to confirm your API handles requests and responses appropriately:

- Endpoints defined as expected by the frontend
- Response body provided as expected by the frontend

### Optional: Updating Endpoints and API behavior

Would you rather the API had different behavior - different endpoints, return the response body in a different format? Go for it! Make the updates to your API and the corresponding updates to the frontend so it works with your API seamlessly.

### Optional: Styling

In addition, you may want to customize and style the frontend by editing the CSS in the `stylesheets` folder.

### Optional: Game Play Mechanics

Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category.

You can optionally update this game play to increase the number of questions or whatever other game mechanics you decide. Make sure to specify the new mechanics of the game in the README of the repo you submit so the reviewers are aware that the behavior is correct.

---

## Frontend Directory Structure

```
├── README.md
├── node_modules
├── package-lock.json
├── package.json
├── public
│   ├── art.svg
│   ├── delete.png
│   ├── entertainment.svg
│   ├── favicon.ico
│   ├── geography.svg
│   ├── history.svg
│   ├── index.html
│   ├── manifest.json
│   ├── science.svg
│   └── sports.svg
└── src
    ├── App.js
    ├── App.test.js
    ├── components
    ├── index.js
    └── stylesheets
```

----

## DO NOT PROCEED: ENDPOINT SPOILERS

> Only read the below to confirm your notes regarding the expected API endpoint behavior based on reading the frontend codebase.

### Expected endpoints and behaviors

`GET '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

---

`GET '/questions?page=${integer}'`

- Fetches a paginated set of questions, a total number of questions, all categories and current category string.
- Request Arguments: `page` - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string

