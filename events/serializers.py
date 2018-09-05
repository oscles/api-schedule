from rest_framework import serializers
from .models import Activity, Employee, Truck


class EmployeeSerializer(serializers.ModelSerializer):
	full_name = serializers.ReadOnlyField(source='get_full_name')

	class Meta:
		model = Employee
		fields = (
			'uuid',
			'identification',
			'first_name',
			'last_name',
			'full_name',
			'username',
			'email',
			'is_active',
			'image',
			'state',
		)


class TruckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Truck
		fields = (
			'uuid',
			'code',
		)


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
	# employees = serializers.SerializerMethodField()
	# trucks = serializers.SerializerMethodField()

	class Meta:
		model = Activity
		fields = (
			'uuid',
			'category',
			'description',
			'start_date',
			'end_date',
			'token',
			'uri',
			'employees',
			'trucks'
		)

	def get_employees(self, instance):
		return EmployeeSerializer(instance=instance.employees, many=True).data

	def get_trucks(self, instance):
		return TruckSerializer(instance=instance.trucks, many=True).data
