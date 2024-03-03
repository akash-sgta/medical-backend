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

from app_master.pkg_views.check_language import Language
from app_master.pkg_models.check_language import LANGUAGE


# ========================================================================
class LanguageModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.language = LANGUAGE.objects.create(
            eng_name="test",
            local_name="test",
        )

    def test_language_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.language.eng_name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_language_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(
            self.language.company_code, self.language.eng_name
        )
        self.assertEqual(str(self.language), expected_result)

    def test_language_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            LANGUAGE.objects.create(
                eng_name="test",
                local_name="test",
            )  # Try to create another file type with the same name


class LanguageViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CITY
        self.language = LANGUAGE.objects.create(
            eng_name="test",
            local_name="test",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_language_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_Language", kwargs={"pk": 0}))
        view = Language.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_language_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Check_Language", kwargs={"pk": self.language.id})
        )
        view = Language.as_view()
        response = view(request, pk=self.language.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_language(self):
        # Test POST request for creating a new file type
        data = {
            "eng_name": "test1",
            "local_name": "test1",
        }
        request = self.factory.post(
            reverse("Check_Language", kwargs={"pk": 0}), data=data
        )
        view = Language.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_language(self):
        # Test PUT request for updating an existing file type
        data = {
            "eng_name": "test2",
            "local_name": "test2",
        }
        request = self.factory.put(
            reverse("Check_Language", kwargs={"pk": self.language.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Language.as_view()
        response = view(request, pk=self.language.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_language(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_Language", kwargs={"pk": self.language.id})
        )
        view = Language.as_view()
        response = view(request, pk=self.language.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
