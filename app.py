from flask import Flask, render_template, request, jsonify
from data_fetch import login_to_linebet, fetch_data
from predictions import predict_outcome
from database import create_database, save_user
from validators import is_valid_username, is_valid_password
from passwords import hash_password, check_password
from logger import setup_logger, log_error
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

setup_logger()

@app.route('/')
def index():
    return render_template('c.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not is_valid_username(username) or not is_valid_password(password):
        log_error("Invalid username or password")
        return jsonify({'error': 'Invalid input!'}), 400

    session = login_to_linebet(username, password)

    if session:
        data = fetch_data(session)
        predicted_result = predict_outcome()
        return jsonify({'data': data, 'prediction': predicted_result})
    else:
        log_error("Login failed for user: {}".format(username))
        return jsonify({'error': 'Login failed!'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    if not is_valid_username(username) or not is_valid_password(password):
        log_error("Invalid signup input for user: {}".format(username))
        return jsonify({'error': 'Invalid input!'}), 400

    hashed_password = hash_password(password)  # تشفير كلمة المرور
    save_user(username, hashed_password)  # حفظ المستخدم في قاعدة البيانات

    return jsonify({'message': 'Signup successful!'}), 201

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
```
