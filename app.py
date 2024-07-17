from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/interpret', methods=['POST'])
def interpret():
    lab_results = request.json.get('lab_results')
    interpreted_text = interpret_lab_results(lab_results)
    return jsonify({'interpreted_text': interpreted_text})

if __name__ == '__main__':
    app.run(debug=True)
