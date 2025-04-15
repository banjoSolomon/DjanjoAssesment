# Django Celery API - Background Task Processor

This project is a Django REST API that allows users to submit an email and message to be processed asynchronously using **Celery** and **Redis**. The API includes Swagger documentation for easy interaction and is set up for deployment via GitHub Actions to an EC2 instance.

---

## 🚀 Features

- Submit background tasks via API
- Monitor task status
- Celery for background task processing
- Redis as the broker
- Swagger UI for API documentation
- Docker + Docker Compose support
- GitHub Actions for CI/CD deployment

  #  Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Start the application using Docker Compose
Make sure Docker is installed, then run: docker-compose up --build

 API Endpoints
Endpoint	Method	Description
/api/process/	POST	Submit a background task
/api/status/<task_id>/	GET	Get the status of a task
/swagger/	GET	Swagger UI for API interaction

Example POST
json
POST /api/process/
{
  "email": "user@example.com",
  "message": "This is a test message"
}


Example Response
json

{
  "task_id": "7f3c9ab2-f4be-4d42-bf9b-4e963fbf409f"
}


Task Status
Use the returned task_id:

http
GET /api/status/7f3c9ab2-f4be-4d42-bf9b-4e963fbf409f/


Example for AWS EC2 Deployment
EC2 instance public IP like 3.90.123.45:


Feature	URL
Base API	http://3.90.123.45/api/
Process Task	http://3.90.123.45/api/process/
Check Status	http://3.90.123.45/api/status/<task_id>/
Swagger Docs	http://3.90.123.45/swagger/
