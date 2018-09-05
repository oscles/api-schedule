# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .serializers import ActivitySerializer, EmployeeSerializer, TruckSerializer
from .models import Activity, Employee, Truck


class ActivityViewset(ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	filter_fields = ('start_date', 'end_date', 'category')


class EmployeeViewset(ReadOnlyModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	filter_backends = (DjangoFilterBackend, )
	filter_fields = ('identification', 'username')


class TruckViewset(ReadOnlyModelViewSet):
	queryset = Truck.objects.all()
	serializer_class = TruckSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('code', )
