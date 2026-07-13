# 📝 Task Manager - 3 Tier Application

A simple 3-Tier Task Manager application built using **HTML, CSS, JavaScript, Flask, MySQL, Docker, and Docker Compose**.

---

# 📐 Architecture

```
                Browser
                   │
                   ▼
         Frontend (Nginx)
                   │
          HTTP REST API
                   │
                   ▼
          Flask Backend
                   │
            SQL Queries
                   │
                   ▼
            MySQL Database
```

---

# 🚀 Features

- Add Tasks
- View Tasks
- Delete Tasks
- REST API
- Dockerized Application
- Docker Compose
- MySQL Database
- Persistent Data
- Health Checks
- Environment Variables

---

# 🛠️ Tech Stack

- HTML5
- CSS3
- JavaScript
- Flask
- MySQL 8
- Docker
- Docker Compose
- Nginx

---

# 📁 Project Structure

```
task-manager/

├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── nginx.conf
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── wait-for-db.sh
│
├── database/
│   └── init.sql
│
├── .env
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# ▶️ Run the Project

Clone the repository:

```bash
git clone <your-repository-url>
cd task-manager
```

Build and start the containers:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

Stop the application:

```bash
docker compose down
```

---

# 🌐 Application URLs

Frontend:

```
http://localhost:8080
```

Backend API:

```
http://localhost:5000
```

Health Check:

```
http://localhost:5000/health
```

---

# 📌 API Endpoints

## Get All Tasks

```http
GET /tasks
```

## Add Task

```http
POST /tasks
```

Request Body:

```json
{
  "title": "Learn Docker"
}
```

## Delete Task

```http
DELETE /tasks/{id}
```

---

# 🐳 Docker Commands

Build Images

```bash
docker compose build
```

Start Containers

```bash
docker compose up
```

View Running Containers

```bash
docker ps
```

View Logs

```bash
docker compose logs -f
```

Stop Containers

```bash
docker compose down
```

Remove Volumes

```bash
docker compose down -v
```

---

# 📚 Learning Goals

This project demonstrates:

- 3-Tier Architecture
- REST API Development
- Docker Images
- Docker Compose
- Container Networking
- Persistent Volumes
- Environment Variables
- Health Checks
- MySQL Integration
- Nginx Static Hosting

---

# 🚀 Future Improvements

- User Authentication
- JWT Security
- Task Status
- Task Due Date
- Task Categories
- Search & Filter
- Edit Tasks
- Kubernetes Deployment
- GitHub Actions CI/CD
- Prometheus Monitoring
- Grafana Dashboard

---

# 👨‍💻 Author

**Mohd Fahad Khan**

DevOps & Cloud Enthusiast

---

# 📄 License

This project is licensed under the MIT License.
