import json
import requests
from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI API Key
openai.api_key = "your_OpenAI_Token"

# SonarQube Configuration
SONARQUBE_URL = "http://localhost:9000"
SONARQUBE_TOKEN = "your_token"

@app.route('/analyze', methods=['POST'])
def analyze_code():
    # Get code from user
    code = request.json.get("code")
    project_key = "SONARCUBE-LLM"

    # Save code to a file
    with open("temp_code.js", "w") as file:
        file.write(code)

    # Run SonarScanner
    sonar_command = f"""
    sonar-scanner \
        -Dsonar.projectKey={project_key} \
        -Dsonar.sources=. \
        -Dsonar.host.url={SONARQUBE_URL} \
        -Dsonar.login={SONARQUBE_TOKEN}
    """
    import os
    os.system(sonar_command)

    # Fetch issues from SonarQube API
    response = requests.get(
        f"{SONARQUBE_URL}/api/issues/search?componentKeys={project_key}",
        auth=(SONARQUBE_TOKEN, "")
    )
    issues = response.json()

    # Prepare prompt for ChatGPT
    prompt = f"The following code has issues:\n\n{code}\n\nIssues:\n"
    for issue in issues.get("issues", []):
        prompt += f"- Line {issue['line']}: {issue['message']}\n"

    prompt += "\nPlease fix the issues in the code."

    # Call ChatGPT
    chatgpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a code assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    fixed_code = chatgpt_response['choices'][0]['message']['content']

    return jsonify({"fixed_code": fixed_code})


if __name__ == "__main__":
    app.run(debug=True)
