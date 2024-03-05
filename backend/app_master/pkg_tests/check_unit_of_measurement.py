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

from app_master.pkg_views.check_unit_of_measurement import Uom
from app_master.pkg_models.check_unit import UNIT
from app_master.pkg_models.check_unit_of_measurement import UOM


# ========================================================================
class UomModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.unit = UNIT.objects.create(
            name="test",
        )
        self.uom = UOM.objects.create(
            unit=self.unit,
            name="test",
        )

    def test_uom_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.uom.name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_uom_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {} -> {}".format(
            self.uom.company_code, self.uom.unit, self.uom.name
        )
        self.assertEqual(str(self.uom), expected_result)

    def test_uom_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            UOM.objects.create(
                unit=self.unit,
                name="test",
            )  # Try to create another file type with the same name


class UomViewTestCase(TestCase):
    def setUp(self):
        # Create test data for UOM
        self.unit = UNIT.objects.create(
            name="test",
        )
        self.uom = UOM.objects.create(
            unit=self.unit,
            name="test",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_uom_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_Uom", kwargs={"pk": 0}))
        view = Uom.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_uom_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(reverse("Check_Uom", kwargs={"pk": self.uom.id}))
        view = Uom.as_view()
        response = view(request, pk=self.uom.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_uom(self):
        # Test POST request for creating a new file type
        data = {
            "unit": self.unit.id,
            "name": "test1",
        }
        request = self.factory.post(reverse("Check_Uom", kwargs={"pk": 0}), data=data)
        view = Uom.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_uom(self):
        # Test PUT request for updating an existing file type
        data = {
            "unit": self.unit.id,
            "name": "test2",
        }
        request = self.factory.put(
            reverse("Check_Uom", kwargs={"pk": self.uom.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Uom.as_view()
        response = view(request, pk=self.uom.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_uom(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(reverse("Check_Uom", kwargs={"pk": self.uom.id}))
        view = Uom.as_view()
        response = view(request, pk=self.uom.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
