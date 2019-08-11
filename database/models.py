from django.db import models

# Create a table
class Courses(models.Model):
    #courses_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='课程名')
    courses_name = models.CharField(max_length=100, blank=False)
    courses_summary = models.CharField(max_length=10000, blank=False)
    courses_teacher = models.CharField(max_length=100, blank=False)
    courses_method = models.CharField(max_length=100, blank=False)
    courses_characteristic = models.CharField(max_length=100, blank=True)
    courses_provide_lab = models.CharField(max_length=100, blank=False)
    courses_detail = models.CharField(max_length=10000, blank=False)



class Device(models.Model):
    name = models.CharField(max_length=50, blank=False)
    ip_address = models.GenericIPAddressField(blank=False, unique=True)
    ro_community = models.CharField(max_length=50, blank=False)
    rw_community = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password =models.CharField(max_length=50, blank=True, null=True)
    enable_password = models.CharField(max_length=50, blank=True, null=True)

    vendor_choice = (('Huawei', 'Huawei'), ('Cisco', 'Cisco'))
    vendor = models.CharField(max_length=10, choices=vendor_choice)

    device_type_choice = (('Firewall', 'Firewall'), ('Router', 'Router'), ('Switch', 'Switch'))
    device_type = models.CharField(max_length=10, choices=device_type_choice)

    create_date = models.DateField(auto_now_add=True)

