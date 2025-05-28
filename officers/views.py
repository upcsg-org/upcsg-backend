from main.utils.generic_api import GenericView
from .models import Term, Officer
from .serializers import TermSerializer, OfficerSerializer

# ========== Term ==========
class TermView(GenericView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    allowed_methods = ["list", "retrieve"]

class ManageTermView(GenericView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    allowed_methods = ["create", "update", "destroy"]

# ========== Officer ==========
class OfficerView(GenericView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    allowed_methods = ["list", "retrieve"]

class ManageOfficerView(GenericView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    allowed_methods = ["create", "update", "destroy"]
