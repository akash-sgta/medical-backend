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

from app_master.pkg_views.master_address import Address
from app_master.pkg_models.check_continent import CONTINENT
from app_master.pkg_models.check_country import COUNTRY
from app_master.pkg_models.check_state import STATE
from app_master.pkg_models.check_city import CITY
from app_master.pkg_models.master_text import TEXT
from app_master.pkg_models.master_address import ADDRESS


# ========================================================================
class AddressModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.continent = CONTINENT.objects.create(
            eng_name="test",
            local_name="test",
        )
        self.country = COUNTRY.objects.create(
            continent=self.continent,
            eng_name="test",
            local_name="test",
        )
        self.state = STATE.objects.create(
            country=self.country,
            eng_name="test",
            local_name="test",
        )
        self.city = CITY.objects.create(
            state=self.state,
            eng_name="test",
            local_name="test",
        )
        self.text = TEXT.objects.create(
            text="test" * 1000,
        )
        self.address = ADDRESS.objects.create(
            city=self.city,
            additional_line=self.text,
            street="test",
            postal_code="1234567890",
            latitude=123.321,
            longitude=123.321,
        )

    # def test_address_creation(self):
    #     # Test if the file type object was created successfully
    #     self.assertEqual(
    #         self.address.eng_name, "test".upper()
    #     )  # Check if the name is uppercased as expected

    def test_address_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(self.address.company_code, self.address.id)
        self.assertEqual(str(self.address), expected_result)

    # def test_address_unique_constraint(self):
    #     # Test uniqueness constraint for name field
    #     with self.assertRaises(Exception):
    #         ADDRESS.objects.create(
    #             country=self.country,
    #             eng_name="test",
    #             local_name="test",
    #         )  # Try to create another file type with the same name


class AddressViewTestCase(TestCase):
    def setUp(self):
        # Create test data for ADDRESS
        self.continent = CONTINENT.objects.create(
            eng_name="test",
            local_name="test",
        )
        self.country = COUNTRY.objects.create(
            continent=self.continent,
            eng_name="test",
            local_name="test",
        )
        self.state = STATE.objects.create(
            country=self.country,
            eng_name="test",
            local_name="test",
        )
        self.city = CITY.objects.create(
            state=self.state,
            eng_name="test",
            local_name="test",
        )
        self.text = TEXT.objects.create(
            text="test" * 1000,
        )
        self.address = ADDRESS.objects.create(
            city=self.city,
            additional_line=self.text,
            street="test",
            postal_code="1234567890",
            latitude=123.321,
            longitude=123.321,
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_address_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Master_Address", kwargs={"pk": 0}))
        view = Address.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_address_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Master_Address", kwargs={"pk": self.address.id})
        )
        view = Address.as_view()
        response = view(request, pk=self.address.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_address(self):
        # Test POST request for creating a new file type
        data = {
            "city": self.city.id,
            "additional_line": self.text.id,
            "street": "test1",
            "postal_code": "12345678901",
            "latitude": 123.3211,
            "longitude": 123.3211,
        }
        request = self.factory.post(
            reverse("Master_Address", kwargs={"pk": 0}), data=data
        )
        view = Address.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_address(self):
        # Test PUT request for updating an existing file type
        data = {
            "city": self.city.id,
            "additional_line": self.text.id,
            "street": "test2",
            "postal_code": "12345678901",
            "latitude": 123.3211,
            "longitude": 123.3211,
        }
        request = self.factory.put(
            reverse("Master_Address", kwargs={"pk": self.address.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Address.as_view()
        response = view(request, pk=self.address.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_address(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Master_Address", kwargs={"pk": self.address.id})
        )
        view = Address.as_view()
        response = view(request, pk=self.address.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
