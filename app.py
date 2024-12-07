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
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if not is_valid_username(username) or not is_valid_password(password):
        log_error("Invalid username or password")
        return jsonify({'error': 'Invalid input!'}), 400

    hashed_password = hash_password(password)  # ????? ???? ??????
    save_user(username, hashed_password)  # ??? ???????? ?? ????? ????????
    
    session = login_to_linebet(username, password)
    
    if session:
        data = fetch_data(session)
        predicted_result = predict_outcome()
        return jsonify({'data': data, 'prediction': predicted_result})
    else:
        return jsonify({'error': 'Login failed!'}), 401

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
```