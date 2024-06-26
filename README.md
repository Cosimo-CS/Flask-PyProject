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

**Flask** is a small web framework written in Python. It's called a microframework because it doesn't need specific tools or libraries to work. It doesn't come with built-in features like a database layer or form validation. 
Instead, Flask uses extensions to add these features, making them work just like they were built into Flask. There are extensions for many things, including database management, form validation, file uploads, authentication, and other common tasks. 
It's designed to help developers start web development quickly. Flask is lightweight and flexible, letting developers pick the tools and libraries they prefer.

### Main features of Flask

1. **Minimalistic**: Flask provides the basic tools to get a web server up and running with minimal setup, but it doesn't include any default database, form handling, or other components that you might find in more extensive frameworks like Django. This gives developers the freedom to add only what they need.

2. **Modular and Extensible**: Flask is designed to be extended. It supports extensions that add application features as if they were implemented in Flask itself. There are extensions for database integration, form validation, upload handling, and more.

3. **Built-in Development Server and Debugger**: Flask includes a built-in development server and a debugger, which makes the development process easier and more efficient.

4. **RESTful Request Dispatching**: Flask makes it easy to build RESTful APIs by providing tools to handle HTTP requests and route URLs to specific pieces of code.

5. **Jinja2 Templating**: Flask uses Jinja2 as its templating engine, allowing you to separate your HTML from your Python code.

### How Flask works?

Here below you can find a simple example of a Flask application in `app.py`:

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

As you can see in the terminal below, each actions that I'm doing in the web page are tracked.

![alt text](/img/terminal.png)


## **3.** Miscellaneous

### **1.** Explain the difference between a POST request and a GET request.

- POST request: The request data is sent in the body of the HTTP request. Used to send sensitive data such as passwords, credit card information, etc. Often used for actions that modify the state of the server, such as sending forms.

- GET request: The request data is sent in the URL as request parameters. Used to retrieve resources from the server. The data is visible in the URL, making it less secure for sensitive information. Used for non-destructive requests such as reading data.

### **2.** Protect yourself against XSS vulnerabilities.

**What is an XSS attack ?**

Cross-Site Scripting (XSS) is a type of security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. These scripts can steal data, hijack user sessions, or perform actions on behalf of the user.

**How does XSS work?**

1. **Injection**: An attacker injects a malicious script into a web application. This can happen through user input fields, URLs, or other methods.
2. **Execution**: When another user visits the affected page, the malicious script is executed by their browser.
3. **Impact**: The script can steal sensitive information (like cookies), redirect users to malicious sites, or perform actions without the user's consent.

**Types of XSS**

- Stored XSS
The malicious script is stored on the server (e.g., in a database) and served to users whenever they access the affected page.
**Example**: An attacker posts a comment containing a script on a forum. Every time users view the comment, the script runs.

- Reflected XSS
The malicious script is reflected off the web server, usually via a URL parameter or form input, and executed immediately.
**Example**: An attacker sends a victim a link with a malicious script in the URL. When the victim clicks the link, the script runs.

- DOM-based XSS
The vulnerability is in the client-side code (JavaScript) that modifies the DOM. The attack happens entirely on the client-side.
**Example**: A script reads data from the URL and dynamically updates the page without proper sanitization.

**Example of a vulnerable code**
```html
<form action="/search" method="get">
  <input type="text" name="query">
  <input type="submit" value="Search">
</form>
```

**Protection against XSS attacks :**

Use of security libraries: Use dedicated security libraries that provide additional functionality to prevent XSS attacks, such as bleach or html_sanitizer.

**I choosed to use html_sanitizer and Jinja2 because:**

`html_sanitizer` is a Python library used to clean and sanitize HTML content. It is designed to remove potentially dangerous or unwanted elements and attributes from HTML code, which can help prevent Cross-Site Scripting (XSS) attacks and ensure that the HTML content is safe to display.

**Why use HTML sanitizer?**

1. **Security**: Sanitizing HTML input prevents malicious users from injecting harmful scripts or code into your web application, which can be used to steal data, deface websites, or perform other malicious activities.
2. **Consistency**: It helps maintain consistent and clean HTML content by removing unwanted tags and attributes.
3. **Compliance**: Ensures that user-generated content adheres to your HTML standards and policies.

**How does it work?**

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

**What is SSTI?**

Server-Side Template Injection (SSTI) is a type of security vulnerability that occurs when an attacker can inject malicious code into a template, which is then executed on the server. This happens due to improper handling of user input in templating engines.

**How does SSTI works?**

1. **Templating Engines**: Web applications use templating engines (like Jinja2, Twig, or EJS) to dynamically generate HTML pages.
2. **User Input**: If user input is directly included in templates without proper sanitization or validation, it can lead to SSTI.
3. **Execution**: Malicious code injected into the template is executed on the server, potentially giving attackers access to sensitive data, server control, or other resources.

**Example of a vulnerable code**

```python
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name')
    template = f"Hello, {name}!"
    return render_template_string(template)
```

**Why is it vulnerable ?**

In this code:

- User Input: The user's input is retrieved from the query parameter name using request.args.get('name').
- Template Injection: The user input is directly embedded into a template string template = f"Hello, {name}!".
- Rendering: The render_template_string function is used to render the template, which processes the embedded user input as part of the template.

This allows an attacker to inject malicious template code via the name parameter, which can then be executed on the server.

**Consequences of SSTI attacks**

- Data Theft: Access sensitive information like database credentials, environment variables, or files on the server.
- Remote Code Execution: Run arbitrary code on the server, potentially taking full control of the server.
- Defacement: Modify the content of the website to mislead or deface the application.

**How to prevent and fix it?**

- Input Validation: Ensure that user input is properly validated and sanitized before including it in templates.
- Use Safe Functions: Use templating engine functions that are designed to handle user input safely.
- Template Escaping: Escape special characters in templates to prevent code execution.

To prevent SSTI, sanitize the user input to ensure it does not contain any executable code.

```python
from flask import Flask, request, render_template_string
from html import escape

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = escape(request.args.get('name', ''))
    template = f"Hello, {name}!"
    return render_template_string(template)

```

In the code above:

- The escape function from the html module is used to sanitize the user input by escaping any special characters.
- This prevents any user input from being executed as code within the template.

By escaping the user input, you ensure that the input is treated as plain text and not executable code, thus mitigating the risk of SSTI.
