from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

#create models (database)

class Department(models.Model):
    department_name=models.CharField(max_length=100, unique=True)
    department_description=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.department_name
    
class Directors(models.Model):
    
    class ROLES(models.TextChoices):
        Default = "Roles"
        Operator = "Operator"
        Management = "Management"
        
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    role=models.CharField(choices=ROLES.choices, max_length=15)
    
  
    
    #TUNATOFAUTISHA DIRCTORS
    OFFICE_CHOICES=[
        ('ARUSHA','ARUSHA BRANCH OFFICE'),
        ('DAR','DAR ES SALAAM HEAD OFFICE')
    ]
    
    office_location=models.CharField(choices=OFFICE_CHOICES, max_length=15)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.full_name}-{self.phone_number}"
    
class Supervisor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    director_in_charge=models.ForeignKey(Directors, on_delete=models.SET_NULL,null=True, related_name='supervisors')
    
    def __str__(self):
        return f"{self.full_name}"
    
class ClientSite(models.Model):
    site_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    contact_person=models.CharField(max_length=100)
    contact_phone=models.CharField(max_length=100)
    
    def __str__(self):
        return self.site_name
    
class Askari(models.Model):
    full_name=models.CharField(max_length=100)  
    badge_number = models.CharField(max_length=15, blank=True, null=True)
    phone_number=models.CharField(max_length=100) 
    supervisor=models.ForeignKey(Supervisor, on_delete=models.PROTECT, related_name='guards')
    current_site=models.ForeignKey(ClientSite, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.full_name}"
    
class Equipment(models.Model):
    STATUS_CHOICES=[
        ('AVAILABLE','AVAILABLE'),
        ('ASSIGNED','ASSIGNED'),
        ('UN AVAILABLE','AVAILABLE'),
        ('DEMAGED','DEMAGED'),
        ('MAINTAINANCE','MAINTAINANCE'),
    ]
    
    equipment_name=models.CharField(max_length=100)
    category=models.CharField(max_length=10, help_text='example: uniform, silaha')
    status=models.CharField(max_length=15, choices=STATUS_CHOICES, default='Available')
    
    def __str__(self):
        return f"{self.equipment_name}"
    
class EquipmentAssigned(models.Model):
    askari=models.ForeignKey(Askari, on_delete=models.CASCADE)
    vifaa=models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_by=models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    date_issue=models.DateTimeField(auto_now_add=True)
    date_returned=models.DateTimeField(null=True, blank=True)
    condition=models.TextField()
    
    def __str__(self):
        return f"{self.askari.full_name}"
    
class Report(models.Model):
    site=models.ForeignKey(ClientSite, on_delete=models.CASCADE)
    reported_by=models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    time_stamp=models.DateTimeField(auto_now_add=True)
    action_taken=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Update(models.Model):
    title=models.CharField(max_length=10)
    heading=models.CharField(max_length=50)
    file=models.FileField(upload_to=('updates/'))
    date_registered=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}">')
    
    
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"