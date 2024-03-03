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

from app_master.pkg_views.check_currency import Currency
from app_master.pkg_models.check_currency import CURRENCY


# ========================================================================
class CurrencyModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.currency = CURRENCY.objects.create(
            code="tst",
            eng_name="test",
            local_name="test",
            symbol="t",
        )

    def test_currency_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.currency.eng_name, "test".upper()
        )  # Check if the name is uppercased as expected
        self.assertEqual(
            self.currency.code, "tst".upper()
        )  # Check if the name is uppercased as expected

    def test_currency_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {} - {}".format(
            self.currency.company_code, self.currency.code, self.currency.eng_name
        )
        self.assertEqual(str(self.currency), expected_result)

    def test_currency_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            CURRENCY.objects.create(
                code="tst",
                eng_name="test",
                local_name="test",
                symbol="t",
            )  # Try to create another file type with the same name


class CurrencyViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CITY
        self.currency = CURRENCY.objects.create(
            code="tst",
            eng_name="test",
            local_name="test",
            symbol="t",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_currency_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_Currency", kwargs={"pk": 0}))
        view = Currency.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currency_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Check_Currency", kwargs={"pk": self.currency.id})
        )
        view = Currency.as_view()
        response = view(request, pk=self.currency.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_currency(self):
        # Test POST request for creating a new file type
        data = {
            "code": "tst2",
            "eng_name": "test2",
            "local_name": "test2",
            "symbol": "t2",
        }
        request = self.factory.post(
            reverse("Check_Currency", kwargs={"pk": 0}), data=data
        )
        view = Currency.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_currency(self):
        # Test PUT request for updating an existing file type
        data = {
            "code": "tst3",
            "eng_name": "test3",
            "local_name": "test3",
            "symbol": "t3",
        }
        request = self.factory.put(
            reverse("Check_Currency", kwargs={"pk": self.currency.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Currency.as_view()
        response = view(request, pk=self.currency.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_currency(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_Currency", kwargs={"pk": self.currency.id})
        )
        view = Currency.as_view()
        response = view(request, pk=self.currency.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
