from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import status,generics,filters
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView


from blog.api.v1.serializers.blog_serializers import *


class Register(APIView):
    permission_classes=[AllowAny]
    
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'successfully registered'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Login(APIView):
    permission_classes=[AllowAny]
    
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.validated_data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
class BlogCreate(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'successfully uploaded'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
 
class BlogUpdate(APIView):
    permission_classes=[IsAuthenticated]
    
    def put (self,request,id):
        blog=BlogPost.objects.get(pk=id)
        serializer=BlogSerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'successfully uploaded'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
        
class BlogListView(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=GetBlogSerializer
    queryset=BlogPost.objects.all()
    
    
class BlogDelete(ListAPIView):
    permission_classes=[IsAuthenticated]
    
    def delete(self,request,id):
        if not BlogPost.objects.filter(id=id).exists():
            return Response({'message': 'blog does not exist'}, status=status.HTTP_404_NOT_FOUND)
        blog = BlogPost.objects.get(pk=id)
        blog.delete()
        return Response({'message': 'blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
  
    
class BlogRetrieve(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,id):
        blog=BlogPost.objects.get(id=id)
        serializer=GetBlogSerializer(blog)
        return Response(serializer.data)
                  

class CommentPost(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'commented successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
        
class CommentUpdate(APIView):
    permission_classes=[IsAuthenticated]
    
    def put(self,request,id):
        comment=Comment.objects.get(id=id)
        serializer=CommentSerializer(comment,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'commented successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class CommentDelete(ListAPIView):
    permission_classes=[IsAuthenticated]
    
    def delete(self,request,id):
        if not Comment.objects.filter(id=id).exists():
            return Response({'message': 'blog does not exist'}, status=status.HTTP_404_NOT_FOUND)
        comment = Comment.objects.get(pk=id)
        comment.delete()
        return Response({'message': 'blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class CommentRetrieve(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,id):
        comment=Comment.objects.get(id=id)
        serializer=CommentSerializer(comment)
        return Response(serializer.data)


class CommentList(ListAPIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,id):
        comment=Comment.objects.filter(post=id)
        serializer=GetCommentSerializer(comment)
        return Response(serializer.data)
    

class BlogSearch(generics.ListCreateAPIView):
    search_fields=['title']
    filter_backends=(filters.SearchFilter,)
    queryset=BlogPost.objects.all()
    serializer_class =  GetBlogSerializer
       
        
        
        
        
        

            
            
            
            
