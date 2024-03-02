# ========================================================================
# Generated using : https://chat.openai.com/
# ========================================================================
import json

from django.test import (
    TestCase,
    RequestFactory,
)
from rest_framework import status
from django.urls import reverse

from app_master.pkg_views.check_city import City
from app_master.pkg_models.check_city import CITY
from app_master.pkg_models.check_state import STATE
from app_master.pkg_models.check_country import COUNTRY
from app_master.pkg_models.check_continent import CONTINENT


# ========================================================================
class CityModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.continent = CONTINENT.objects.create()
        self.city = CITY.objects.create(
            name="test",
        )

    def test_city_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.city.name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_city_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(self.city.company_code, self.city.name)
        self.assertEqual(str(self.city), expected_result)

    def test_city_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            CITY.objects.create(
                name="test"
            )  # Try to create another file type with the same name


class CityViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CITY
        self.city = CITY.objects.create(name="TEST_00")

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_city_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_City", kwargs={"pk": 0}))
        view = City.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_city_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(reverse("Check_City", kwargs={"pk": self.city.id}))
        view = City.as_view()
        response = view(request, pk=self.city.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_city(self):
        # Test POST request for creating a new file type
        data = {
            "name": "TEST_01",
        }
        request = self.factory.post(reverse("Check_City", kwargs={"pk": 0}), data=data)
        view = City.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_city(self):
        # Test PUT request for updating an existing file type
        data = {
            "name": "TEST_02",
        }
        request = self.factory.put(
            reverse("Check_City", kwargs={"pk": self.city.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = City.as_view()
        response = view(request, pk=self.city.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_city(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_City", kwargs={"pk": self.city.id})
        )
        view = City.as_view()
        response = view(request, pk=self.city.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
