# ========================================================================
import json

from django.test import (
    TestCase,
    RequestFactory,
)
from rest_framework import status
from django.urls import reverse

from app_cdn.pkg_views.master_file import File
from app_cdn.pkg_models.master_file import FILE, FILE_TYPE


# ========================================================================
class FileModelTestCase(TestCase):
    """
    Test case for the FILE model.
    """

    def setUp(self):
        """
        Set up test data.
        """
        # Create test data
        self.file_type = FILE_TYPE.objects.create(name="test")
        self.file = FILE.objects.create(
            type=self.file_type,
            name="test",
            size=100.2,
            url="https://1337x.to",
        )

    def test_file_creation(self):
        """
        Test if the file object was created successfully.
        """
        self.assertEqual(self.file.name, "test".upper())

    def test_file_str_method(self):
        """
        Test the __str__ method of the file model.
        """
        expected_result = "[{}] {} -> {}".format(
            self.file.company_code, str(self.file.type), self.file.name
        )
        self.assertEqual(str(self.file), expected_result)

    def test_file_unique_constraint(self):
        """
        Test uniqueness constraint for name field.
        """
        with self.assertRaises(Exception):
            FILE.objects.create(
                type=self.file_type,
                name="test",
            )


class FileViewTestCase(TestCase):
    """
    Test case for views related to FILE.
    """

    def setUp(self):
        """
        Set up test data for FILE and initialize the request factory.
        """
        # Create test data for FILE
        self.file_type = FILE_TYPE.objects.create(name="test")
        self.file = FILE.objects.create(
            type=self.file_type,
            name="test",
            size=100.2,
            url="https://1337x.to",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_file_list(self):
        """
        Test GET request for fetching list of files.
        """
        request = self.factory.get(reverse("Master_File", kwargs={"pk": 0}))
        view = File.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_detail(self):
        """
        Test GET request for fetching detail of a file.
        """
        request = self.factory.get(reverse("Master_File", kwargs={"pk": self.file.id}))
        view = File.as_view()
        response = view(request, pk=self.file.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_file(self):
        """
        Test POST request for creating a new file.
        """
        data = {
            "type": self.file_type.id,
            "name": "TEST_01",
            "size": 100.2,
            "url": "https://1337x.to",
        }
        request = self.factory.post(reverse("Master_File", kwargs={"pk": 0}), data=data)
        view = File.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_file(self):
        """
        Test PUT request for updating an existing file.
        """
        data = {
            "name": "TEST_02",
        }
        request = self.factory.put(
            reverse("Master_File", kwargs={"pk": self.file.id}),
            data=json.dumps(data),
            content_type="application/json",
        )
        view = File.as_view()
        response = view(request, pk=self.file.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_file(self):
        """
        Test DELETE request for deleting an existing file.
        """
        request = self.factory.delete(
            reverse("Master_File", kwargs={"pk": self.file.id})
        )
        view = File.as_view()
        response = view(request, pk=self.file.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
