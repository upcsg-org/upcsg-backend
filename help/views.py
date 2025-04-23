from main.utils.generic_api import GenericView
from .models import Concern
from .serializers import ConcernSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
class ConcernView(GenericView):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    allowed_methods = ["create"]
    
class TrackConcernView(GenericView):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ["list", "retrieve"]

class ManageConcernView(GenericView):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    permission_classes = [IsAdminUser]
