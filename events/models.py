import uuid as uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Activity(models.Model):
	CATEGORY_CHOICES = (
		('forniture', 'Forniture'),
		('production', 'Production')
	)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
	description = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	token = models.CharField(max_length=200, blank=True, null=True)
	uri = models.CharField(max_length=200, blank=True, null=True)
	employees = models.ManyToManyField('Employee', related_name='activities', blank=True)
	trucks = models.ManyToManyField('Truck', related_name='activities', blank=True)

	class Meta:
		ordering = ['start_date', 'category']

	def __str__(self):
		return self.description


class Employee(User):
	STATES_CHOICES = (
		('off', 'Off'),
		('no show', 'No show'),
		('no call', 'No call'),
		('sick', 'Sick'),
		('out', 'Out')
	)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	identification = models.CharField(max_length=45)
	image = models.ImageField(upload_to='media/', max_length=200, blank=True, null=True)
	state = models.CharField(choices=STATES_CHOICES, max_length=10, blank=True, null=True)

	@property
	def get_activities(self):
		return self.activities.all()

	def __str__(self):
		return f'{ self.first_name } { self.last_name }'


class Truck(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	code = models.IntegerField()

	def __str__(self):
		return f'Truck-{ self.code }'
