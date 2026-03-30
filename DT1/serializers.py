from rest_framework import serializers
from .models import Askari, Report, Supervisor

class AskariSerializer(serializers.ModelSerializer):
    # Hapa tunachukua jina la supervisor badala ya ID tu
    supervisor_name = serializers.ReadOnlyField(source='supervisor.full_name')
    site_name = serializers.ReadOnlyField(source='current_site.site_name')

    class Meta:
        model = Askari
        fields = ['id', 'full_name', 'badge_number', 'phone_number', 'supervisor_name', 'site_name']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
