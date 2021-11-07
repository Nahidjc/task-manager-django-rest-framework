from rest_framework import serializers
from .models import Todo


class TodoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        # feilds = ('id', 'title', 'description', 'completed')
