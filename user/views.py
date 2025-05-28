from main.utils.generic_api import GenericView  
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer
from .models import User

class UserView(GenericView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ["update"]
    
    def pre_update(self, request, instance):
        request.data['id'] = self.request.user.id
        
    def get_object(self, pk):
        return self.queryset.get(pk=pk)

class ManageUserView(GenericView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ["list", "retrieve", "update", "destroy"]
