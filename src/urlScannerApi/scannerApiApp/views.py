from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializer import DataSerializer
from .tasks import backgroundThread

# Create your views here.
@api_view(['GET'])
def getData(request):
    app= Data.objects.all()
    serializer= DataSerializer(app, many=True)
    return Response(serializer.data)

""" 
@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)

    # Check if the serializer is valid
    if serializer.is_valid():
        # Save the data if valid
        serializer.save()
        # Return the serialized data with HTTP status 201 (Created)
        return Response(serializer.data, status=201)
    else:
        # If the serializer is invalid, return the errors
        return Response(serializer.errors, status=400)
 """

@api_view(['POST'])
def startBackgroundTask(request):
    url= request.data.get('url')
    if not url:
        return Response({"error": "URL is required"}, status=400)

    #create new entry
    task= Data.objects.create(url=url, status='pending')

    backgroundThread(url,task.id)

    return Response({"message": "Task started", "task_id": task.id}, status=202)



@api_view(['GET'])
def getData(request,taskId)
    try:
        task=UrlTask.objects.get(id=taskId)
    except Data.DoesNotExist:
        return Response({"error": "Task not found."}, status=404)
    
    if task.status=='completed':
        return Response({
            "status": task.status,
            "result": task.result  # JSON result or error message
        })
    
    else:
        return Response({
            "status": task.status,
            "message": "Task is still in progress."
        })
