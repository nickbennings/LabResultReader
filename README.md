https://nickbennings.github.io/LabResultReader/

Lab Results Interpreter
This web application interprets lab results into plain English using OpenAI's language model. It provides a user-friendly interface to input lab results, send them to the backend for processing, and display the interpreted text.

Features
Input Form: Allows users to enter lab results in a textarea.
Interpretation: Sends lab results to the backend using Flask and OpenAI's API to generate interpreted text.
Display: Shows the interpreted text in a formatted manner on the same page.
Technologies Used
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
API: OpenAI API for natural language processing
Getting Started
To run this project locally, follow these steps:

Clone this repository:

bash
Copy code
git clone <repository-url>
cd lab-results-interpreter
Install dependencies:

Copy code
pip install -r requirements.txt
Set up your OpenAI API key:

Sign up for an OpenAI account and obtain your API key.
Set your API key as an environment variable:
arduino
Copy code
export OPENAI_API_KEY='your-api-key'
Run the Flask application:

Copy code
python app.py
Open your web browser and go to http://localhost:5000 to view the application.

Usage
Enter the lab results in the textarea provided.
Click the "Interpret" button to see the interpreted text.
Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

