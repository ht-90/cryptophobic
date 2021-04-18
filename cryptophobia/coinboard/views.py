from rest_framework import generics

from .models import Coin
from .serializers import CoinSerializer


class CoinList(generics.ListCreateAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


# Create your views here.
