# OAuth2 with Password (and hashing), Bearer with JWT tokens



### Installation

***clone the repository***:
```bash
	git clone https://github.com/Hemantr05/The-API-Garage/tree/main/FastAPI-examples && cd fastapi_crud_mongo
```

***install requirements***:
```bash
	pip install -r requirements.txt
```


### Handle JWT tokens

Import the modules installed.

Create a random secret key that will be used to sign the JWT tokens.

To generate a secure random secret key use the command:

```bash
	$ openssl rand -hex 32
```


### Usage:

```bash
	$ uvicorn main:app --reload 
```