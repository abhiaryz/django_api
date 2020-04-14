from rest_framework import serializers
from . models import Server

class serverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['hostname','kernal','time','os','os_arch','cpu_model','cpu_core','cpu_speed','cpu_load_1','cpu_load_2','cpu_load_3','ram_total','ram_usage','ram_free','ram_caches','ram_buffer','swap_total','swap_free','swap_usage','file_descriptors_1','file_descriptors_2','file_descriptors_3','ssh_sessions','uptime','default_interface','active_connections','ping_latency','ipv4_addresses','ipv6_addresses','all_interfaces','all_interfaces_current','disks','disks_inodes','cpu_info','cpu_info_current' ]





