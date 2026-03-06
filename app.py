from flask import Flask, render_template, request
import re

# Initialize the Flask application
app = Flask(__name__)

def check_password_strength(password):
    """
    Evaluates the strength of a password based on simple rules:
    - Less than 6 characters → Weak
    - 6–8 characters → Medium
    - More than 8 characters and contains numbers and uppercase letters → Strong
    """
    if len(password) < 6:
        return "Weak"
    elif 6 <= len(password) <= 8:
        return "Medium"
    else:
        # Check if it contains at least one number and one uppercase letter
        has_number = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        
        # If it has more than 8 chars, AND contains both numbers and uppercase letters
        if has_number and has_upper:
            return "Strong"
        else:
            # Otherwise, it falls back to Medium
            return "Medium"

def is_valid_email(email):
    """
    Checks if the email format is valid using a simple regular expression.
    """
    # Simple regex for email validation (e.g., name@domain.com)
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Define the main route that handles both GET (display form) and POST (submit form)
@app.route('/', methods=['GET', 'POST'])
def index():
    email_result = None
    password_result = None
    email_input = ""
    
    # Check if the form was submitted using POST method
    if request.method == 'POST':
        # Get the email and password from the submitted form (default to empty string if missing)
        email_input = request.form.get('email', '')
        password_input = request.form.get('password', '')
        
        # 1. Validate the email format
        if is_valid_email(email_input):
            email_result = "Valid"
        else:
            email_result = "Invalid"
            
        # 2. Check the password strength
        password_result = check_password_strength(password_input)
        
    # Render the index.html template and pass the results to it so they can be displayed
    return render_template('index.html', 
                           email_result=email_result, 
                           password_result=password_result,
                           email_input=email_input)

if __name__ == '__main__':
    # Run the Flask application in debug mode for easier development
    app.run(debug=True)
