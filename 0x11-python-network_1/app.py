from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    return f"Your email is: {email}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
