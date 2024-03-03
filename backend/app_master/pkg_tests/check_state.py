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

from app_master.pkg_views.check_state import State
from app_master.pkg_models.check_state import STATE
from app_master.pkg_models.check_country import COUNTRY
from app_master.pkg_models.check_continent import CONTINENT


# ========================================================================
class StateModelTestCase(TestCase):
    def setUp(self):
        # Create test data
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

    def test_state_creation(self):
        # Test if the file type object was created successfully
        self.assertEqual(
            self.state.eng_name, "test".upper()
        )  # Check if the name is uppercased as expected

    def test_state_str_method(self):
        # Test the __str__ method
        expected_result = "[{}] {} -> {}".format(
            self.state.company_code, self.state.country, self.state.eng_name
        )
        self.assertEqual(str(self.state), expected_result)

    def test_state_unique_constraint(self):
        # Test uniqueness constraint for name field
        with self.assertRaises(Exception):
            STATE.objects.create(
                country=self.country,
                eng_name="test",
                local_name="test",
            )  # Try to create another file type with the same name


class StateViewTestCase(TestCase):
    def setUp(self):
        # Create test data for CITY
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

        # Initialize the request factory
        self.factory = RequestFactory()

    def test_get_state_list(self):
        # Test GET request for fetching list of file types
        request = self.factory.get(reverse("Check_State", kwargs={"pk": 0}))
        view = State.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_state_detail(self):
        # Test GET request for fetching detail of a file type
        request = self.factory.get(reverse("Check_State", kwargs={"pk": self.state.id}))
        view = State.as_view()
        response = view(request, pk=self.state.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_state(self):
        # Test POST request for creating a new file type
        data = {
            "country": self.country.id,
            "eng_name": "test1",
            "local_name": "test1",
        }
        request = self.factory.post(reverse("Check_State", kwargs={"pk": 0}), data=data)
        view = State.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_state(self):
        # Test PUT request for updating an existing file type
        data = {
            "country": self.country.id,
            "eng_name": "test2",
            "local_name": "test2",
        }
        request = self.factory.put(
            reverse("Check_State", kwargs={"pk": self.state.id}),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        view = State.as_view()
        response = view(request, pk=self.state.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_state(self):
        # Test DELETE request for deleting an existing file type
        request = self.factory.delete(
            reverse("Check_State", kwargs={"pk": self.state.id})
        )
        view = State.as_view()
        response = view(request, pk=self.state.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
