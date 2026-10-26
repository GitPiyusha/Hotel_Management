from django.test import TestCase

from .models import HotelModel


class HotelApiTests(TestCase):
    def test_get_lists_hotels_as_json(self):
        HotelModel.objects.create(name="Harbor", address="12 Coast Road", rating=5)

        response = self.client.get("/api/hotels/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [{"id": 1, "name": "Harbor", "address": "12 Coast Road", "rating": 5}],
        )

    def test_post_creates_hotel(self):
        response = self.client.post(
            "/api/hotels/",
            {"name": "Harbor", "address": "12 Coast Road", "rating": 5},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(HotelModel.objects.count(), 1)
        self.assertEqual(response.json()["name"], "Harbor")
