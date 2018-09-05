from django.contrib import admin

# Register your models here.
from .models import Activity, Employee, Truck


@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):
	list_display = (
		'uuid',
		'category',
		'description',
		'start_date',
		'end_date',
		'token',
		'uri',
	)


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
	list_display = (
		'uuid',
		'identification',
		'first_name',
		'last_name',
		'username',
		'email',
		'is_active',
		'image',
		'state',
	)

	def save_model(self, request, obj, form, change):
		password = obj.password
		obj.set_password(password)
		super().save_model(request, obj, form, change)


@admin.register(Truck)
class AdminTruck(admin.ModelAdmin):
	list_display = (
		'uuid',
		'code',
	)
