from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt 
from rest_framework.parsers import JSONParser
from starting.models import Snippet
from starting.serializers import SnippetSerializer
from rest_framework import status


def snippet_list(request):
    if request.method=="GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def snippet_detail(request,pk):
    try:
        snippet= Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer= SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method=="PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
