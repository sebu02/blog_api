from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from blog.models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['name','username','password']
        
    def create(self,validated_data):
        username=self.validated_data['username']
        name=self.validated_data['name']
        password=self.validated_data['password']
        user=User(username=username,name=name)
        user.set_password(password)
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if not User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError('username does not exists')
        user = User.objects.get(username=validated_data['username'])

        creds = {
            'username': user.username,
            'password': validated_data['password']
        }
        
        user = None
        data = {}
        user = authenticate(**creds)
        
        if not user:
            raise serializers.ValidationError('Invalid credentials')
            
        refresh = TokenObtainPairSerializer.get_token(user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
    
        
        
class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True) 
    class Meta:
        model=BlogPost
        fields=['title','content','author']
        
        
class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields=['author','post','content']
        
class GetBlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=BlogPost
        fields=['title','content','author']
        
class GetCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields=['author','content','post']
        
        
class  ReplyCommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields=['author','content','post','parent']
        


