# app.py
from flask import Flask, render_template, request, redirect, url_for
import json
import os
import hashlib
from zk_login import generate_challenge, prove, verify

app = Flask(__name__)
USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        if username in users:
            return "User already exists."

        # Save reversed password as secret (for ZKP simulation)
        users[username] = {
            'password_hash': hash_password(password),
            'zk_secret': password[::-1]  # simulate a ZKP shared secret
        }

        save_users(users)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        if username not in users:
            return "Invalid username"

        # Rebuild the ZKP secret using reversed password
        zk_secret = password[::-1]

        # Generate challenge and verify ZKP
        challenge = generate_challenge()
        response = prove(zk_secret, challenge)

        if verify(response, zk_secret, challenge):
            return f"✅ ZKP Login successful for {username}!<br>🧠 Challenge: {challenge}<br>🔐 Response: {response}"
        else:
            return "❌ ZKP verification failed."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
