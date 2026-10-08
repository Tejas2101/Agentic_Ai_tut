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




