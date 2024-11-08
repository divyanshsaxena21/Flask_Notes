
## Lecture 1

Why make a Web App? 
- For Exchange of Information

	==*"Exchange of Information"* - How ?==
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


## Lecture 5

*Topics*

- About Databases
- Types of Mappings
- ORM (Object Relational Mapping)
- SQL Alchemy and SQLite Database
- Code Demo


**What is a Database**

- Database is a means of storing data in an organized manner.
- Helps to store, process and manipulate large volumes of data rather conveniently.
- Allows complex datasets to be stored as separate entities and establish relationships between each other for easy identification.
- Most preferred method for storing application data in the server side in the backend.

**Type of Databases :**

On broad level

- Relational Databases
- Non-Relational Databases

**What is ORM ?**

- It's a tool that acts as an interface between an OOP language and a Relational Database.
- Helps represent database tables in corresponding object-oriented formats in OOP language.
- Allows accessing and manipulation of database tables just as we would objects in OOP language of choice.
- Helps translate code written in OOP languages into SQL queries for data processing and vice versa.


**Why use an ORM ?**

- Provides abstraction from complex SQL queries
- Seamless mapping between OOP language and Relational Database
- Let's switch between different Databases quickly and effortlessly
- Less code to write to perform operations
- Helps overcome SQL Injection Attacks.


##### **SQL Alchemy**

Flask SQL Alchemy is an extension for Flask that adds support for SQL Alchemy to your application. It simplifies using SQL Alchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines.

- A Python-specific ORM tool.
- Can be used to connect with any database.
- Helps represent Database tables as Python classes
- Helps work with rows and columns of a Database table as Class instances and attributes respectively in Python.

##### **SQLite Database**

- Server-less, lightweight database engine.
- Written in C programming language
- The database is stored as a file in the file system
- Convenient for quick use and small-scale storage purposes.
