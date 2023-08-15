from django.urls import path
from rest_framework import renderers
from . import views 
from . import views_class_based
from . import views_mixin
from . import views_generic
from . import view_view_sets



snippet_list =view_view_sets.SnippetViewSets.as_view({
    'get': 'list',
    'post': 'create',
})

snippet_detail = view_view_sets.SnippetViewSets.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_custom = view_view_sets.SnippetViewSets.as_view({
    'get': 'title_plus_code'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns_viewsets = [
    path("snippets_view_sets/",snippet_list, name="snippet_list"),
    path("snippets_view_sets/<int:pk>/",snippet_detail, name="snippet_detail"),
    path("snippets_view_sets/<int:pk>/title_plus_code/",snippet_custom, name="snippet_title_plus_code"),
]

urlpatterns =  [
    path("snippets/",views.snippet_list ),
    path("snippets/<int:pk>",views.snippet_detail ),
    path("snippets_class_based/",views_class_based.SnippetList.as_view() ),
    path("snippets_class_based/<int:pk>",views_class_based.SnippetDetail.as_view() ),
    path("snippets_mixin/",views_mixin.SnippetList.as_view() ),
    path("snippets_mixin/<int:pk>",views_mixin.SnippetDetail.as_view() ),
    path("snippets_generic/",views_generic.SnippetList.as_view() ),
    path("snippets_generic/<int:pk>",views_generic.SnippetDetail.as_view() ),

    
] + urlpatterns_viewsets