
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


## Lecture 5 (Part 1)

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

**Create Database and Insert**

![[CREATE AND INSERT.png]]

**READ from Database**

![[READ_1.png]]

**UPDATE and CLOSE CONNECTION**

![[UPDATE.png]]

### Lecture-5 (Part 2)

*Topics*
- One to many
- Many to Many


- Establish a Foreign Key between two tables

##### One to Many

**Team and Player**

![[Creating and Adding in Tables.png]]

![[Basic Operations.png]]

#### **The third table in Many to Many is called *==Association Table==***


**Create tables and add rows**

![[Pasted image 20241110211402.png]]

![[Pasted image 20241110211441.png]]
![[Pasted image 20241110211503.png]]

**How the Many-to-Many Works**

![[Pasted image 20241110211613.png]]


### Lecture-6

##### Sessions
*Topics*

- Definition
- Working
- Type of Sessions
- Security Considerations
- Code Demo

**What is a Web Session ?**

- A web session refers to the period of time an end user is active on a web application during a visit (until logout or session timeout)
- Information about the interaction b/w the user and the application during each visit is usually stored at 
	- Client side - *cookies (small chunks of data sent to application via server)*
	- Server side - *database*
- This helps the server and the browser maintain user preferences throughout the duration  of a particular visit to the website
	- *User login status*
	- *Items in online shopping cart*
	- *Website layout/appearance preferences*


**Working of Web Sessions**

1. Client-Server Architecture
2. HTTP Protocol
3. Login Credentials Stored in Server
4. IO Generated
5. For every interaction request is generated
6. Client-side session -> default in Flask
7. Server-side session -> in flask using library

**Types of Sessions**

*Based on Duration:*

1. Persistent Sessions:
	1. These sessions remain active for a very long period of time
	2. Ends only when the user manually terminates the session
	3. Ex: Social media, OTT
2. Non- persistent Session:
	1. These sessions last for a very short period of time
	2. Session ends when the application/browser is close

*Based on Security Mechanism*

1. Authenticated Sessions:
	1. Sessions are created only after the user has been authenticated (via login credentials)
2. Anonymous Sessions:
	1. Sessions are created even if the user hasn't been authenticated
	2. Useful for maintaining state information without authentication (as a 'Guest')
	3. Ex: Amazon

*Based on Storage Location*

1. Client-Side
	1. State information of the sessions is stored within the browser
	2. Useful for storing, insensitive data
	3. Ex: browser cookies
2. Server-Side
	1. State information of the sessions is stored in databases
	2. Ideal for large volumes and sensitive data; Offer improved security and integrity.


**Security Considerations**

***Measures to enhance Security and Integrity of Sessions data getting stored***

1. Session ID:
	- The session ID should be long and randomly generated
	- The session ID should be changed periodically during a session
	- The session ID shouldn't be exposed as part of any URL.
2. Secure Cookies:
	- Set the flags *HTTP Only* and *Secure* and the attribute *SameSite* while setting cookies over HTTP.
	- *HTTP Only* prevents client-side scripts (JavaScript) from accessing browser cookies, thus preventing XSS (cross-site scripting) attacks.
	- Secure ensures that cookies are sent over the HTTPS domain, preventing interception over unsecured connections.
	- *SameSite* helps chances of CSRF attacks.
		- ==Set-Cookie: sessionId=abc123; HttpOnly:Secure; SameSite=Strict==
3. Session Timeout:
	- Can end session after a predefined period of inactivity.
	- Can terminate sessions after a fixed duration, regardless of activity.
	- Helps reduce the time window available for attackers.
4. Logging and Monitoring:
	- Maintain logs of session creation, access, terminates and various events to detect any unusual activity.
	- Implement real-time monitoring systems to analyse logs and detect anomalies as occur.
	- Use automated tools to generate alerts for suspicious activities, enabling product investigation and response.
5. Additional Measures:
	- Implement MFA (mutli-factor authentication) for security of session.
	- Prompt users to confirm any and all critical actions within a session.
	- Notify users before session timeout due to inactivity, if they want to extend a session.
		This can improve user experience while maintaining security.


### Lecture-7

