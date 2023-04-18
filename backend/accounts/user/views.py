from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view  
from rest_framework.response import Response

@api_view(['POST'])        # @api_view는 데이터가 오고 갈 때만 쓰인다.
def UserInfo(request):     # GET 요청은 페이지를 연결(render 사용)
    print(request.data)
    serializer = UserInfoSerializer(data = request.data)
    if serializer.is_valid():
        print("is_vaild..")
        print(serializer.save())
    else:
        print("error")
    print(serializer.data)
    return Response(serializer.data)

def login(request):
    return render(request, 'register.html')