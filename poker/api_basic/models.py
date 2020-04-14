from django.db import models

# Create your models here.
class Server(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=50,default='')
    kernal = models.CharField(max_length=50,default='')
    time = models.CharField(max_length=50,default='')
    os = models.CharField(max_length=50,default='')
    os_arch = models.CharField(max_length=50,default='')
    cpu_model = models.CharField(max_length=50,default='')
    cpu_core = models.CharField(max_length=50,default='')
    cpu_speed = models.CharField(max_length=50, default='')
    cpu_load_1 = models.CharField(max_length=50, default='')
    cpu_load_2 = models.CharField(max_length=50, default='')
    cpu_load_3 = models.CharField(max_length=50, default='')
    ram_total = models.CharField(max_length=50, default='')
    ram_usage = models.CharField(max_length=50, default='')
    ram_free = models.CharField(max_length=50, default='')
    ram_caches = models.CharField(max_length=50, default='')
    ram_buffer = models.CharField(max_length=50, default='')
    swap_total = models.CharField(max_length=50, default='')
    swap_free = models.CharField(max_length=50, default='')
    swap_usage = models.CharField(max_length=50, default='')
    file_descriptors_1 = models.CharField(max_length=500, default='')
    file_descriptors_2 = models.CharField(max_length=500, default='')
    file_descriptors_3 = models.CharField(max_length=500, default='')
    ssh_sessions = models.CharField(max_length=500, default='')
    uptime = models.CharField(max_length=500, default='')
    default_interface = models.CharField(max_length=500, default='')
    active_connections = models.CharField(max_length=500, default='')
    ping_latency = models.CharField(max_length=500, default='')
    ipv4_addresses = models.CharField(max_length=500, default='')
    ipv6_addresses = models.CharField(max_length=500, default='')
    all_interfaces_current = models.CharField(max_length=500, default='')
    all_interfaces = models.CharField(max_length=500, default='')
    disks = models.CharField(max_length=500, default='')
    disks_inodes = models.CharField(max_length=500, default='')
    cpu_info = models.CharField(max_length=500, default='')
    cpu_info_current = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.hostname

