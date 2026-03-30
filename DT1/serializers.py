from rest_framework import serializers
from .models import Askari, Report, ContactMessage

class AskariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Askari
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
