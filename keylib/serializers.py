from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.Serializer):
    
    bname = serializers.CharField(max_length=100)
    bauthor = serializers.CharField(max_length=100)
    bquantity = serializers.IntegerField() 

    def create(self, validate_data):
        return Library.objects.create(**validate_data)


    def update(self, instance, validated_data):
        instance.bname = validated_data.get('bname',instance.bname)
        instance.bauthor = validated_data.get('bauthor',instance.bauthor)
        instance.bquantity = validated_data.get('bquantity',instance.bquantity) 

        instance.save()

        return instance        