# SonarCube LLM - Code Analysis API

SonarCube LLM is a simple web application that analyzes your code and provides feedback on potential issues using AI-powered analysis. It utilizes OpenAI's GPT-3.5 for code issue detection and suggestions.

## Features

- **Code Analysis**: Submits code to the backend to analyze and identify issues.
- **AI-powered Suggestions**: Uses OpenAI's GPT-3.5 model to generate recommendations for improving your code.
- **REST API**: Simple REST API that accepts code for analysis and returns suggestions.

## Technologies Used

- Python
- Flask
- OpenAI API (GPT-3.5)
- Werkzeug (for debugging)

## Requirements

Before running the project, you need to have the following dependencies installed:

- Python 3.x
- Flask
- OpenAI Python package
- Requests (for sending HTTP requests to the Flask API)

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/sonarcube-llm.git
cd sonarcube-llm
Install dependencies:

Run the following command to install all necessary dependencies.

bash
Copy code
pip install -r requirements.txt
Set up the OpenAI API key:

You will need an OpenAI API key to use the AI-powered analysis feature. If you don't have one, you can sign up on the OpenAI website.

Set your API key as an environment variable:

bash
Copy code
export OPENAI_API_KEY="your-api-key-here"
Alternatively, you can add the API key directly in the code (not recommended for production).

Run the Flask Application:

Once everything is set up, you can start the Flask application using:

bash
Copy code
python app.py
This will run the server locally on port 5000.

API Usage
The application exposes a simple API that accepts a POST request with a code snippet, analyzes it, and returns feedback.

POST /analyze
Request:

bash
Copy code
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d "{\"code\": \"function unusedFunction() { let unusedVar = 42; console.log('Hello World!'); }\"}"
Response:

json
Copy code
{
  "issues": [
    {
      "line": 1,
      "message": "Unused variable 'unusedVar'"
    }
  ],
  "suggestions": "Please remove unused variables and optimize your code."
}
Request Parameters:

code: A string representing the code you want to analyze.
Response:

A JSON object containing:
issues: An array of issues detected in the code, each with a line number and a description.
suggestions: A general recommendation for fixing issues in the code.
Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Contributions are always welcome!

How to Contribute:
Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes.
Commit your changes and push them to your fork.
Open a pull request with a description of your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
OpenAI GPT-3.5 for providing the AI-powered code analysis.
Flask for serving the API.
vbnet
Copy code

### How to Use the README

1. Replace `your-username` in the `git clone` URL with your GitHub username.
2. The instructions provide basic setup information and usage examples.
3. Ensure you update the instructions for setting the OpenAI API key, depending on how users should manage it.
4. Add a `LICENSE` file if you intend to include one, or adjust the licensing section as needed.
   
Feel free to modify the content as necessary based on your specific requirements!