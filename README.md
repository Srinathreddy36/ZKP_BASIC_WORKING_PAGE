🔐 Garuda ZKP Login – Simulated Zero-Knowledge Authentication System
Garuda ZKP Login is a simulation project under the Garuda Sentinel cybersecurity mission. It demonstrates the principles of Zero-Knowledge Proofs (ZKPs) applied to user authentication—where a user proves knowledge of a secret without revealing it.

This system is implemented both as a command-line prototype and a Flask-based web interface to showcase how ZKP protocols can be adapted across platforms.

🚀 Features
🧠 ZKP Simulation using simple challenge-response authentication.

🔑 User Registration with ZKP-compatible secret generation.

🔁 Login System verifying users without revealing actual passwords.

🖥️ Command-line Interface (CLI) for ZKP authentication.

🌐 Web Interface built with Flask and HTML forms.

📄 User credentials stored securely in a local JSON file.

📚 Educational design to help understand ZKP-based authentication systems.
⚙️ How It Works
📝 Registration
User provides a username and password.

Password is reversed to create a ZKP secret (for simulation purposes only).

Both the password hash and the secret are stored in users.json.

🔁 ZKP Login Process
Verifier (server) generates a random challenge.

Prover (user) computes a response using their secret and the challenge.

The Verifier checks if the response matches the expected one using the stored secret.

✅ Access granted if matched; ❌ access denied otherwise.

💻 Run the Project
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Srinathreddy36/garuda-zkp-login.git
cd garuda-zkp-login
2. Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Requirements
bash
Copy
Edit
pip install flask
4. Run the Web App
bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

5. Run CLI ZKP Authentication
bash
Copy
Edit
python zk_login.py
🧠 Educational Purpose
⚠️ This project uses simplified ZKP logic (like reversing passwords) for simulation purposes only. Do not use this design in production environments.

This is part of the Garuda Sentinel mission to explore advanced cybersecurity mechanisms, including cryptography and authentication via hands-on projects.

📌 Next Upgrade (Coming Soon)
✅ In the next version:

Session-based user management

Improved ZKP model using Fiat-Shamir heuristic

Enhanced secure secret handling

Upgraded security storage (password hashing + salted secrets)

Real-world architecture simulation

🧙‍♂️ Author
Srinath Reddy – Cybersecurity Researcher & Developer
Part of the Garuda Sentinel project series.

📄 License
This project is licensed under the MIT License – feel free to use it for educational and research purposes.