*Topics*
- About Cookies
- Working
- Types
- Security Considerations
- Code Demo


##### About Cookies

**Definition**

- A cookie, technically known as HTTP cookie, is a small piece of data that's stored within the browser where the end user is interacting with the web application.
- Main purpose of a cookie is to 'remember' the preference of the user over a session. This helps provide the users a more personalized experience
- Each browser has a specific database it uses to store cookies.
	- *Chrome and Firefox use SQLite database*

**Why Cookies ?**

- Helps improve overall user browsing experience:
	- Maintaining login status
	- Shopping carts in online retail stores
	- Store user language, theme appearance, custom settings and preferences.
	- Save website traffic for analytics
	- Reduce CSRF/XSS attacks.

##### Working of Cookies

1. When user visits a web application and interacts with it, a HTTP request is sent to the server.
2. The server generate an appropriate response message and sends it back to the application (browser), along with the session ID generated as well as a cookie header. This is done by the *Set-Cookie* header in the 'headers' part of the response message:
		==Set-Cookie: sessionId=abc123; Expires=Wed,21Oct 2023 07:28:00GMT; Secure; HttpOnly==

3. Attributes to set a Cookie:
	- *Name/Value*: Contains the main data of the cookie
	- *Expires/Max-Age*: This determines the lifespan of the cookie
	- *Path*: Determines the URL for the cookie to be sent
	- *Secure*: A flag used to ensure cookies are sent over HTTPS
	- *HttpsOnly*: Prevents XSS attacks
	- *SameSite*: Prevents CSRF attacks

4. The storage location of cookie at client-side varies depending on the browser and OS. Typically, cookie are stored in databases.
5. For subsequent requests from the client side, the relevant cookies will be included in the *Cookie* header in the 'headers' section of the request message.
		==Cookie: sessionId=abc123; userId=78910; theme=dark;==

6. Now, the server can identify the Session ID and retrieve the corresponding session data. This way, the server 'remembers' the user's preferences and is able to provide a personalized browsing experience.
7. Cookies with the *Expires* or *Max-Age* attribute will be deleted automatically when the time comes. Else, they'll be deleted when the browser is closed.


##### Types of Cookies
--- 

#### **First-party Cookies:**

- These cookies are used by the same application/website that the user is currently interacting with.
- These are considered to be more secure and protected, as they can only be accessed by the website the user is currently visiting.
- First Party cookies help with:
	- Maintaining login status in application
	- Keeping track of and storing user's preferences(language, theme, custom settings)
	- Duration of visits on application
	- Providing a personalized experience

#### **Third-party Cookies:**

- Cookies that get stored in the browser but actually created by some other website which the user isn't currently visiting, are third party cookies.
- Associated with greater security concerns as it exposes users' browsing data to external parties (sometimes without consent).
- These cookies are mainly used for
	- Tracking a user's activities across different websites, to generate targeted ads
	- Analyzing website traffic and performance for analytics.
	- Tailoring social media feeds by tracking user activity
	- Generating user profiles based on data collected about a user's activities across different websites

#### **What happens when we select 'Accept All Cookies' ?**

- Equivalent of a user giving consent to store and use first-party and third-party cookies
- Allows third-party companies to collect browsing data and activity across multiple website. This helps with targeted ad generation, building user profiles, etc.
- Higher risk of data leakage if the third-party companies are compromised.


### Security Considerations

***Measures to take, to protect data stored in Cookies:***

**1. Cookie Attributes:**

- Use attributes and flags like HttpOnly and SameSite
- Helps avoid CSRF and SXX attacks.

**2. Cookie Poisoning:**

- An attacker can modify the contents of cookies to gain unauthorized access.
- Encrypt cookie data using hashes
- Avoid storing critical and sensitive information in cookies.

**3. Man-in-the-Middle Attacks:**

- Attackers can intercept cookies and manipulate between client and server
- Ensure to user *Server* attributes and HTTPS channels for communication

**4. Consent:**

- Read all terms and conditions before accepting all cookies
- Minimize use of third-party cookies unless absolutely necessary.

**5. Others:**

- Cookies are a part of sessions
- Cookies are generated within a session
- Similar security considerations will apply
