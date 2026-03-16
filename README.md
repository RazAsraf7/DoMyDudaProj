# DoMyDuda – Backend Service

## Overview

DoMyDuda is a backend service designed to manage application data through a REST API.
The project demonstrates building a modern backend system using Python with containerized deployment and database integration.

This project focuses on backend architecture, API design, and containerized environments.

---

## Tech Stack

* Python
* FastAPI
* MongoDB
* Docker
* REST API

---

## Features

* RESTful API for managing application data
* Health check endpoint for service monitoring
* Database persistence using MongoDB
* Containerized deployment using Docker

---

## Architecture

Client Application
↓
FastAPI Backend
↓
MongoDB Database

---

## Project Structure

```
DoMyDudaProj
│
├── app
│   ├── routes
│   ├── models
│   ├── services
│   └── main.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Running the Project

### Clone the repository

```bash
git clone https://github.com/RazAsraf7/DoMyDudaProj
cd DoMyDudaProj
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn app.main:app --reload
```

### Run with Docker

```bash
docker build -t domyduda .
docker run -p 8000:8000 domyduda
```

---

## Example Endpoint

Health check:

```
GET /health
```

Response:

```
OK
```

---

## Purpose

This project was created as part of a personal effort to deepen backend development knowledge and explore API design with Python.
