from main.utils.generic_api import GenericView
from .models import Merch, MerchVariant, Bundle, MerchType, MerchSize
from .serializers import (
    MerchSerializer,
    MerchVariantSerializer,
    BundleSerializer,
    MerchTypeSerializer,
    MerchSizeSerializer
)

# ========== MerchType ==========
class MerchTypeView(GenericView):
    queryset = MerchType.objects.all()
    serializer_class = MerchTypeSerializer
    allowed_methods = ["list", "retrieve"]

class ManageMerchTypeView(GenericView):
    queryset = MerchType.objects.all()
    serializer_class = MerchTypeSerializer
    allowed_methods = ["create", "update", "destroy"]

# ========== MerchSize ==========
class MerchSizeView(GenericView):
    queryset = MerchSize.objects.all()
    serializer_class = MerchSizeSerializer
    allowed_methods = ["list", "retrieve"]

class ManageMerchSizeView(GenericView):
    queryset = MerchSize.objects.all()
    serializer_class = MerchSizeSerializer
    allowed_methods = ["create", "update", "destroy"]

# ========== Merch ==========
class MerchView(GenericView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    allowed_methods = ["list", "retrieve"]

class ManageMerchView(GenericView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    allowed_methods = ["create", "update", "destroy"]

# ========== MerchVariant ==========
class MerchVariantView(GenericView):
    queryset = MerchVariant.objects.all()
    serializer_class = MerchVariantSerializer
    allowed_methods = ["list", "retrieve"]

class ManageMerchVariantView(GenericView):
    queryset = MerchVariant.objects.all()
    serializer_class = MerchVariantSerializer
    allowed_methods = ["create", "update", "destroy"]

# ========== Bundle ==========
class BundleView(GenericView):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
    allowed_methods = ["list", "retrieve"]

class ManageBundleView(GenericView):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
    allowed_methods = ["create", "update", "destroy"]
