# OpenFaas - Python-FastAPI Template

An OpenFaas template using FastAPI. Find the deployed live demo [here](https://faasd-demo.alexfranz.com).

## Quickstart Guide

Pull the template first from this Github repo using the faas CLI: 

```
faas template pull https://github.com/alfranz/openfaas-fastapi-template
```

To create a new function:

```
faas new --lang dockerfile yournewproject
```

Build the function:

```
faas build -f yournewproject.yml
```

Run locally: 

```
docker run -p 8000:8000 yournewproject:latest
```

## Deployment guide

Easily deploy your Python project with 

- faasd 🐳
- FastAPI 🪄
- Caddy 🔐

Blog article coming soon.