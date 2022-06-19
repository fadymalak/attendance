from re import I
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from api.permission import UserOnly
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.serializer import AttendanceSerializer,UserSerializer,EmployeeSerializer
from api.logic.attendance import create_attend_login ,\
     create_attend_logout , list_attend 
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from api.models import LogType
from rest_framework import status
from rest_framework.decorators import api_view ,renderer_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from api.service.attendance import AttendanceService
from api.service.employee import EmployeeService
# Create your views here.

class AttendViewSet(ViewSet):
    permission_classes = [UserOnly,IsAuthenticated]
    renderer_classes = [JSONRenderer,]

    def list(self,request):
        user = request.user.id
        data = list_attend(user)
        serial = AttendanceSerializer(data,many=True)
        return Response(serial.data,status=200)

    def retrieve(self,request,pk=None):
        attendance = AttendanceService.get_attendacne_by_id(id=pk)
        if attendance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request,attendance)
        serial = AttendanceSerializer(attendance)
        return Response(data=serial.data,status=status.HTTP_200_OK)

    def create(self,request):
        user= request.user.id
        data = request.data
        type = data.get("type",None)
        if type and type == LogType.LOGIN:
            obj = create_attend_login(user=user,data=data)
        elif type == LogType.LOGOUT:
            obj = create_attend_logout(user=user,data=data)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serial = AttendanceSerializer(obj)
        return Response(data=serial.data,status=status.HTTP_201_CREATED)



@api_view(["POST",])
@csrf_exempt
@renderer_classes([JSONRenderer,])
def CreateUserAPI(request):
    data = request.data
    user_serial = UserSerializer(data=data)
    if user_serial.is_valid(raise_exception=True):
        user = EmployeeService.create_employee(user_serial.validated_data)
        serializer = EmployeeSerializer(user)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)