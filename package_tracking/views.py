from rest_framework import viewsets

from .models import Package
from .serializers import PackageSerializer
# Create your views here.


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
