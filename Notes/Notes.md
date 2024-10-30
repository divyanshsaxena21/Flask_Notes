
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
