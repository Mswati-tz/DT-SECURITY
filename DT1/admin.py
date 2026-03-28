from django.contrib import admin
from . import models

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_name',)
admin.site.register(models.Department, DepartmentAdmin)

class DirectorsAdmin(admin.ModelAdmin):
    list_display=('full_name',)
admin.site.register(models.Directors, DirectorsAdmin)

class SupervisorAdmin(admin.ModelAdmin):
    list_display=('full_name',)
admin.site.register(models.Supervisor, SupervisorAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display=('site_name',)
admin.site.register(models.ClientSite, ClientAdmin)

class AskariAdmin(admin.ModelAdmin):
    list_display=('full_name',)
admin.site.register(models.Askari, AskariAdmin)

class EquipmentAdmin(admin.ModelAdmin):
    list_display=('equipment_name',)
admin.site.register(models.Equipment, EquipmentAdmin)

class AssignedAdmin(admin.ModelAdmin):
    list_display=('assigned_by',)
admin.site.register(models.EquipmentAssigned, AssignedAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display=('title',)
admin.site.register(models.Report, ReportAdmin)

class UpdateAdmin(admin.ModelAdmin):
    #list_editable=('title','heading')
    list_per_page= 5
    list_display=('title','heading','file','date_registered')
admin.site.register(models.Update, UpdateAdmin)

class ServiceAdmin(admin.ModelAdmin):
    #list_editable=('title','heading')
    list_per_page= 5
    list_display=('title','image')
admin.site.register(models.Service, ServiceAdmin)




class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent','message') # Inaonyesha hivi vitu kwenye list
    readonly_fields = ('name', 'email', 'subject', 'message', 'date_sent') # Inazuia usiedit ujumbe wa mteja
    search_fields = ('name', 'email', 'subject')
admin.site.register(models.ContactMessage, ContactMessageAdmin)