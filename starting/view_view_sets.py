from rest_framework.decorators import  action
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response

from starting.models import Snippet
from starting.serializers import SnippetSerializer


class SnippetViewSets(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer = SnippetSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def title_plus_code(self, request, *args, **kwargs):
        snippet: Snippet =self.get_object()
        return Response(f"{snippet.title} --{snippet.code}")
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
