from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'creation_date', 'due_date', 'status']
        
        def update(self, validated_data, instance):
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.creation_date = validated_data.get('creation_data', instance.creation_date)
            instance.due_date = validated_data.get('due_data', instance.due_date)
            instance.save()
            return instance