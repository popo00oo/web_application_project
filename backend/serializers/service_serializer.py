from rest_framework import serializers
from service.models import Lost, Notice


class LostSer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'


class NoticeSer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Notice
        fields = '__all__'
