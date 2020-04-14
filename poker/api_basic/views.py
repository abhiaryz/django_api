from django.shortcuts import render
from .models import Server
from .serializers import serverSerializer
from django.http import JsonResponse ,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def server_data(request):

    if request.method == 'GET':
        servers = Server.objects.all()
        serializer = serverSerializer(servers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serverSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def article_detail(request, pk):
    try:
        server = Server.objects.get(pk=pk)

    except Server.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serverSerializer(server)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServerSerializer(server,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        server.delete()
        return HttpResponse(status=204)


