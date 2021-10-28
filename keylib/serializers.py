from rest_framework import serializers
from .models import Library


class LibrarySerializer(serializers.ModelSerializer):

    
    # Validators
    def start_with_cap(value):
        if value[0].islower():
            raise serializers.ValidationError("First word should be capital")


    bname = serializers.CharField(validators=[start_with_cap])
    class Meta:
        model = Library
        fields = '__all__'


    
    def validate_bquantity(self,value):
        if value>=100:
            raise serializers.ValidationError('Max Quantity For Book')
        return value        

    def validate(self,data):
        bn=data.get('bname')
        ba=data.get('bauthor')
        bq=data.get('bquantity')

        if bn.lower()=='ilmaan' and ba.lower()!='delhi':
            raise serializers.ValidationError('Delhi se hai bheai')
        return data 








# class LibrarySerializer(serializers.Serializer):
    
    # bname = serializers.CharField(max_length=100)
    # bauthor = serializers.CharField(max_length=100)
    # bquantity = serializers.IntegerField()  

    # def create(self, validate_data):
    #     return Library.objects.create(**validate_data)


    # def update(self, instance, validated_data):
    #     instance.bname = validated_data.get('bname',instance.bname)
    #     instance.bauthor = validated_data.get('bauthor',instance.bauthor)
    #     instance.bquantity = validated_data.get('bquantity',instance.bquantity) 

    #     instance.save()

    #     return instance     


    # def validate_bquantity(self,value):
    #     if value>=100:
    #         raise serializers.ValidationError('Max Quantity For Book')
    #     return value        

    # def validate(self,data):
    #     bn=data.get('bname')
    #     ba=data.get('bauthor')
    #     bq=data.get('bquantity')

    #     if bn.lower()=='ilmaan' and ba.lower()!='delhi':
    #         raise serializers.ValidationError('Delhi se hai bheai')
    #     return data    