from django.shortcuts import render
from rest_framework.views import APIView
from .serilizers import *
from rest_framework.response import Response

# Create your views here.
class CreateData(APIView):

    def post(self, request):
        
        ser_obj = Machine(data = request.data)
        if ser_obj.is_valid():
            ser_obj.save() # data base mein create ho jaayega
            all_users = User.objects.all()
            ser_new_obj = Machine(all_users, many = True)
            return Response(data = ser_new_obj.data)
        else:
            return Response(ser_obj.errors)


class GetData(APIView):

    def get(self, request, pk):
        u1 = User.objects.get(id= pk)
        ser_obj = Machine(u1)
        return Response(ser_obj.data)
    

class UpdateData(APIView):

    def put(self, request, pk):
        u1 = User.objects.get(id=pk)
        ser_obj = Machine(u1, data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            all_users = User.objects.all()
            ser_new_obj = Machine(all_users, many = True)
            return Response(data = ser_new_obj.data)
        else:
            return Response(ser_obj.errors)
        

class DeleteData(APIView):

    def delete(self, request, pk):
        u1 = User.objects.get(id=pk)
        u1.delete()
        all_users = User.objects.all()
        ser_new_obj = Machine(all_users, many = True)
        return Response(data = ser_new_obj.data)
    

class AllData(APIView):

    def get(self, request):
        all_users = User.objects.all()
        ser_new_obj = Machine(all_users, many = True)
        return Response(data = ser_new_obj.data)