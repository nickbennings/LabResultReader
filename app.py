import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/interpret', methods=['POST'])
def interpret():
    # Retrieve lab results from POST request
    lab_results = request.json.get('lab_results')

    # Use OpenAI API to interpret lab results
    response = openai.Completion.create(
        model="text-davinci-003",  # Choose the model appropriate for text interpretation
        prompt=f"Translate the following lab results into plain English:\n\n{lab_results}",
        max_tokens=150
    )

    interpreted_text = response.choices[0].text.strip()

    # Return interpreted text as JSON response
    return jsonify({'interpreted_text': interpreted_text})

if __name__ == '__main__':
    app.run(debug=True)
