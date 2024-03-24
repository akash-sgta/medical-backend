# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_product import PRODUCT
from app_master.pkg_serializers.master_product import (
    Product as Product_Serializer,
)
from utility.abstract_view import View
from utility.constants import *


# ========================================================================


class Product(View):
    serializer_class = Product_Serializer
    queryset = PRODUCT.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        product_de_serialized = Product_Serializer(data=request.data)
        try:
            product_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if product_de_serialized.is_valid():
            try:
                product_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Product_Serializer(
                        PRODUCT.objects.filter(
                            company_code=self.company_code,
                            type=product_de_serialized.validated_data["type"],
                            name=product_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[product_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {product_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            product_serialized = Product_Serializer(PRODUCT.objects.all(), many=True)
            payload = super().create_payload(success=True, data=product_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                product_ref = PRODUCT.objects.get(id=int(pk))
                product_serialized = Product_Serializer(product_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[product_serialized.data]
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
                product_ref = PRODUCT.objects.get(id=int(pk))
                product_de_serialized = Product_Serializer(
                    product_ref, data=request.data, partial=True
                )
                if product_de_serialized.is_valid():
                    try:
                        product_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Product_Serializer(
                                PRODUCT.objects.filter(
                                    company_code=self.company_code,
                                    type=product_de_serialized.validated_data["type"],
                                    name=product_de_serialized.validated_data[
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
                            success=True, data=[product_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {product_de_serialized.errors}",
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
                product_ref = PRODUCT.objects.get(id=int(pk))
                product_de_serialized = Product_Serializer(product_ref)
                product_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_de_serialized.data]
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
            "type": "Integer : /master/check/type/0",
            "image_01": "Integer : /master/master/file/0",
            "image_02": "Integer : /master/master/file/0",
            "image_03": "Integer : /master/master/file/0",
            "currency": "Integer : /master/check/currency/0",
            "description": "Integer : /master/master/text/0",
            "storage_instructions": "Integer : /master/master/text/0",
            "side_effects": "Integer : /master/master/text/0",
            "warnings_precautions": "Integer : /master/master/text/0",
            "contraindications": "Integer : /master/master/text/0",
            "name": "String : 32",
            "manufacturer": "String : 128",
            "dosage": "String : 64",
            "price": "Decimal : [max 15, dec 2]",
            "url": "String : 128",
            "is_prescription_required": "Boolean : true/false",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "type": "Integer : /master/check/type/0",
            "image_01": "Integer : /master/master/file/0",
            "image_02": "Integer : /master/master/file/0",
            "image_03": "Integer : /master/master/file/0",
            "currency": "Integer : /master/check/currency/0",
            "description": "Integer : /master/master/text/0",
            "storage_instructions": "Integer : /master/master/text/0",
            "side_effects": "Integer : /master/master/text/0",
            "warnings_precautions": "Integer : /master/master/text/0",
            "contraindications": "Integer : /master/master/text/0",
            "name": "String : 32",
            "manufacturer": "String : 128",
            "dosage": "String : 64",
            "price": "Decimal : [max 15, dec 2]",
            "url": "String : 128",
            "is_prescription_required": "Boolean : true/false",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
