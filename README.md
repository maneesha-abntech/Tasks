# Tasks
![logo-teal](https://github.com/maneesha-abntech/Tasks/assets/154917046/517d8d74-c691-471a-9ab8-861056b88dfe)

**Framework**:![Static Badge](https://img.shields.io/badge/FastAPI-%2318c482?style=plastic)


## Documentation
**Tutorial-User Guide** : <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

The key features are:

* **Fast**: Very high performance
* **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
* **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.

## Requirements

Python 3.8+

FastAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> for the web parts.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> for the data parts.

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

