from django.test import TestCase, Client

from ...models import Coin


class TestCoinList(TestCase):
    """Test CoinList API view"""
    def setUp(self):
        """Create a test coin object"""
        self.test_coin = Coin.objects.create(
            name="TestCoin",
            ticker="TSTC",
            address="xxxxx00000",
        )

    def test_coin_list_api_get(self):
        """Ensure API get request returns expected data"""
        c = Client()
        response = c.get("/coins/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["name"], "TestCoin")
        self.assertEqual(response.data[0]["ticker"], "TSTC")
        self.assertEqual(response.data[0]["address"], "xxxxx00000")

    def test_coin_list_api_post(self):
        """Ensure API post request returns 404"""
        c = Client()
        response = c.post("/coin/", {"name": "test"})
        self.assertEqual(response.status_code, 404)
