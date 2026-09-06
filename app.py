```python
from flask import Flask, render_template, request
import re

app = Flask(__name__)


def check_password_strength(password):
    if len(password) < 6:
        return "Weak"

    if len(password) <= 8:
        return "Medium"

    has_number = any(c.isdigit() for c in password)
    has_uppercase = any(c.isupper() for c in password)

    return "Strong" if has_number and has_uppercase else "Medium"


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


@app.route("/", methods=["GET", "POST"])
def index():
    email_result = None
    password_result = None
    email = ""

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        email_result = "Valid" if is_valid_email(email) else "Invalid"
        password_result = check_password_strength(password)

    return render_template(
        "index.html",
        email_result=email_result,
        password_result=password_result,
        email_input=email
    )


if __name__ == "__main__":
    app.run(debug=True)
```
