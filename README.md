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
EC2 instance public IP like 35.85.59.155 :


Feature	URL
Base API	http://35.85.59.155 /api/
Process Task	http://35.85.59.155/api/process/
Check Status	http://35.85.59.155/api/status/<task_id>/
Swagger Docs	http://35.85.59.155 /swagger/



🧩 Components Description
1. Django REST Framework (DRF)
Handles API requests (POST /process/ and GET /status/<task_id>/).

Serializes input using ProcessRequestSerializer.

Uses class-based views (APIView) for structure.

2. Swagger (drf_yasg)
Provides interactive API documentation.

Accessible via /swagger/.

3. Celery
Task queue manager used to offload time-consuming operations.

Tasks are created in Django and executed in the background.

Defined in tasks.py.

4. Redis
Serves as:

Message Broker for Celery

Result Backend to store task status/results

5. Celery Worker
Separate process (Docker container) that:

Listens for tasks from Redis

Executes them

Stores the results in Redis

6. Docker & Docker Compose
Dockerizes:

Django app (web)

Redis broker

Celery worker

Makes the system portable and easy to deploy

7. AWS EC2
Hosts the entire application

Public IP provides access to endpoints:

http://<EC2-IP>/api/process/

http://<EC2-IP>/swagger/






🔄 Request Flow Summary
User sends POST request to /api/process/ with email and message.

Django validates input, then queues the task using Celery.

Celery pushes the task to Redis.

Celery worker picks up the task from Redis and simulates a long-running operation.

User can query task status at /api/status/<task_id>/ to check progress.

Swagger UI allows testing and documentation browsing.

📦 Deployment Highlights
CI/CD via GitHub Actions pushes the code to EC2 on every master branch update.

SSH and Docker Compose are used to:

Stop existing containers

Rebuild the app

Spin it up again cleanly

Redis runs in its own container

Celery worker is decoupled from Django and runs independently
