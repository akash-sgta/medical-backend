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

from app_master.pkg_views.master_profile import Profile
from app_master.pkg_models.master_profile import PROFILE
from app_master.pkg_models.master_credential import CREDENTIAL
from app_master.pkg_models.check_continent import CONTINENT
from app_master.pkg_models.check_country import COUNTRY
from app_master.pkg_models.check_state import STATE
from app_master.pkg_models.check_city import CITY
from app_master.pkg_models.master_text import TEXT
from app_master.pkg_models.master_address import ADDRESS
from app_cdn.pkg_models.check_file_type import FILE_TYPE
from app_cdn.pkg_models.master_file import FILE


# ========================================================================
class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.credential = CREDENTIAL.objects.create(
            email="email@email.com",
            pwd="sha256_password",
            is_admin=True,
            is_internal_user=True,
            is_external_user=True,
        )
        self.continent = CONTINENT.objects.create(
            eng_name="test",
            local_name="test",
        )
        self.country = COUNTRY.objects.create(
            continent=self.continent,
            eng_name="test",
            local_name="test",
        )
        self.state = STATE.objects.create(
            country=self.country,
            eng_name="test",
            local_name="test",
        )
        self.city = CITY.objects.create(
            state=self.state,
            eng_name="test",
            local_name="test",
        )
        self.text = TEXT.objects.create(
            text="test" * 1000,
        )
        self.address = ADDRESS.objects.create(
            city=self.city,
            additional_line=self.text,
            street="test",
            postal_code="1234567890",
            latitude=123.321,
            longitude=123.321,
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
        self.profile = PROFILE.objects.create(
            cred=self.credential,
            address=self.address,
            image=self.file,
            bio=self.text,
            first_name="test",
            middle_name="test",
            last_name="test",
            phone_number="+912222222222",
            date_of_birth="20231222",
            facebook_profile="https://www.facebook.com/",
            twitter_profile="https://www.facebook.com/",
            linkedin_profile="https://www.facebook.com/",
        )

    def test_profile_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.profile.first_name, "test".upper()
        )  # Check if the name is uppercased as expected
        self.assertEqual(
            self.profile.middle_name, "test".upper()
        )  # Check if the name is uppercased as expected
        self.assertEqual(
            self.profile.last_name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_profile_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {} -> {}.{}".format(
            self.profile.company_code,
            self.profile.cred,
            self.profile.first_name,
            self.profile.last_name,
        )
        self.assertEqual(str(self.profile), expected_result)

    def test_profile_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            PROFILE.objects.create(
                cred=self.credential,
                address=self.address,
                image=self.file,
                bio=self.text,
                first_name="test",
                middle_name="test",
                last_name="test",
                phone_number="+912222222222",
                date_of_birth="20231222",
                facebook_profile="https://www.facebook.com/",
                twitter_profile="https://www.facebook.com/",
                linkedin_profile="https://www.facebook.com/",
            )  # Try to create another file type with the same name


class ProfileViewTestCase(TestCase):
    def setUp(self):
        # Create test data for PROFILE
        self.credential = CREDENTIAL.objects.create(
            email="email@email.com",
            pwd="sha256_password",
            is_admin=True,
            is_internal_user=True,
            is_external_user=True,
        )
        self.continent = CONTINENT.objects.create(
            eng_name="test",
            local_name="test",
        )
        self.country = COUNTRY.objects.create(
            continent=self.continent,
            eng_name="test",
            local_name="test",
        )
        self.state = STATE.objects.create(
            country=self.country,
            eng_name="test",
            local_name="test",
        )
        self.city = CITY.objects.create(
            state=self.state,
            eng_name="test",
            local_name="test",
        )
        self.text = TEXT.objects.create(
            text="test" * 1000,
        )
        self.address = ADDRESS.objects.create(
            city=self.city,
            additional_line=self.text,
            street="test",
            postal_code="1234567890",
            latitude=123.321,
            longitude=123.321,
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
        self.profile = PROFILE.objects.create(
            cred=self.credential,
            address=self.address,
            image=self.file,
            bio=self.text,
            first_name="test",
            middle_name="test",
            last_name="test",
            phone_number="+912222222222",
            date_of_birth="20231222",
            facebook_profile="https://www.facebook.com/",
            twitter_profile="https://www.facebook.com/",
            linkedin_profile="https://www.facebook.com/",
        )

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_profile_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Master_Profile", kwargs={"pk": 0}))
        view = Profile.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(
            reverse("Master_Profile", kwargs={"pk": self.profile.id})
        )
        view = Profile.as_view()
        response = view(request, pk=self.profile.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_profile(self):
        # Test POST request for creating a new file type
        data = {
            "cred": CREDENTIAL.objects.create(
                email="email2@email.com",
                pwd="sha256_password",
                is_admin=True,
                is_internal_user=True,
                is_external_user=True,
            ).id,
            "address": ADDRESS.objects.create(
                city=self.city,
                additional_line=self.text,
                street="test",
                postal_code="1234567890",
                latitude=123.321,
                longitude=123.321,
            ).id,
            "image": self.file.id,
            "bio": self.text.id,
            "first_name": "test1",
            "middle_name": "test1",
            "last_name": "test1",
            "phone_number": "+912222222222",
            "date_of_birth": "20231222",
            "facebook_profile": "https://www.facebook.com/",
            "twitter_profile": "https://www.facebook.com/",
            "linkedin_profile": "https://www.facebook.com/",
        }
        request = self.factory.post(
            reverse("Master_Profile", kwargs={"pk": 0}), data=data
        )
        view = Profile.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_profile(self):
        # Test PUT request for updating an existing file type
        data = {
            "cred": self.credential.id,
            "address": self.address.id,
            "image": self.file.id,
            "bio": self.text.id,
            "first_name": "test2",
            "middle_name": "test2",
            "last_name": "test2",
            "phone_number": "+912222222222",
            "date_of_birth": "20231222",
            "facebook_profile": "https://www.facebook.com/",
            "twitter_profile": "https://www.facebook.com/",
            "linkedin_profile": "https://www.facebook.com/",
        }
        request = self.factory.put(
            reverse("Master_Profile", kwargs={"pk": self.profile.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = Profile.as_view()
        response = view(request, pk=self.profile.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_profile(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Master_Profile", kwargs={"pk": self.profile.id})
        )
        view = Profile.as_view()
        response = view(request, pk=self.profile.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
