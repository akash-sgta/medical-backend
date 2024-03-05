# ========================================================================
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_unit import UNIT
from app_master.pkg_serializers.check_unit import (
    Unit as Unit_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Unit(View):
    serializer_class = Unit_Serializer
    queryset = UNIT.objects.filter(company_code=View().company_code)

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        unit_de_serialized = Unit_Serializer(data=request.data)
        try:
            unit_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if unit_de_serialized.is_valid():
            try:
                unit_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Unit_Serializer(
                        UNIT.objects.filter(
                            company_code=self.company_code,
                            name=unit_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[unit_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(unit_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if pk is None or int(pk) <= 0:
            unit_serialized = Unit_Serializer(
                UNIT.objects.filter(company_code=View().company_code), many=True
            )
            payload = super().create_payload(success=True, data=unit_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                unit_ref = UNIT.objects.get(id=int(pk))
                unit_serialized = Unit_Serializer(unit_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[unit_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except UNIT.DoesNotExist:
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
                unit_ref = UNIT.objects.get(id=int(pk))
                unit_de_serialized = Unit_Serializer(
                    unit_ref, data=request.data, partial=True
                )
                if unit_de_serialized.is_valid():
                    unit_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[unit_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            unit_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except UNIT.DoesNotExist:
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
                unit_ref = UNIT.objects.get(id=int(pk))
                unit_de_serialized = Unit_Serializer(unit_ref)
                unit_ref.delete()
                payload = super().create_payload(
                    success=True, data=[unit_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except UNIT.DoesNotExist:
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
            "name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
