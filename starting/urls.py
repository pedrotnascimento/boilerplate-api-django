from django.urls import path

from . import views 
from . import views_class_based
from . import views_mixin
from . import views_generic
from . import view_view_sets
urlpatterns =  [
    path("snippets/",views.snippet_list ),
    path("snippets/<int:pk>",views.snippet_detail ),
    path("snippets_class_based/",views_class_based.SnippetList.as_view() ),
    path("snippets_class_based/<int:pk>",views_class_based.SnippetDetail.as_view() ),
    path("snippets_mixin/",views_mixin.SnippetList.as_view() ),
    path("snippets_mixin/<int:pk>",views_mixin.SnippetDetail.as_view() ),
    path("snippets_generic/",views_generic.SnippetList.as_view() ),
    path("snippets_generic/<int:pk>",views_generic.SnippetDetail.as_view() ),
    # path("snippets_view_sets/",view_view_sets.SnippetList.as_view() ),
    # path("snippets_view_sets/<int:pk>",view_view_sets.SnippetDetail.as_view() ),
]