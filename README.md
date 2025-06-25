# 🔗 URL Shortener

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-4169E1?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-20.10%2B-2496ED?logo=docker)
![React](https://img.shields.io/badge/React-18%2B-61DAFB?logo=react)

A full-stack **URL shortening service** built with **FastAPI**, **React** and **PostgreSQL**, fully containerized using Docker.


## 🚀 Features

- 🔧 **FastAPI** backend with REST API endpoints
- 🎨 **React** frontend with clean UI and Axios integration
- 🐘 **PostgreSQL** for persistent URL storage
- 🐳 Fully **Dockerized** setup using Docker Compose
- 🔁 Supports **URL redirecting**, short code generation, and API usage


## 📦 Tech Stack

| Layer       | Technology       |
|-------------|------------------|
| 🧠 Backend   | **FastAPI**, SQLAlchemy, Pydantic |
| 🌐 Frontend | **React**, Axios |
| 🐘 Database | **PostgreSQL**   |
| 📦 DevOps   | **Docker**, Docker Compose |


## 🛠️ Local Setup

> Make sure you have **Docker** and **Docker Compose** installed.

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/url_shortener.git
cd url-shortener

# 2. Build and start services
docker compose build
docker compose up
