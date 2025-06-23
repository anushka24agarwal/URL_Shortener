# 🔗 URL Shortener

A full-stack **URL shortening service** built with **FastAPI**, **React**, and **PostgreSQL** — fully containerized using Docker.

> <u>Generate short, shareable links just like Bitly or TinyURL!</u>


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
