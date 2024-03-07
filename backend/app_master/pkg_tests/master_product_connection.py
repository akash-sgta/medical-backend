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

from app_cdn.pkg_models.check_file_type import FILE_TYPE
from app_cdn.pkg_models.master_file import FILE
from app_master.pkg_models.check_currency import CURRENCY
from app_master.pkg_models.check_unit import UNIT
from app_master.pkg_models.check_unit_of_measurement import UOM
from app_master.pkg_models.master_text import TEXT
from app_master.pkg_views.master_product_connection import Product_Connection
from app_master.pkg_models.master_product import PRODUCT
from app_master.pkg_models.check_product_type import PRODUCT_TYPE
from app_master.pkg_models.master_product_connection import (
    PRODUCT_CONNECTION,
)


# ========================================================================
class Product_ConnectionModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.unit = UNIT.objects.create(
            name="test",
        )
        self.uom = UOM.objects.create(
            unit=self.unit,
            name="test",
        )
        self.product_type = PRODUCT_TYPE.objects.create(
            name="test",
        )
        self.text = TEXT.objects.create(
            text="test" * 1000,
        )
        self.file_type = FILE_TYPE.objects.create(
            name="test",
        )
        self.file = FILE.objects.create(
            type=self.file_type,
            name="test",
            size=1000.11,
            url="https://www.ungabunga.com",
        )
        self.currency = CURRENCY.objects.create(
            code="tst",
            eng_name="test",
            local_name="test",
            symbol="t",
        )
        self.product = PRODUCT.objects.create(
            type=self.product_type,
            image_01=self.file,
            image_02=self.file,
            image_03=self.file,
            currency=self.currency,
            description=self.text,
            storage_instructions=self.text,
            side_effects=self.text,
            warnings_precautions=self.text,
            contraindications=self.text,
            name="test",
            manufacturer="test",
            dosage="test",
            price=1.1,
            url="https://www.ungabunga.com",
            is_prescription_required=True,
        )
        self.product_connection = PRODUCT_CONNECTION.objects.create(
            parent=self.product,
            parent_uom=self.uom,
            child=self.product,
            child_uom=self.uom,
            parent_quantity=1,
            child_quantity=1,
        )

    # def test_product_connection_creation(self):
    #     # Test if the file type object was created successfully
    #     self.assertEqual(
    #         self.product.name, "test".upper()
    #     )  # Check if the name is uppercased as expected

    def test_product_connection_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {} - {}".format(
            self.product_connection.company_code,
            self.product_connection.parent.name,
            self.product_connection.child.name,
        )
        self.assertEqual(str(self.product_connection), expected_result)

    def test_product_connection_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            PRODUCT_CONNECTION.objects.create(
                parent=self.product,
                parent_uom=self.uom,
                child=self.product,
                child_uom=self.uom,
                parent_quantity=1,
                child_quantity=1,
            )  # Try to create another file type with the same name


class Product_ConnectionViewTestCase(TestCase):
    def setUp(self):
        # Create test data for PRODUCT
        self.unit = UNIT.objects.create(
            name="test",
        )
        self.uom = UOM.objects.create(
            unit=self.unit,
            name="test",
        )
        self.product_type = PRODUCT_TYPE.objects.create(
            name="test",
        )
        self.text = TEXT.objects.create(
            text="test" * 1000,
        )
        self.file_type = FILE_TYPE.objects.create(
            name="test",
        )
        self.file = FILE.objects.create(
            type=self.file_type,
            name="test",
            size=1000.11,
            url="https://www.ungabunga.com",
        )
        self.currency = CURRENCY.objects.create(
            code="tst",
            eng_name="test",
            local_name="test",
            symbol="t",
        )
        self.product = PRODUCT.objects.create(
            type=self.product_type,
            image_01=self.file,
            image_02=self.file,
            image_03=self.file,
            currency=self.currency,
            description=self.text,
            storage_instructions=self.text,
            side_effects=self.text,
            warnings_precautions=self.text,
            contraindications=self.text,
            name="test",
            manufacturer="test",
            dosage="test",
            price=1.1,
            url="https://www.ungabunga.com",
            is_prescription_required=True,
        )
        self.product_connection = PRODUCT_CONNECTION.objects.create(
            parent=self.product,
            parent_uom=self.uom,
            child=self.product,
            child_uom=self.uom,
            parent_quantity=1,
            child_quantity=1,
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_product_connection_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Master_Product", kwargs={"pk": 0}))
        view = Product_Connection.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_connection_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Master_Product", kwargs={"pk": self.product.id})
        )
        view = Product_Connection.as_view()
        response = view(request, pk=self.product.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_product(self):
        # Test POST request for creating a new file type
        data = {
            "parent": PRODUCT.objects.create(
                type=self.product_type,
                image_01=self.file,
                image_02=self.file,
                image_03=self.file,
                currency=self.currency,
                description=self.text,
                storage_instructions=self.text,
                side_effects=self.text,
                warnings_precautions=self.text,
                contraindications=self.text,
                name="test1",
                manufacturer="test",
                dosage="test",
                price=1.1,
                url="https://www.ungabunga.com",
                is_prescription_required=True,
            ).id,
            "parent_uom": self.uom.id,
            "child": self.product.id,
            "child_uom": self.uom.id,
            "parent_quantity": 1,
            "child_quantity": 1,
        }
        request = self.factory.post(
            reverse("Master_Product", kwargs={"pk": 0}), data=data
        )
        view = Product_Connection.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_product(self):
        # Test PUT request for updating an existing file type
        data = {
            "parent": self.product.id,
            "parent_uom": self.uom.id,
            "child": PRODUCT.objects.create(
                type=self.product_type,
                image_01=self.file,
                image_02=self.file,
                image_03=self.file,
                currency=self.currency,
                description=self.text,
                storage_instructions=self.text,
                side_effects=self.text,
                warnings_precautions=self.text,
                contraindications=self.text,
                name="test2",
                manufacturer="test",
                dosage="test",
                price=1.1,
                url="https://www.ungabunga.com",
                is_prescription_required=True,
            ).id,
            "child_uom": self.uom.id,
            "parent_quantity": 1,
            "child_quantity": 1,
        }
        request = self.factory.put(
            reverse("Master_Product", kwargs={"pk": self.product.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Product_Connection.as_view()
        response = view(request, pk=self.product.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_product(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Master_Product", kwargs={"pk": self.product.id})
        )
        view = Product_Connection.as_view()
        response = view(request, pk=self.product.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
