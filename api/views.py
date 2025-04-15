from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProcessRequestSerializer
from .tasks import process_data
from celery.result import AsyncResult

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProcessView(APIView):
    @swagger_auto_schema(
        operation_description="Queue a background task with email and message",
        request_body=ProcessRequestSerializer,
        responses={
            202: openapi.Response(description="Task has been accepted", examples={
                "application/json": {"task_id": "123abc"}
            }),
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = ProcessRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            task = process_data.delay(email, message)
            return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusView(APIView):
    @swagger_auto_schema(
        operation_description="Get the status of a background task",
        manual_parameters=[
            openapi.Parameter(
                'task_id',
                openapi.IN_PATH,
                description="The Celery task ID",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response(description="Task status", examples={
                "application/json": {
                    "task_id": "123abc",
                    "status": "SUCCESS",
                    "result": "Email sent to user@example.com"
                }
            })
        }
    )
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        return Response({
            'task_id': task_id,
            'status': result.status,
            'result': result.result if result.ready() else None
        })
