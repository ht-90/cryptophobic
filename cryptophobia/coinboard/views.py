from django.views.generic import ListView

from .models import Coin


class CoinView(ListView):
    template_name = "coin_list.html"
    model = Coin
