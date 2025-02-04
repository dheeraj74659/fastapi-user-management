# 🚀 FastAPI User Management API

A **FastAPI-based** user management system with **JWT authentication** and **role-based access control (RBAC)**, using **PostgreSQL & Docker**.

## 📌 Features
- **User Registration & Login** with JWT authentication
- **Role-Based Access Control (RBAC)**
- **Async Database Operations** using SQLAlchemy & PostgreSQL
- **API Documentation** with Swagger (OpenAPI)
- **Dockerized Deployment**
- **CORS Enabled** for frontend integration

---

## 🛠️ Installation (Local Setup)

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/fastapi-user-management.git
cd fastapi-user-management
```

### 2️⃣ **Create & Activate a Virtual Environment**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Set Up Database (PostgreSQL Required)**
```sh
export DATABASE_URL="postgresql+asyncpg://admin:password@localhost:5432/user_db"  # Mac/Linux
set DATABASE_URL="postgresql+asyncpg://admin:password@localhost:5432/user_db"  # Windows
```

### 5️⃣ **Run Database Migrations**
```sh
alembic upgrade head
```

### 6️⃣ **Run the Application**
```sh
uvicorn app.main:app --reload
```
📌 Open API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚀 Running with Docker

### 1️⃣ **Build & Start Containers**
```sh
docker-compose up --build -d
```
### 2️⃣ **Apply Migrations in Docker**
```sh
docker exec -it fastapi_app alembic upgrade head
```

### 3️⃣ **Access the API**
📌 Open API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)


## 🔗 API Endpoints

| Method | Endpoint       | Description            |
|--------|---------------|------------------------|
| POST   | `/auth/login` | User login (JWT)       |
| POST   | `/users/`     | Create new user        |
| GET    | `/users/`     | List all users         |
| GET    | `/users/{id}` | Get user by ID         |

---

## 🛠️ Tech Stack
- **FastAPI** (Backend Framework)
- **PostgreSQL** (Database)
- **SQLAlchemy** (ORM + Async Support)
- **JWT Authentication** (Security)
- **Alembic** (Migrations)
- **Docker & Docker Compose** (Containerization)
