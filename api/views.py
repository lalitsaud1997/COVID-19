from rest_framework import generics
from .models import Coronavirus
from .serializers import CoronavirusModelSerializer

# Create your views here.
class CoronavirusListAPIView(generics.ListAPIView):
    queryset = Coronavirus.objects.all()
    queryset = queryset.extra(select={
        'total_cases': 'CAST(REPLACE(total_cases, ",","") AS INT)',
        'total_deaths': 'CAST(REPLACE(total_deaths, ",","") AS INT)',
        'total_recovered': 'CAST(REPLACE(total_recovered, ",","") AS INT)',})
    serializer_class = CoronavirusModelSerializer
    search_fields    = ['country', 'continent']
    ordering_fields  = ['total_cases', 'total_deaths', 'total_recovered']

class CoronavirusDetailAPIView(generics.RetrieveAPIView):
    queryset = Coronavirus.objects.all()
    serializer_class = CoronavirusModelSerializer
    lookup_field = 'slug'