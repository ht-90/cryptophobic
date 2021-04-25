from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .coinboard.views import CoinView
from .coinboard.api.views import CoinList

urlpatterns = [
    path('admin/', admin.site.urls),
    # coinboard
    path('', CoinView.as_view(), name="coin"),
    # coinboard api
    path('coins/', CoinList.as_view(), name='get_all_coins'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
