# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_cdn.pkg_models.check_file_type import FILE_TYPE
from app_cdn.pkg_serializers.check_file_type import (
    File_Type as File_Type_Serializer,
)
from utility.abstract_view import View
from utility.constants import *

# ========================================================================


class File_Type(View):
    """
    API endpoint for managing file types.
    """

    serializer_class = File_Type_Serializer
    queryset = FILE_TYPE.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new file type.
        """
        auth = super().authorize(request=request)  # TODO : Do stuff

        file_type_de_serialized = File_Type_Serializer(data=request.data)
        try:
            file_type_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                self.company_code
            )
        except AttributeError:
            pass
        if file_type_de_serialized.is_valid():
            try:
                file_type_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=File_Type_Serializer(
                        FILE_TYPE.objects.filter(
                            company_code=self.company_code,
                            name=file_type_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True,
                    data=[file_type_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {file_type_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve file type(s).
        """
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            file_type_serialized = File_Type_Serializer(
                FILE_TYPE.objects.all(), many=True
            )
            payload = super().create_payload(
                success=True, data=file_type_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                file_type_ref = FILE_TYPE.objects.get(id=int(pk))
                file_type_serialized = File_Type_Serializer(file_type_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[file_type_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle PUT request to update an existing file type.
        """
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                file_type_ref = FILE_TYPE.objects.get(id=int(pk))
                file_type_de_serialized = File_Type_Serializer(
                    file_type_ref, data=request.data, partial=True
                )
                if file_type_de_serialized.is_valid():
                    try:
                        file_type_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=File_Type_Serializer(
                                FILE_TYPE.objects.filter(
                                    company_code=self.company_code,
                                    name=file_type_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=True,
                            ).data,
                            message=f"{self.get_view_name()} {EXISTS}",
                        )
                        return Response(
                            data=payload, status=status.HTTP_400_BAD_REQUEST
                        )
                    else:
                        payload = super().create_payload(
                            success=True, data=[file_type_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {file_type_de_serialized.errors}",
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()} {DOES_NOT_EXIST}",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle DELETE request to delete an existing file type.
        """
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()} {DOES_NOT_EXIST}",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                file_type_ref = FILE_TYPE.objects.get(id=int(pk))
                file_type_de_serialized = File_Type_Serializer(file_type_ref)
                file_type_ref.delete()
                payload = super().create_payload(
                    success=True, data=[file_type_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()} {DOES_NOT_EXIST}",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle OPTIONS request to provide information about supported methods and headers.
        """
        auth = super().authorize(request=request)  # TODO : Do stuff

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "name": "String : 8",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "name": "String : 8",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
