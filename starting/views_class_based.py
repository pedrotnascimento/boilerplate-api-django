from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt 
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from starting.models import Snippet
from starting.serializers import SnippetSerializer
from rest_framework import status

    
class SnippetList(APIView):

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
            return  snippet
        except:
            raise Http404
        

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        try:
            snippet= Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer= SnippetSerializer(snippet)
            return Response(serializer.data)
    def put(self, request, pk, format=None):
        data = JSONParser().parse(request)
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
