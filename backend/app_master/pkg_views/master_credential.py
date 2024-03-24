# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_credential import CREDENTIAL
from app_master.pkg_serializers.master_credential import (
    Credential as Credential_Serializer,
)
from utility.abstract_view import View
from utility.constants import *


# ========================================================================


class Credential(View):
    serializer_class = Credential_Serializer
    queryset = CREDENTIAL.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        credential_de_serialized = Credential_Serializer(data=request.data)
        try:
            credential_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                self.company_code
            )
        except AttributeError:
            pass
        if credential_de_serialized.is_valid():
            try:
                credential_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    # data=Credential_Serializer(
                    #     CREDENTIAL.objects.filter(
                    #         company_code=self.company_code,
                    #         email=credential_de_serialized.validated_data[
                    #             "email"
                    #         ].upper(),
                    #     ),
                    #     many=True,
                    # ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[credential_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {credential_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            credential_serialized = Credential_Serializer(
                CREDENTIAL.objects.all(), many=True
            )
            payload = super().create_payload(
                success=True, data=credential_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                credential_ref = CREDENTIAL.objects.get(id=int(pk))
                credential_serialized = Credential_Serializer(
                    credential_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[credential_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                credential_ref = CREDENTIAL.objects.get(id=int(pk))
                credential_de_serialized = Credential_Serializer(
                    credential_ref, data=request.data, partial=True
                )
                if credential_de_serialized.is_valid():
                    try:
                        credential_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            # data=Credential_Serializer(
                            #     CREDENTIAL.objects.filter(
                            #         company_code=self.company_code,
                            #         email=credential_de_serialized.validated_data[
                            #             "email"
                            #         ].upper(),
                            #     ),
                            #     many=True,
                            # ).data,
                            message=f"{self.get_view_name()} {EXISTS}",
                        )
                        return Response(
                            data=payload, status=status.HTTP_400_BAD_REQUEST
                        )
                    else:
                        payload = super().create_payload(
                            success=True, data=[credential_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {credential_de_serialized.errors}",
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                credential_ref = CREDENTIAL.objects.get(id=int(pk))
                credential_de_serialized = Credential_Serializer(credential_ref)
                credential_ref.delete()
                payload = super().create_payload(
                    success=True, data=[credential_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "email": "String : 128",
            "pwd": "String : 128",
            # "is_admin": "Boolean : true/false",
            # "is_internal_user": "Boolean : true/false",
            # "is_external_user": "Boolean : true/false",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "email": "String : 128",
            "pwd": "String : 128",
            # "is_admin": "Boolean : true/false",
            # "is_internal_user": "Boolean : true/false",
            # "is_external_user": "Boolean : true/false",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
