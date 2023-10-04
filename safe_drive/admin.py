from django.contrib import admin

from .models import CAR, DRIVER, HIRING, PAYMENT

class CARAdmin(admin.ModelAdmin):
    list_display = ("Plate_number", "Make", "Model", "Capacity", "Transmission", "Price_per_day", "Status", "Driver")

class DRIVERAdmin(admin.ModelAdmin):
    list_display = ("Name", "Gender", "License_number", "Contact", "Address")

class HIRINGAdmin(admin.ModelAdmin):
    list_display = ("Hire_date", "Customer", "Car", "Service_type", "Number_of_days", "Amount_paid")

class PAYMENTAdmin(admin.ModelAdmin):
    list_display = ("Payment_date", "Hire", "Amount_paid")





admin.site.register(CAR, CARAdmin)
admin.site.register(DRIVER, DRIVERAdmin)
admin.site.register(HIRING, HIRINGAdmin)
admin.site.register(PAYMENT, PAYMENTAdmin)