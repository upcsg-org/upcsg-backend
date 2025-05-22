from django.contrib import admin
from .models import Merch, MerchType, MerchSize, MerchVariant, Bundle

admin.site.register(Merch)
admin.site.register(MerchType)
admin.site.register(MerchSize)
admin.site.register(MerchVariant)
admin.site.register(Bundle)


