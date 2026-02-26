from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.conf import settings
import re


class User(AbstractUser):
    phone_number  = models.CharField(max_length=15, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    # Phone numerber validation written in the manager file, so we can reuse it in both create_user and create_superuser methods.
    objects = CustomUserManager()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class Nurse(User):
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    license_id = models.TextField(max_length=255, unique=True)
    emergency_contact = models.CharField(max_length=15)
    is_on_duty = models.BooleanField(default=True)
    num_of_patients = models.PositiveIntegerField(default=0)
    is_senior_nurse = models.BooleanField(default=False)
    
    # @property
    # def current_patient_count(self):
    #     return self.assignments.filter(is_active=True).count()    
    
    
# Connection Table of [Nurses <-----> Patients] (M:N Relationship)
class NurseAssignments(models.Model):
    SLOT_CHOICES = [
        ('MOR', 'Morning'),
        ('AFT', 'Afternoon'),
        ('EVE', 'Evening'),
    ]

    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='assignments')
    # Using string 'patients.Patient' avoids circular imports
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE) 
    slot = models.CharField(max_length=3, choices=SLOT_CHOICES)
    assigned_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True) # Used to 'Sign Off'

    class Meta:
        # A nurse cannot be assigned to the same patient in the same slot twice
        unique_together = ('nurse', 'patient', 'slot', 'assigned_date')
    
    
    

# # users/views.py logic
# def sign_off_nurse(request, nurse_id):
#     nurse = Nurse.objects.get(id=nurse_id)
    
#     # 1. Reset the load meter
#     nurse.num_of_patients = 0
    
#     # 2. Flip the master switch to Off
#     nurse.is_on_duty = False
    
#     nurse.save()
    
# Now, when a Senior Nurse wants to assign a new patient, your dropdown or list should only show nurses who satisfy your "Lead Architect" constraints:

# Python
# # Get only nurses who are actually here AND have space
# available_nurses = Nurse.objects.filter(
#     is_on_duty=True, 
#     num_of_patients__lt=3  # __lt means "less than"
# )