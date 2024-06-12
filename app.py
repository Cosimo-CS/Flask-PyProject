```python
# Import necessary modules from Flask and html_sanitizer
from flask import Flask, render_template, request
from html_sanitizer import Sanitizer

# Create an instance of the Flask class
app = Flask(__name__)

# Create an instance of the Sanitizer class
sanitizer = Sanitizer()

# Define the route for the homepage (URL)
@app.route('/')
def index():
    # Render the contact.html template when the homepage is accessed
    return render_template('contact.html')

# Define the route for form submission with the POST method
@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data submitted by the user
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    country = request.form.get('country')
    message = request.form.get('message')
    gender = request.form.get('gender')
    subjects = request.form.getlist('subject')

    # Sanitize the HTML content of the form data
    first_name = sanitizer.sanitize(first_name)
    last_name = sanitizer.sanitize(last_name)
    email = sanitizer.sanitize(email)
    country = sanitizer.sanitize(country)
    message = sanitizer.sanitize(message)
    gender = sanitizer.sanitize(gender)
    subjects = [sanitizer.sanitize(subject) for subject in subjects]

    # Render the thank_you.html template with the sanitized form data
    return render_template('thank_you.html', first_name=first_name, last_name=last_name, email=email, country=country, message=message, gender=gender, subjects=subjects)

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
