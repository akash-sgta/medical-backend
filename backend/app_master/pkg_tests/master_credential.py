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

from app_master.pkg_views.master_credential import Credential
from app_master.pkg_models.master_credential import CREDENTIAL


# ========================================================================
class CredentialModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.credential = CREDENTIAL.objects.create(
            email="email@email.com",
            pwd="sha256_password",
            is_admin=True,
            is_internal_user=True,
            is_external_user=True,
        )

    def test_credential_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.credential.email, "email@email.com".upper()
        )  # Check if the name is uppercased as expected

    def test_credential_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {}".format(
            self.credential.company_code, self.credential.email
        )
        self.assertEqual(str(self.credential), expected_result)

    def test_credential_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            CREDENTIAL.objects.create(
                email="email@email.com",
                pwd="sha256_password",
                is_admin=True,
                is_internal_user=True,
                is_external_user=True,
            )  # Try to create another file type with the same name


class CredentialViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CREDENTIAL
        self.credential = CREDENTIAL.objects.create(
            email="email@email.com",
            pwd="sha256_password",
            is_admin=True,
            is_internal_user=True,
            is_external_user=True,
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_credential_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Master_Credential", kwargs={"pk": 0}))
        view = Credential.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_credential_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Master_Credential", kwargs={"pk": self.credential.id})
        )
        view = Credential.as_view()
        response = view(request, pk=self.credential.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_credential(self):
        # Test POST request for creating a new file type
        data = {
            "email": "email1@email.com",
            "pwd": "sha256_password",
            "is_admin": True,
            "is_internal_user": True,
            "is_external_user": True,
        }
        request = self.factory.post(
            reverse("Master_Credential", kwargs={"pk": 0}), data=data
        )
        view = Credential.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_credential(self):
        # Test PUT request for updating an existing file type
        data = {
            "email": "email2@email.com",
            "pwd": "sha256_password",
            "is_admin": True,
            "is_internal_user": True,
            "is_external_user": True,
        }
        request = self.factory.put(
            reverse("Master_Credential", kwargs={"pk": self.credential.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Credential.as_view()
        response = view(request, pk=self.credential.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_credential(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Master_Credential", kwargs={"pk": self.credential.id})
        )
        view = Credential.as_view()
        response = view(request, pk=self.credential.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
