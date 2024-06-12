# Flask-PyProject
![alt text](/img/banner.png)
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
```

### How to run a Flask Application

1. Ensure you have Python installed.
2. Install Flask using pip:

```bash
pip install Flask
```

3. Save the above code in a file named `app.py`.
4. Run the application:

```bash
python app.py
```

5. Open a web browser and navigate to http://127.0.0.1:5000/ to see the output or if you are using Visual Code just click on the link displayed in the terminal.

![alt text](/img/flask-terminal.png)

### Flask and Web Security
Regarding security, Flask allows you to implement various measures to protect against web vulnerabilities like XSS and SSTI. 

For example, you can use the following strategies in your Flask backend:

1. Sanitize Inputs: Always sanitize and validate user inputs.
2. Escape Outputs: Use Flask’s built-in Jinja2 templating to automatically escape user inputs before rendering them in HTML.
3. CSRF Protection: Use Flask extensions like Flask-WTF to protect forms from Cross-Site Request Forgery (CSRF) attacks.
4. Content Security Policy: Set appropriate security headers, such as Content Security Policy (CSP), to mitigate risks.

## **2.** Project

For this project I installed Flask via my terminal and I ran it via Visual code.
First I prepared my tree structure for my files.

I linked a folder to Visual code with flask and created my files: contact.html, thank_you.html.  I also have my app.py ready to be coded.

![alt text](/img/arbo-flask.png)

Here are the links for each scripts I used for this project.

1. [app.py](https://github.com/Cosimo-CS/Flask-PyProject/blob/main/app.py)
2. [contact.html](https://github.com/Cosimo-CS/Flask-PyProject/blob/main/contact.html)
3. [thank_you.html](https://github.com/Cosimo-CS/Flask-PyProject/blob/main/thank_you.html)

Here below you can see the results:

![alt text](/img/contact-html.png)
![alt text](/img/thanks-html.png)



## **3.** Miscellaneous

### **1.** Explain the difference between a POST request and a GET request.

- POST request: The request data is sent in the body of the HTTP request. Used to send sensitive data such as passwords, credit card information, etc. Often used for actions that modify the state of the server, such as sending forms.

- GET request: The request data is sent in the URL as request parameters. Used to retrieve resources from the server. The data is visible in the URL, making it less secure for sensitive information. Used for non-destructive requests such as reading data.

### **2.** Protect yourself against XSS vulnerabilities.

- **Protection against XSS attacks :**

Use of security libraries: Use dedicated security libraries that provide additional functionality to prevent XSS attacks, such as bleach or html_sanitizer.

- **I choosed to use html_sanitizer and Jinja2 because:**

`html_sanitizer` is a Python library used to clean and sanitize HTML content. It is designed to remove potentially dangerous or unwanted elements and attributes from HTML code, which can help prevent Cross-Site Scripting (XSS) attacks and ensure that the HTML content is safe to display.

- **Why Use HTML Sanitizer?**

1. **Security**: Sanitizing HTML input prevents malicious users from injecting harmful scripts or code into your web application, which can be used to steal data, deface websites, or perform other malicious activities.
2. **Consistency**: It helps maintain consistent and clean HTML content by removing unwanted tags and attributes.
3. **Compliance**: Ensures that user-generated content adheres to your HTML standards and policies.

- **How Does It Work?**

`html_sanitizer` works by parsing the HTML content and removing or escaping any elements or attributes that are not in the allowed list. This includes:
- Removing scripts, iframes, and other potentially harmful tags.
- Removing or sanitizing attributes that could be used for malicious purposes, like `onload`, `onclick`, etc.
- Ensuring that the content adheres to a specified whitelist of allowed tags and attributes.


`Jinja2` is a modern and designer-friendly templating engine for Python web frameworks. It allows you to create dynamic HTML pages by embedding Python-like expressions in your HTML.

**Key Features**

- **Template Inheritance**: Allows you to reuse common layout structures.
- **Variables**: Dynamically insert values into your HTML.
- **Control Structures**: Use loops and conditionals to control the rendering of your HTML.
- **Filters**: Modify the display of variables.

**How Jinja2 Works**

- A template is an HTML file with placeholders for dynamic content. These placeholders are called variables and control structures.
- Rendering is the process of combining a template with data to produce a final HTML document.

Here below you can find an example of how to use it in an html code.

![alt text](/img/ex-jinja2.png)

### **3.** Protect yourself against SSTI attacks.

