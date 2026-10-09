# Rest API
## Introduction
- Application Programming Interface : Two Software to talk to each other to exchange data.
- Representational State Transfer (Rest) : Standard on which Api's are communicated through web.
- Data from server is received in the form of JSON format.

---

<u>**API endpoints**</u> - A request that is made to the server.


Structure of API communication
```Sequence           
                           GET -> this is an API 
database---Python app - /drinks/<Id>            <-JS app

```
 tejasfavdrinks.com/drinks/5 - this is the url that returns json file with data.

 >NOTE :- 
 >Direct communication bw app (JS app) and database is possible but not encouraged for security reasons, versatility (All share same backend), Modularity and Interoperability.

---

### <u>Different Methods of requesting data from server.</u>

- **GET** - Is to retrive data.
- **POST** - To write new data. (Just adds new data usually duplicates the data and causes error.)
- **DELETE** - To delete stuff.
- **PUT** - To write Update data. (Usually replaces the data)



> CRUD - Create, Read, update, delete  are the things that we need to do with database.

---
## Fast API

- FastAPI is a Python web framework for building APIs. It is used to create backend services that expose data and actions over HTTP, like login endpoints, CRUD APIs, or machine-learning inference services.

People use it because it is fast to develop with and fast at runtime. The main advantages are:

- It uses Python type hints to validate request data automatically.
- It generates interactive API docs for you.
- It supports async code, which helps with I/O-heavy apps.
- It gives clear error messages and strong editor support.
> In practice, FastAPI is a good choice when you want to build an API in Python with less boilerplate and better built-in validation than older frameworks.


**Pydantic** is a fast, Rust-core Python data validation and serialization library controlled by type annotations.

Core Features

- Data Validation: Enforces type constraints at runtime and raises clear ValidationError messages when data is invalid.
- Data Coercion: Automatically converts and parses incoming data (like strings to integers or dates) into the expected shapes.
- Serialization: Converts models easily to dictionaries or JSON using methods like model_dump() and model_dump_json().
- Ecosystem & Tools: Powers popular frameworks like FastAPI, and includes complementary tools like Pydantic Logfire for observability and Pydantic AI for AI agents.

---

### FASTAPI w.r.t FLASK

- Async by default (Can handle a lot concurrent request)
- Easier to use
- Less Adoption and support.

