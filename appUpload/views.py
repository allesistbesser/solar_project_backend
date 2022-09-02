from django.shortcuts import render
from django.http.response import HttpResponse
from .serilaziers import CommentSerializer , ProductsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment , Products

def home(request):
    return HttpResponse("Hallo Welt")
    # return render(request, 'home.html')

def download_file(request):
    # # Define Django project base directory
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # # Define text file name
    # filename = 'tw.pdf'
    # # Define the full file path
    # filepath = BASE_DIR + '/templates/' + filename
    # # Open the file for reading content
    # path = open(filepath, 'r')
    # # Set the mime type
    # mime_type, _ = mimetypes.guess_type(filepath)
    # # Set the return value of the HttpResponse
    # response = HttpResponse(path, content_type=mime_type)
    # # Set the HTTP header for sending to browser
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # # Return the response value
    # return response
    with open('./templates/Musterbrief-Anmeldung-Balkonkraftwerk-Solaranlage.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=tw.pdf'
        return response

class Commentview(APIView):
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        comments = Comment.objects.filter(status="published")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        
class Productsview(APIView):
    def get(self,request):
        products = Products.objects.filter(status="published")
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)