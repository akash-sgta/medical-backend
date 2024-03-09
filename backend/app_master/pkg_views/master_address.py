# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_address import ADDRESS
from app_master.pkg_serializers.master_address import (
    Address as Address_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Address(View):
    serializer_class = Address_Serializer
    queryset = ADDRESS.objects.filter(company_code=View().company_code)

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        address_de_serialized = Address_Serializer(data=request.data)
        try:
            address_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if address_de_serialized.is_valid():
            try:
                address_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Address_Serializer(
                        ADDRESS.objects.filter(
                            company_code=self.company_code,
                            name=address_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[address_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(address_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            address_serialized = Address_Serializer(
                ADDRESS.objects.filter(company_code=View().company_code), many=True
            )
            payload = super().create_payload(success=True, data=address_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                address_ref = ADDRESS.objects.get(id=int(pk))
                address_serialized = Address_Serializer(address_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[address_serialized.data]
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
                address_ref = ADDRESS.objects.get(id=int(pk))
                address_de_serialized = Address_Serializer(
                    address_ref, data=request.data, partial=True
                )
                if address_de_serialized.is_valid():
                    try:
                        address_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Address_Serializer(
                                ADDRESS.objects.filter(
                                    company_code=self.company_code,
                                    name=address_de_serialized.validated_data[
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
                            success=True, data=[address_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            address_de_serialized.errors
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
                address_ref = ADDRESS.objects.get(id=int(pk))
                address_de_serialized = Address_Serializer(address_ref)
                address_ref.delete()
                payload = super().create_payload(
                    success=True, data=[address_de_serialized.data]
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
            "city": "Integer : /master/check/state/0",
            "street": "String : 128",
            "postal_code": "String : 32",
            "additional_line": "Integer : /master/master/text/0",
            "latitude": "Decimal : [max 9, decimal 6]",
            "longitude": "Decimal : [max 9, decimal 6]",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "city": "Integer : /master/check/state/0",
            "street": "String : 128",
            "postal_code": "String : 32",
            "additional_line": "Integer : /master/master/text/0",
            "latitude": "Decimal : [max 9, decimal 6]",
            "longitude": "Decimal : [max 9, decimal 6]",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
