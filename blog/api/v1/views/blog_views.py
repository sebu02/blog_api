from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import status,generics,filters
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


from blog.api.v1.serializers.blog_serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


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
    
    
class BlogCUD(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'successfully uploaded'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put (self,request,pk):
        blog=BlogPost.objects.get(pk=pk)
        serializer=BlogSerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'successfully uploaded'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        if not BlogPost.objects.filter(id=id).exists():
            return Response({'message': 'blog does not exist'}, status=status.HTTP_404_NOT_FOUND)
        blog = BlogPost.objects.get(pk=id)
        blog.delete()
        return Response({'message': 'blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
  
            
class BlogListView(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=GetBlogSerializer
    queryset=BlogPost.objects.all()
    pagination_class = StandardResultsSetPagination
    
      
class BlogRetrieve(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    
    def get(self,request,id):
        blog=BlogPost.objects.get(id=id)
        serializer=GetBlogSerializer(blog)
        return Response(serializer.data)
    
                  

class CommentCUD(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'commented successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        comment=Comment.objects.get(id=id)
        serializer=CommentSerializer(comment,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'commented successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        if not Comment.objects.filter(id=id).exists():
            return Response({'message': 'blog does not exist'}, status=status.HTTP_404_NOT_FOUND)
        comment = Comment.objects.get(pk=id)
        comment.delete()
        return Response({'message': 'blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class CommentRetrieve(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    
    def get(self,request,id):
        comment=Comment.objects.get(id=id)
        serializer=CommentSerializer(comment)
        return Response(serializer.data)


class CommentList(ListAPIView):
    permission_classes=[IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    
    def get(self,request,id):
        queryset = Comment.objects.filter(post_id=id)
        serializer_class = GetCommentSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class BlogSearch(generics.ListCreateAPIView):
    search_fields=['title']
    filter_backends=(filters.SearchFilter,)
    queryset=BlogPost.objects.all()
    serializer_class =  GetBlogSerializer
    
    
class CommentReply(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer=ReplyCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response({'message':'comment replied successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        

        
        
        


        
        
        

            
            
            
            
