# Tasks
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>

## Main Features
**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

#### The key features are:

* **Fast**: Very high performance
* **Fast to code**: Increase the speed to develop features by about 200% to 300%. 
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. 
* **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.

## Table of Contents
- [Documentation](#documentation)
- [Main Features](#main-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [SQL (Relational) Databases](#sql-relational-databases)



## Documentation
**Framework**:![Static Badge](https://img.shields.io/badge/FastAPI-%2318c482?style=plastic)

**Tutorial-User Guide** : <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

## Requirements

Python 3.8+

FastAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" target="_blank">Starlette</a> for the web parts.
* <a href="https://docs.pydantic.dev/" target="_blank">Pydantic</a> for the data parts.

## Installation

<div class="termy">

```console
$ pip install fastapi
```
</div>

You will also need an ASGI server, for production such as uvicorn

<div class="termy">
  
```console
$ pip install "uvicorn[standard]"
```
</div>

### Run it

Run the server with:

<div class="termy">

```console
$ uvicorn main:app --reload
```
</div>

<details> 
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `uvicorn main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>

***

## SQL (Relational) Databases
You can use a SQL (relational) database using SQL Alchemy
### Install SQL Alchemy
<div class="termy">
  
```console
$ pip install sqlalchemy
```
</div>

### ORM(object-relational mapping)
**FastAPI** works with any database and any style of library to talk to the database.

A common pattern is to use an "ORM": an "object-relational mapping" library.

An ORM has tools to convert ("map") between objects in code and database tables ("relations").

With an ORM, you normally create a class that represents a table in a SQL database, each attribute of the class represents a column, with a name and a type.


