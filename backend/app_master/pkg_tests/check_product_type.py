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

from app_master.pkg_models.check_language import LANGUAGE
from app_master.pkg_models.master_text import TEXT
from app_master.pkg_views.check_product_type import (
    Product_Type,
    PRODUCT_TYPE_T,
)
from app_master.pkg_models.check_product_type import (
    PRODUCT_TYPE,
    PRODUCT_TYPE_T,
)


# ========================================================================
class Product_TypeModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.product_type = PRODUCT_TYPE.objects.create(
            name="test",
        )

    def test_product_type_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.product_type.name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_product_type_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(
            self.product_type.company_code, self.product_type.name
        )
        self.assertEqual(str(self.product_type), expected_result)

    def test_product_type_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            PRODUCT_TYPE.objects.create(
                name="test",
            )  # Try to create another file type with the same name


class Product_TypeViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CITY
        self.product_type = PRODUCT_TYPE.objects.create(
            name="test",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_product_type_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_Product_Type", kwargs={"pk": 0}))
        view = Product_Type.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_type_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Check_Product_Type", kwargs={"pk": self.product_type.id})
        )
        view = Product_Type.as_view()
        response = view(request, pk=self.product_type.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_product_type(self):
        # Test POST request for creating a new file type
        data = {
            "name": "test1",
        }
        request = self.factory.post(
            reverse("Check_Product_Type", kwargs={"pk": 0}), data=data
        )
        view = Product_Type.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_product_type(self):
        # Test PUT request for updating an existing file type
        data = {
            "name": "test2",
        }
        request = self.factory.put(
            reverse("Check_Product_Type", kwargs={"pk": self.product_type.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Product_Type.as_view()
        response = view(request, pk=self.product_type.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_product_type(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_Product_Type", kwargs={"pk": self.product_type.id})
        )
        view = Product_Type.as_view()
        response = view(request, pk=self.product_type.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class Product_Type_TModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.product_type = PRODUCT_TYPE.objects.create(
            name="test",
        )
        self.language = LANGUAGE.objects.create(
            eng_name="test",
            local_name="test",
        )
        self.text = TEXT.objects.create(
            text="test " * 100,
        )
        self.product_type_t = PRODUCT_TYPE_T.objects.create(
            type=self.product_type,
            lang=self.language,
            text=self.text,
        )

    def test_product_type_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {} - {}".format(
            self.product_type_t.company_code,
            self.product_type_t.type.name,
            self.product_type_t.lang.eng_name,
        )
        self.assertEqual(str(self.product_type_t), expected_result)

    def test_product_type_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            PRODUCT_TYPE_T.objects.create(
                type=self.product_type,
                lang=self.language,
                text=self.text,
            )  # Try to create another file type with the same name


class Product_Type_TViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CITY
        self.product_type = PRODUCT_TYPE.objects.create(
            name="test",
        )
        self.language = LANGUAGE.objects.create(
            eng_name="test",
            local_name="test",
        )
        self.text = TEXT.objects.create(
            text="test " * 100,
        )
        self.product_type_t = PRODUCT_TYPE_T.objects.create(
            type=self.product_type,
            lang=self.language,
            text=self.text,
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_product_type_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_Product_Type_T", kwargs={"pk": 0}))
        view = Product_Type.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_type_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Check_Product_Type_T", kwargs={"pk": self.product_type.id})
        )
        view = Product_Type.as_view()
        response = view(request, pk=self.product_type.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_product_type(self):
        # Test POST request for creating a new file type
        product_type = PRODUCT_TYPE.objects.create(
            name="test1",
        )
        language = LANGUAGE.objects.create(
            eng_name="test1",
            local_name="test1",
        )
        text = TEXT.objects.create(
            text="test1 " * 100,
        )
        data = {
            "type": product_type.id,
            "lang": language.id,
            "text": text.id,
        }
        request = self.factory.post(
            reverse("Check_Product_Type_T", kwargs={"pk": 0}), data=data
        )
        view = Product_Type.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_product_type(self):
        # Test PUT request for updating an existing file type
        product_type = PRODUCT_TYPE.objects.create(
            name="test2",
        )
        language = LANGUAGE.objects.create(
            eng_name="test2",
            local_name="test2",
        )
        text = TEXT.objects.create(
            text="test2 " * 100,
        )
        data = {
            "type": product_type.id,
            "lang": language.id,
            "text": text.id,
        }
        request = self.factory.put(
            reverse("Check_Product_Type_T", kwargs={"pk": self.product_type.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Product_Type.as_view()
        response = view(request, pk=self.product_type.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_product_type(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_Product_Type_T", kwargs={"pk": self.product_type.id})
        )
        view = Product_Type.as_view()
        response = view(request, pk=self.product_type.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
