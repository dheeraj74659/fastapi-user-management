from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.base import api_router

app = FastAPI(
    title = "User Management API",
    description="A FastAPI based user management system with JWT authentication and RBAC.",
    version="1.0",
    contact={
        "Name": "Dheeraj Kumar",
        "Email": "dheerajkumar74659@gmail.com",
    },
    openapi_tags=[
        {"name": "auth", "description": "Endpoints related to authentication"},
        {"name": "users", "description": "Endpoints related to user management"},
    ]
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # to be changed in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the api router
app.include_router(api_router)


@app.get("/")
async def root():
    """api root function"""
    return {"message": "Welcome to FastAPI User Management API"}