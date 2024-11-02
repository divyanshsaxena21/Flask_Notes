
## Lecture 1

Why make a Web App? 
- For Exchange of Information

	==*"Exchange of Information"* -How ?==
	- Client - Server Architecture
	- HTTP protocol

#### What is Flask?

- ==Flask is a web framework== mainly used for creating and working with web applications using Python.
- ==Flask is based on WSGI architecture and supports Jinja.==

==What is WSGI ?==

- Web Server Gateway Interface
- An architecture to follow, for handling requests and responses between clients and server.

==What is Jinja ?==

- Web Template Engine
- Allows to develop dynamic web pages.
- Supports *"Template Inheritance"*.
- Helps reduce repetitiveness and complexity in web page development.


## Prerequisites

**1. Endpoints** 

- Address of web pages.

**2. Path parameters and Query Parameters**

- Path parameters are used for accessing a particular resource at an endpoint.
- Query parameters are used for filtering the data received from an endpoint.

**3. HTTP Methods**

*CRUD*
- Post *(Create)*  
- Get *(Read)*
- Put *(Update)*
- Delete *(Delete)*

**4. HTTP Response Codes**

- **1xx** - Informative 
- **2xx** - Success
- **3xx** - Redirection
- **4xx** - Client - side error
- **5xx** - Server - side error




## Lecture 2

*Topics*
- Dynamic URL
- URL Redirection
- Building URL

**What is a dynamic URL**

A URL that gets generated automatically based on certain inputs is a dynamic URL.


**What is URL Redirection ?**

It's a process in which when users visit a particular URL, they're navigated/ guided to a different URL.

*How is URL Redirection helpful?*

- If a page is deleted, users need to be redirected to another URL.
- If maintenance of a web page is going on, users can be redirected.
- If website gets renamed, users can be redirected to appropriate URL.

**Common Response Codes:**

-  301: *Moved permanently*
-  302: *Redirected temporarily*
-  303: *Redirected temporarily*
-  307: *Redirected temporarily*
-  308: *Redirected permanently*


## Lecture 3

*Topics*
- Custom HTML Templates
- Jinja
- Template Inheritance


#### Jinja

- Parameters and Placeholders
- If Conditional
- For Loops
- Blocks

**Parameter**

- things inside the render_templates (eg: title)

**Placeholders**

- Use **{{}}** -> 2 sets of curly brackets

**Blocks**

- {% block content %}
    {% endblock content %}

		This starts a block in which custom code dedicated to the single page is written, % block block_name

```html 
<li ><a href="{{url_for('about')}}" target="_blank">About</a></li>
```

**If Statements**

- They are used using Jinja Tempates code under the HTML file.
```

{% block content %}

<h2>Given input is {{number}}</h2>

{% if number==0%}

    <p>The given input {{number}} is neither Even nor Odd</p>

{% elif number%2==0%}

    <p>The given input {{number}} is Even</p>

{% else %}

    <p>The given input {{number}} is Odd</p>

{% endif %}

{% endblock %}

```

**Loops**

- We firstly stored the data in a python file and then showed the data on a HTML page using Jinja.
```{% for emp_id,emp_data in emps.items()%}
<div>

    <table>

        <tr>

            <td>ID</td>

            <td>{{emp_id}}</td>

        </tr>

        <tr>

            <td>Name</td>

            <td>{{emp_data["name"]}}</td>

        </tr>

        <tr>

            <td>Age</td>

            <td>{{emp_data["age"]}}</td>

        </tr>

        <tr>

            <td>Position</td>

            <td>{{emp_data["position"]}}</td>

        </tr>

    </table>

</div>

<br>

<br>

{% endfor %}
```
### Template Inheritance

*When the same piece of code is present in several HTML files, then we make one single file and use it's code across all files.*

{% extends "layout.html" %} -> "layout.html", this is the file where the main code is present

and this code is used to inherit/ extend that file.


## Lecture 4

*Topics*


- Forms
- CSRF (Cross-Site Request Forgery)
- wtforms
- Code Demo


##### What are Forms (Web Forms) ?

Forms are web pages where end-users can enter their data which can be sent to the backend server for processing

##### Why do we need Forms ?

- Allows end-users to interact with webpages and websites
- Enable data collection
- Facilitates communication with end-users
- Make for dynamic websites.

##### Working of Web Forms :

- Front-end design (HTML,CSS, JS)
- User input captured from input field
- Input data processed in the back-end
- HTTP Request generated and sent to Server
	- Get - *query parameters*
	- Post - *store in database*
- HTTP Response from Server
- Response data parsed and displayed to Client accordingly


#### What is CSRF attack ?

- Cross Side Request Forgery
- It's a type of an attack, where an attacker 'tricks' and end-user in performing some malicious/unintended action over a web application
- Such attacks are common when web applications take inputs from users (ex: forms)

##### Working of CSRF : 

- An attacker creates a malicious website or an email
- These websites/emails usually contain links that will generate a request to the web application
- These requests are designed to perform some unintended actions over the application on behalf of the end-users.
- Since the end-users would be authenticated, these 'unintended' actions would be perceived as 'genuine' by the web application and carried out.
- These actions generally lead to leakage of sensitive data, transfer of funds, etc.

##### Prevention of CSRF: *CSRF Tokens*

- It's a long, random and unpredictable string generated at the server side
- The token is shared with the end-user after authentication
- Whenever 


### WTForms

WTForms is a flexible forms validation and rendering library for Python web development. It can work with whatever web framework and template engine you choose. It supports data validation, CSRF protection, internationalization (I18N), and more. There are various community libraries that provide closer integration with popular frameworks.


#### Why use wtforms ?

- Super convenient to create and handle forms
- Help avoid manual input validation
- Helps prevent CSRF attacks.
- Complaint with 'pythonic' coding style
	- Treat forms as python classes
	- Work with forms as objects and attributes
	- No need to write tedious HTML code (input, label, id tags, etc.)
- Integrated with Flask (flask-wtf)
