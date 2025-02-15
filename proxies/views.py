from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import ProxyNode
from .serializers import ProxyNodeSerializer


class ProxyNodeViewSet(viewsets.ModelViewSet):
    queryset = ProxyNode.objects.all()
    serializer_class = ProxyNodeSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return ProxyNode.objects.filter(status='active')

@api_view(['POST'])
@permission_classes([AllowAny])
def register_proxy(request):
    user = request.user
    data = request.data
    
    proxy, created = ProxyNode.objects.get_or_create(
        user=user,
        ip_address=data.get('ip_address'),
        port=data.get('port'),
        location=data.get('location', ''),
        status='active'
    )
    return Response({'message': 'Proxy registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_available_proxies(request):
    proxies = ProxyNode.objects.filter(status='active')
    serializer = ProxyNodeSerializer(proxies, many=True)
    return Response(serializer.data)