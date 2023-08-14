from .models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance

# SnippetSerializer class is replicating a lot of information that's also contained in the Snippet model.
# ModelSerializer classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


##shell
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# snippet = Snippet(code='foo = "bar"\n')
# snippet.save()
# snippet = Snippet(code='print("hello, world")\n')
# snippet.save()
# serializer = SnippetSerializer(snippet)
# serializer.data
## {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
# content = JSONRenderer().render(serializer.data)
# content
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'
# import io
# stream = io.BytesIO(content)
# data = JSONParser().parse(stream)
# serializer = SnippetSerializer(data=data)
# serializer.is_valid()
# True
# serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
# serializer.save()