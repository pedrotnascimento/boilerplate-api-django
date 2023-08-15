from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt 
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from starting.models import Snippet
from starting.serializers import SnippetSerializer
from rest_framework import status


from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer