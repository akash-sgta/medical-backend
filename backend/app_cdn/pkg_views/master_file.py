# ========================================================================
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_cdn.pkg_models.master_file import FILE
from app_cdn.pkg_serializers.master_file import (
    File as File_Serializer,
)
from utility.abstract_view import View

# ========================================================================


class File(View):
    serializer_class = File_Serializer
    queryset = FILE.objects.filter(company_code=View().company_code)

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        file_de_serialized = File_Serializer(data=request.data)
        try:
            file_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if file_de_serialized.is_valid():
            try:
                file_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=File_Serializer(
                        FILE.objects.filter(
                            company_code=self.company_code,
                            type=file_de_serialized.validated_data["type"],
                            name=file_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True,
                    data=[file_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(file_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if pk is None or int(pk) <= 0:
            file_serialized = File_Serializer(
                FILE.objects.filter(company_code=View().company_code), many=True
            )
            payload = super().create_payload(success=True, data=file_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                file_ref = FILE.objects.get(id=int(pk))
                file_serialized = File_Serializer(file_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[file_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except FILE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if pk is None or int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                file_ref = FILE.objects.get(id=int(pk))
                file_de_serialized = File_Serializer(
                    file_ref, data=request.data, partial=True
                )
                if file_de_serialized.is_valid():
                    file_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[file_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            file_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except FILE.DoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()}_DOES_NOT_EXIST",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                file_ref = FILE.objects.get(id=int(pk))
                file_de_serialized = File_Serializer(file_ref)
                file_ref.delete()
                payload = super().create_payload(
                    success=True, data=[file_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except FILE.DoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
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
            "type": "Integer : /cdn/check/file_type/0",
            "name": "String : 128",
            "size": "Float",
            "url": "String : 256",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "type": "Integer : /cdn/check/file_type/0",
            "name": "String : 128",
            "size": "Float",
            "url": "String : 256",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
