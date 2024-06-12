# Flask-PyProject
# Project: Form in Python with Flask

## Skills developed:
* Backend: PYTHON programming (introduction to logical structures)
* Sanitization and validation of a form
* Implementation of POST and GET methods
* Implementation of templates with Jinja

## Problem statement:
The company Hackers Poulette™ sells DIY kits and accessories for Rasperri Pi. They want to allow their users to contact their technical support. Your mission is to develop a Python script that displays a contact form and processes its response: sanitization, validation, and then sending feedback to the user.

## Performance criteria:
* If the user makes an error, the form should be returned to them with valid responses preserved in their respective input fields.
* Ideally, display error messages near their respective fields.
* The form will perform server-side sanitization and validation.
* If sanitization and validation are successful, a "Thank you for contacting us." page will be displayed, summarizing all the encoded information.
* Implementation of the honeypot anti-spam technique.

#### Form fields
First name & last name + email + country (list) + message + gender (M/F) (Radio box) + 3 possible subjects (Repair, Order, Others) (checkboxes). All fields are mandatory, except for the subject (in this case, the value should be "Others").

## Contact Form (Python)
* Presentation: server/client architecture (transmissive, 10")
* Sanitization: neutralizing any harmful encoding (<script>)
* Validation: mandatory fields + valid email
* Sending + Feedback
* NO NEED FOR JAVASCRIPT OR CSS

#### At the end of this project, you should be able to:
- Explain the difference between a POST request and a GET request.
- Protect yourself against XSS vulnerabilities.
- Protect yourself against SSTI attacks.
- Use a micro framework.
- Perform a deployment.

-----------------------------------------------------------------

## **1.** Flask Web Framework

### What is Flask?

**Flask** is a lightweight, micro web framework for Python, designed to be easy to use and to help developers get started quickly with web development. 
It’s known for its simplicity and flexibility, allowing developers to choose the tools and libraries they want to use.

### Key Features of Flask

1. **Minimalistic**: Flask provides the basic tools to get a web server up and running with minimal setup, but it doesn't include any default database, form handling, or other components that you might find in more extensive frameworks like Django. This gives developers the freedom to add only what they need.

2. **Modular and Extensible**: Flask is designed to be extended. It supports extensions that add application features as if they were implemented in Flask itself. There are extensions for database integration, form validation, upload handling, and more.

3. **Built-in Development Server and Debugger**: Flask includes a built-in development server and a debugger, which makes the development process easier and more efficient.

4. **RESTful Request Dispatching**: Flask makes it easy to build RESTful APIs by providing tools to handle HTTP requests and route URLs to specific pieces of code.

5. **Jinja2 Templating**: Flask uses Jinja2 as its templating engine, allowing you to separate your HTML from your Python code.

### How Flask Works

Here’s a simple example of a Flask application in `app.py`:

```python
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Route for handling the home page
@app.route('/')
def home():
    return "Hello, Flask!"

# Route for handling a form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    # Process the form data here
    return f"Form submitted by {first_name} {last_name} with email {email}"

if __name__ == '__main__':
    app.run(debug=True)

