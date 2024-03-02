# ========================================================================
# Generated using : https://chat.openai.com/
# ========================================================================
from django.test import (
    TestCase,
    RequestFactory,
)
from rest_framework import status
from django.urls import reverse

from app_cdn.pkg_views.check_file_type import File_Type
from app_cdn.pkg_models.check_file_type import FILE_TYPE


# ========================================================================
class FileTypeModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.file_type = FILE_TYPE.objects.create(
            name="test",
        )

    def test_file_type_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.file_type.name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_file_type_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(
            self.file_type.company_code, self.file_type.name
        )
        self.assertEqual(str(self.file_type), expected_result)

    def test_file_type_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            FILE_TYPE.objects.create(
                name="test"
            )  # Try to create another file type with the same name


class File_TypeViewTestCase(TestCase):
    def setUp(self):
        # Create test data for FILE_TYPE
        self.file_type = FILE_TYPE.objects.create(name="TEST_00")

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_file_type_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_File_Type", kwargs={"pk": 0}))
        view = File_Type.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_type_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Check_File_Type", kwargs={"pk": self.file_type.id})
        )
        view = File_Type.as_view()
        response = view(request, pk=self.file_type.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_file_type(self):
        # Test POST request for creating a new file type
        data = {
            "name": "TEST_01",
        }
        request = self.factory.post(
            reverse("Check_File_Type", kwargs={"pk": 0}), data=data
        )
        view = File_Type.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_file_type(self):
        # Test PUT request for updating an existing file type
        data = {
            "name": "TEST_02",
        }
        request = self.factory.put(
            reverse("Check_File_Type", kwargs={"pk": self.file_type.id}),
            data=data,
            headers={"Content-Type": "application/json"},
        )
        view = File_Type.as_view()
        response = view(request, pk=self.file_type.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_file_type(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_File_Type", kwargs={"pk": self.file_type.id})
        )
        view = File_Type.as_view()
        response = view(request, pk=self.file_type.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
