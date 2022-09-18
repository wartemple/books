# drf的常用
## 自定义序列化字段
```
class FooSerializer(ModelSerializer):
    foo = serializers.SerializerMethodField()

    def get_foo(self, obj):
        return "Foo id: %i" % obj.pk
```

## 验证字段
```
class FooSerializer(ModelSerializer):

    foo = CharField(write_only=True)

    class Meta:
        model = Foo
        fields = ["foo", ...]

    def validate(self, data):
        foo = data.pop("foo", None)
        # Do what you want with your value
        return super().validate(data)
```


## 常用的试图集对象
```
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```