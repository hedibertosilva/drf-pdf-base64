from rest_framework import serializers
from reports.models import Reports


class ReportsList(serializers.ModelSerializer):

    class Meta:
        model = Reports
        fields = ['id', 'date', 'title']


   
