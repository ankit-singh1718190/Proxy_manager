from django.contrib import admin
from .models import ProxyNode, ProxyLog
@admin.register(ProxyNode)
class ProxyNodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'port', 'status', 'created_at')
    search_fields = ('ip_address', 'user__username')
    list_filter = ('status',)

@admin.register(ProxyLog)
class ProxyLogAdmin(admin.ModelAdmin):
    list_display = ('proxy', 'timestamp', 'request_count')
    search_fields = ('proxy__ip_address',)
