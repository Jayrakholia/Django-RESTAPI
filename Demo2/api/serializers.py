from rest_framework import serializers
from api.models import User, Competition, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['name','birth_date','gender']
        read_only_fields =['id']
    


# class CompetitionSerializer(serializers.ModelSerializer):
    
    
# class EntrySerializer(serializers.ModelSerializer):
    