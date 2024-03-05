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

from app_master.pkg_views.check_unit import Unit
from app_master.pkg_models.check_unit import UNIT


# ========================================================================
class UnitModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.unit = UNIT.objects.create(
            name="test",
        )

    def test_unit_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.unit.name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_unit_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(self.unit.company_code, self.unit.name)
        self.assertEqual(str(self.unit), expected_result)

    def test_unit_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            UNIT.objects.create(
                name="test",
            )  # Try to create another file type with the same name


class UnitViewTestCase(TestCase):
    def setUp(self):
        # Create test data for UNIT
        self.unit = UNIT.objects.create(
            name="test",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_unit_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_Unit", kwargs={"pk": 0}))
        view = Unit.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unit_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(reverse("Check_Unit", kwargs={"pk": self.unit.id}))
        view = Unit.as_view()
        response = view(request, pk=self.unit.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_unit(self):
        # Test POST request for creating a new file type
        data = {
            "name": "test1",
        }
        request = self.factory.post(reverse("Check_Unit", kwargs={"pk": 0}), data=data)
        view = Unit.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_unit(self):
        # Test PUT request for updating an existing file type
        data = {
            "name": "test2",
        }
        request = self.factory.put(
            reverse("Check_Unit", kwargs={"pk": self.unit.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Unit.as_view()
        response = view(request, pk=self.unit.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_unit(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_Unit", kwargs={"pk": self.unit.id})
        )
        view = Unit.as_view()
        response = view(request, pk=self.unit.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
