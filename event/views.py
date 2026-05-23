from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Blessing
from .serializers import BlessingSerializer

class BlessingViewSet(ModelViewSet):
    queryset = Blessing.objects.all()
    serializer_class = BlessingSerializer
    permission_classes = [AllowAny]  # 🔥 allows React POST without login