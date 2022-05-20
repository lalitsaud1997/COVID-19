from dataclasses import field
from rest_framework import serializers
from .models import Coronavirus
from django.utils.formats import number_format


class CoronavirusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coronavirus
        fields = ['country','total_cases', 'new_cases', 'total_deaths' ,'new_deaths' ,'total_recovered', 'active_cases' ,'total_tests' ,'population', 'continent']