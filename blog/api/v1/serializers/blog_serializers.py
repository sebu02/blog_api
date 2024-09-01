from rest_framework import serializers


from blog.models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['name']
        
    def create(self,validated_data):
        username=self.validated_data['username']
        name=self.validated_data['name']
        password=self.validated_data['password']
        user=User(username=username,name=name)
        user.set_password(password)
        user.save()
        return user
        
        
class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=BlogPost
        fields='__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields='__all__'
        


