# OpenFaas - Python-FastAPI Template

An OpenFaas template using FastAPI. See the deployed live version [here](fastapi.alexfranz.com).

## Quickstart Guide

Pull the template first from this Github page: 

```
faas template pull alfranz/openfaas-python3-fastapi-template
```

To create a new function:

```
faas new --lang python3-fastapi yournewproject
```

Build the function:

```
faas build -f yournewproject.yml
```

```
docker run -p 8000:8000 yournewproject:latest
```

## Deployment guide

Easily deploy your Python project using 

- faasd 🐳
- FastAPI 🪄
- Caddy 🔐

see blog article here.