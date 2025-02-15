from django.db import models
from django.contrib.auth.models import User

class ProxyNode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    port = models.IntegerField()
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address}:{self.port} ({self.status})"

class ProxyLog(models.Model):
    proxy = models.ForeignKey(ProxyNode, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Log for {self.proxy.ip_address} at {self.timestamp}"