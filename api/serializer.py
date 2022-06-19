from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    

class EmployeeSerializer(serializers.Serializer):
    user = UserSerializer()

class AttendanceLogSerializer(serializers.Serializer):
    type = serializers.CharField()
    created_at = serializers.DateTimeField()

class AttendanceSerializer(serializers.Serializer):
    employee = EmployeeSerializer(read_only=True)
    date = serializers.DateField()
    status = serializers.CharField()