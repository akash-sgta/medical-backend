# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION
from app_master.pkg_serializers.master_product_connection import (
    Product_Connection as Product_Connection_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Product_Connection(View):
    serializer_class = Product_Connection_Serializer
    queryset = PRODUCT_CONNECTION.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        product_connection_de_serialized = Product_Connection_Serializer(
            data=request.data
        )
        try:
            product_connection_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
        except AttributeError:
            pass
        if product_connection_de_serialized.is_valid():
            try:
                product_connection_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Product_Connection_Serializer(
                        PRODUCT_CONNECTION.objects.filter(
                            company_code=self.company_code,
                            type=product_connection_de_serialized.validated_data[
                                "type"
                            ],
                            name=product_connection_de_serialized.validated_data[
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
                    success=True, data=[product_connection_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(
                    product_connection_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            product_connection_serialized = Product_Connection_Serializer(
                PRODUCT_CONNECTION.objects.all(),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=product_connection_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                product_connection_ref = PRODUCT_CONNECTION.objects.get(id=int(pk))
                product_connection_serialized = Product_Connection_Serializer(
                    product_connection_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[product_connection_serialized.data]
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
                product_connection_ref = PRODUCT_CONNECTION.objects.get(id=int(pk))
                product_connection_de_serialized = Product_Connection_Serializer(
                    product_connection_ref, data=request.data, partial=True
                )
                if product_connection_de_serialized.is_valid():
                    try:
                        product_connection_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Product_Connection_Serializer(
                                PRODUCT_CONNECTION.objects.filter(
                                    company_code=self.company_code,
                                    type=product_connection_de_serialized.validated_data[
                                        "type"
                                    ],
                                    name=product_connection_de_serialized.validated_data[
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
                            success=True, data=[product_connection_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            product_connection_de_serialized.errors
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
                product_connection_ref = PRODUCT_CONNECTION.objects.get(id=int(pk))
                product_connection_de_serialized = Product_Connection_Serializer(
                    product_connection_ref
                )
                product_connection_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_connection_de_serialized.data]
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
            "parent": "Integer : /master/master/product/0",
            "parent_uom": "Integer : /master/check/uom/0",
            "child": "Integer : /master/master/product/0",
            "child_uom": "Integer : /master/check/uom/0",
            "parent_quantity": "Float",
            "child_quantity": "Float",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "parent": "Integer : /master/master/product/0",
            "parent_uom": "Integer : /master/check/uom/0",
            "child": "Integer : /master/master/product/0",
            "child_uom": "Integer : /master/check/uom/0",
            "parent_quantity": "Float",
            "child_quantity": "Float",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
