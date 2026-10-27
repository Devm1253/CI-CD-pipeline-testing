from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response

def home(request):
    return HttpResponse("<h1>Hello, World!, This is the home page.</h1>")

def about(request):
    return HttpResponse("<h1>This is the about page.</h1>")

@api_view(['GET'])
def api_home(request):
    return Response({
        "message": "CI/CD pipeline is working successfully!",
        "status": "success",
        "version": "1.1",
    })
