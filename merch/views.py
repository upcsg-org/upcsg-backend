from main.utils.generic_api import GenericView
from .models import Merch, MerchVariant, Bundle
from .serializers import MerchSerializer, MerchVariantSerializer, BundleSerializer

class MerchView(GenericView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    allowed_methods = ["list", "retrieve"]
class ManageMerchView(GenericView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    allowed_methods = ["create", "update", "delete"]

class MerchVariantView(GenericView):
    queryset = MerchVariant.objects.all()
    serializer_class = MerchVariantSerializer
    allowed_methods = ["list", "retrieve"]
    
class ManageMerchVariantView(GenericView):
    queryset = MerchVariant.objects.all()
    serializer_class = MerchVariantSerializer
    allowed_methods = ["create", "update", "delete"]

class BundleView(GenericView):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
    allowed_methods = ["list", "retrieve"]
    
class ManageBundleView(GenericView):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
    allowed_methods = ["create", "update", "delete"]
