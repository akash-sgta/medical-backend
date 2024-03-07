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

from app_master.pkg_views.master_text import Text
from app_master.pkg_models.master_text import TEXT


# ========================================================================
class TextModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.text = TEXT.objects.create(
            text="test" * 10000,
        )

    # def test_text_creation(self):
    #     # Test if the file type object was created successfully
    #     self.assertEqual(
    #         self.text.name, "test".upper()
    #     )  # Check if the name is uppercased as expected

    def test_text_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}...".format(
            self.text.company_code, self.text.text[:8]
        )
        self.assertEqual(str(self.text), expected_result)

    # def test_text_unique_constraint(self):
    #     # Test uniqueness constraint for name field
    #     with self.assertRaises(Exception):
    #         TEXT.objects.create(
    #             name="test",
    #         )  # Try to create another file type with the same name


class TextViewTestCase(TestCase):
    def setUp(self):
        # Create test data for TEXT
        self.text = TEXT.objects.create(
            text="test" * 10000,
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_text_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Master_Text", kwargs={"pk": 0}))
        view = Text.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_text_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(reverse("Master_Text", kwargs={"pk": self.text.id}))
        view = Text.as_view()
        response = view(request, pk=self.text.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_text(self):
        # Test POST request for creating a new file type
        data = {
            "text": "test1" * 100000,
        }
        request = self.factory.post(reverse("Master_Text", kwargs={"pk": 0}), data=data)
        view = Text.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_text(self):
        # Test PUT request for updating an existing file type
        data = {
            "text": "test1" * 100000,
        }
        request = self.factory.put(
            reverse("Master_Text", kwargs={"pk": self.text.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Text.as_view()
        response = view(request, pk=self.text.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_text(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Master_Text", kwargs={"pk": self.text.id})
        )
        view = Text.as_view()
        response = view(request, pk=self.text.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
