from django.shortcuts import render

# Create your views here.
from appa.models import *
from appa.serializers import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView,Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import permission_classes
import json

class AddressViewSet(ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'welcome Hello, World!'}
        return Response(content)

class BookOperations(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



    def create(self, request, *args, **kwargs):
        reqjson = request.data
        if reqjson.get('book_qty')>0 and reqjson.get('book_price')>100:
            return super().create(request)
        else:
            result = {"message": "INcorrect data"}
            return Response(json.dumps(result))

    # @permission_classes(IsAuthenticated,)
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request)