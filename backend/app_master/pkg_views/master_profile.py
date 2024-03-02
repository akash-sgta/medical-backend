# ========================================================================
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_profile import PROFILE
from app_master.pkg_serializers.master_profile import (
    Profile as Profile_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Profile(View):
    serializer_class = Profile_Serializer
    queryset = PROFILE.objects.filter(company_code=View().company_code)

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        profile_de_serialized = Profile_Serializer(data=request.data)
        profile_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        if profile_de_serialized.is_valid():
            try:
                profile_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Profile_Serializer(
                        PROFILE.objects.filter(
                            company_code=self.company_code,
                            cred=profile_de_serialized.validated_data["cred"],
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[profile_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(profile_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            profile_serialized = Profile_Serializer(
                PROFILE.objects.filter(company_code=View().company_code),
                many=True,
            )
            payload = super().create_payload(success=True, data=profile_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                profile_ref = PROFILE.objects.get(id=int(pk))
                profile_serialized = Profile_Serializer(profile_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[profile_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except PROFILE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                profile_ref = PROFILE.objects.get(id=int(pk))
                profile_de_serialized = Profile_Serializer(
                    profile_ref, data=request.data, partial=True
                )
                if profile_de_serialized.is_valid():
                    profile_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[profile_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            profile_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except PROFILE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                profile_ref = PROFILE.objects.get(id=int(pk))
                profile_de_serialized = Profile_Serializer(profile_ref)
                profile_ref.delete()
                payload = super().create_payload(
                    success=True, data=[profile_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except PROFILE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "cred": "Integer : /master/master/credential/0",
            "address": "Integer : /master/master/address/0",
            "image": "Integer : /cdn/master/file/0",
            "bio": "Integer : /master/master/text/0",
            "first_name": "String : 128",
            "middle_name": "String : 128",
            "last_name": "String : 128",
            "date_of_birth": "Date : YYYYMMDD",
            "facebook_profile": "String : 256",
            "twitter_profile": "String : 256",
            "linkedin_profile": "String : 256",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "cred": "Integer : /master/master/credential/0",
            "address": "Integer : /master/master/address/0",
            "image": "Integer : /cdn/master/file/0",
            "bio": "Integer : /master/master/text/0",
            "first_name": "String : 128",
            "middle_name": "String : 128",
            "last_name": "String : 128",
            "date_of_birth": "Date : YYYYMMDD",
            "facebook_profile": "String : 256",
            "twitter_profile": "String : 256",
            "linkedin_profile": "String : 256",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
