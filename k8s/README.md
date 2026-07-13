# 🚀 Task Manager - 3 Tier Kubernetes Application

A full-stack Task Manager application deployed on Kubernetes using a 3-tier architecture.

The application contains:

- Frontend → Nginx + HTML/CSS/JavaScript
- Backend → Python Flask API + Gunicorn
- Database → MySQL
- Container Platform → Docker
- Orchestration → Kubernetes (Kind Cluster)

---

# 🏗️ Architecture

```
                User Browser
                     |
                     |
             Frontend Service
                NodePort
               Port:30080
                     |
                     |
            Frontend Pods (Nginx)
                     |
                     |
        Backend Service (ClusterIP)
              Port:5000
                     |
                     |
            Backend Pods (Flask)
                     |
                     |
          MySQL Service (ClusterIP)
              Port:3306
                     |
                     |
             MySQL Pod
                     |
                     |
             Persistent Volume
```

---

# 📂 Project Structure

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
├── k8s/
│   ├── namespace.yml
│   ├── mysql-secret.yml
│   ├── mysql-pv.yml
│   ├── mysql-pvc.yml
│   ├── mysql-deployment.yml
│   ├── mysql-service.yml
│   ├── backend-deployment.yml
│   ├── backend-service.yml
│   ├── frontend-deployment.yml
│   └── frontend-service.yml
│
├── docker-compose.yml
└── README.md
```

---

# 🛠️ Technologies Used

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Web Server | Nginx |
| Backend | Python Flask |
| API Server | Gunicorn |
| Database | MySQL 8 |
| Container | Docker |
| Orchestration | Kubernetes |
| Local Cluster | Kind |
| Storage | PV/PVC |
| Security | Kubernetes Secret |

---

# 🐳 Build Docker Images

## Frontend Image

```bash
cd frontend

docker build -t task-manager-frontend:latest .
```

---

## Backend Image

```bash
cd backend

docker build -t task-manager-backend:latest .
```

---

# ☸️ Kubernetes Deployment

## Create Namespace

```bash
kubectl apply -f namespace.yml
```

Check:

```bash
kubectl get namespace
```

---

# 🔐 Create Secret

Database credentials are stored using Kubernetes Secret.

```bash
kubectl apply -f mysql-secret.yml
```

Check:

```bash
kubectl get secret -n task
```

---

# 💾 Storage Setup

Create Persistent Volume:

```bash
kubectl apply -f mysql-pv.yml
```

Create Persistent Volume Claim:

```bash
kubectl apply -f mysql-pvc.yml
```

Check:

```bash
kubectl get pv

kubectl get pvc -n task
```

Expected:

```
STATUS: Bound
```

---

# 🗄️ Deploy MySQL

Apply Deployment:

```bash
kubectl apply -f mysql-deployment.yml
```

Create Service:

```bash
kubectl apply -f mysql-service.yml
```

Check:

```bash
kubectl get pods -n task
```

Expected:

```
mysql-deployment   Running
```

---

# ⚙️ Deploy Backend

Load image into Kind:

```bash
kind load docker-image task-manager-backend:latest --name fwd-cluster
```

Deploy:

```bash
kubectl apply -f backend-deployment.yml
```

Create Service:

```bash
kubectl apply -f backend-service.yml
```

Check:

```bash
kubectl get pods -n task
```

---

# 🌐 Deploy Frontend

Load image:

```bash
kind load docker-image task-manager-frontend:latest --name fwd-cluster
```

Deploy:

```bash
kubectl apply -f frontend-deployment.yml
```

Create Service:

```bash
kubectl apply -f frontend-service.yml
```

---

# 🔎 Check All Resources

```bash
kubectl get all -n task
```

Example:

```
Pods:
frontend     Running
backend      Running
mysql        Running


Services:
frontend-task-service
backend-task-service
mysql-service
```

---

# 🌍 Access Application

Frontend:

```
http://localhost:8081
```

---

# 🔍 Test Backend API

Port forward:

```bash
kubectl port-forward svc/backend-task-service 5001:5000 -n task
```

Test:

```bash
curl http://localhost:5001/
```

Response:

```json
{
 "message":"Task Manager API Running"
}
```

Health:

```bash
curl http://localhost:5001/health
```

Response:

```json
{
 "status":"UP"
}
```

---

# 📝 Kubernetes Commands Used

Check pods:

```bash
kubectl get pods -n task
```

Check services:

```bash
kubectl get svc -n task
```

Check logs:

```bash
kubectl logs <pod-name> -n task
```

Describe resources:

```bash
kubectl describe pod <pod-name> -n task
```

Delete resources:

```bash
kubectl delete -f filename.yml
```

---

# 🔐 Security

Database credentials are managed using Kubernetes Secrets.

Features:

✅ No hardcoded passwords  
✅ Environment variables  
✅ SecretKeyRef usage  
✅ Persistent database storage  

---

# 🚀 Future Improvements

- Add Ingress Controller
- Add HTTPS using TLS
- Add Horizontal Pod Autoscaler
- Add CI/CD with GitHub Actions
- Push images to Docker Hub
- Add Monitoring using Prometheus and Grafana

---

# 👨‍💻 Author

Fahad Khan

DevOps Learning Project

---

⭐ If you like this project, give it a star!
