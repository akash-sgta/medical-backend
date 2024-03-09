# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_unit_of_measurement import UOM
from app_master.pkg_serializers.check_unit_of_measurement import (
    Uom as Uom_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Uom(View):
    serializer_class = Uom_Serializer
    queryset = UOM.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        unit_of_measurement_de_serialized = Uom_Serializer(data=request.data)
        try:
            unit_of_measurement_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
        except AttributeError:
            pass
        if unit_of_measurement_de_serialized.is_valid():
            try:
                unit_of_measurement_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Uom_Serializer(
                        UOM.objects.filter(
                            company_code=self.company_code,
                            unit=unit_of_measurement_de_serialized.validated_data[
                                "unit"
                            ],
                            name=unit_of_measurement_de_serialized.validated_data[
                                "name"
                            ].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[unit_of_measurement_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(
                    unit_of_measurement_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            unit_of_measurement_serialized = Uom_Serializer(
                UOM.objects.filter(company_code=View().company_code), many=True
            )
            payload = super().create_payload(
                success=True, data=unit_of_measurement_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                unit_of_measurement_ref = UOM.objects.get(id=int(pk))
                unit_of_measurement_serialized = Uom_Serializer(
                    unit_of_measurement_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[unit_of_measurement_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                unit_of_measurement_ref = UOM.objects.get(id=int(pk))
                unit_of_measurement_de_serialized = Uom_Serializer(
                    unit_of_measurement_ref, data=request.data, partial=True
                )
                if unit_of_measurement_de_serialized.is_valid():
                    try:
                        unit_of_measurement_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Uom_Serializer(
                                UOM.objects.filter(
                                    company_code=self.company_code,
                                    unit=unit_of_measurement_de_serialized.validated_data[
                                        "unit"
                                    ],
                                    name=unit_of_measurement_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=True,
                            ).data,
                            message=f"{self.get_view_name()}_EXISTS",
                        )
                        return Response(
                            data=payload, status=status.HTTP_400_BAD_REQUEST
                        )
                    else:
                        payload = super().create_payload(
                            success=True, data=[unit_of_measurement_de_serialized.data]
                        )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            unit_of_measurement_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                unit_of_measurement_ref = UOM.objects.get(id=int(pk))
                unit_of_measurement_de_serialized = Uom_Serializer(
                    unit_of_measurement_ref
                )
                unit_of_measurement_ref.delete()
                payload = super().create_payload(
                    success=True, data=[unit_of_measurement_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
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
            "unit": "Integer : /master/check/unit/0",
            "name": "String : 128",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "unit": "Integer : /master/check/unit/0",
            "name": "String : 128",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
