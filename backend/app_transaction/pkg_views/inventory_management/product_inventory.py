# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_transaction.pkg_models.inventory_management.product_inventory import (
    PRODUCT_INVENTORY_SUMMARY,
    PRODUCT_INVENTORY_ITEM,
)
from app_transaction.pkg_serializers.inventory_management.product_inventory import (
    Product_Inventory_Summary as Product_Inventory_Summary_Serializer,
    Product_Inventory_Item as Product_Inventory_Item_Serializer,
)
from utility.abstract_view import View
from utility.constants import *


# ========================================================================


class Product_Inventory_Summary(View):
    """
    API endpoint for managing product_inventory_summaries.
    """

    serializer_class = Product_Inventory_Summary_Serializer
    queryset = PRODUCT_INVENTORY_SUMMARY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new product_inventory_summary.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        product_inventory_summary_de_serialized = Product_Inventory_Summary_Serializer(
            data=request.data
        )
        try:
            product_inventory_summary_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
        except AttributeError:
            pass
        if product_inventory_summary_de_serialized.is_valid():
            try:
                product_inventory_summary_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Product_Inventory_Summary_Serializer(
                        PRODUCT_INVENTORY_SUMMARY.objects.filter(
                            company_code=self.company_code,
                            buyer=product_inventory_summary_de_serialized.validated_data[
                                "buyer"
                            ],
                            id=product_inventory_summary_de_serialized.validated_data[
                                "id"
                            ],
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[product_inventory_summary_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {product_inventory_summary_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve product_inventory_summary(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            product_inventory_summary_serialized = Product_Inventory_Summary_Serializer(
                PRODUCT_INVENTORY_SUMMARY.objects.all(),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=product_inventory_summary_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                product_inventory_summary_ref = PRODUCT_INVENTORY_SUMMARY.objects.get(
                    id=int(pk)
                )
                product_inventory_summary_serialized = (
                    Product_Inventory_Summary_Serializer(
                        product_inventory_summary_ref, many=False
                    )
                )
                payload = super().create_payload(
                    success=True, data=[product_inventory_summary_serialized.data]
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
        Handle PUT request to update an existing product_inventory_summary.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_inventory_summary_ref = PRODUCT_INVENTORY_SUMMARY.objects.get(
                    id=int(pk)
                )
                product_inventory_summary_de_serialized = (
                    Product_Inventory_Summary_Serializer(
                        product_inventory_summary_ref, data=request.data, partial=True
                    )
                )
                if product_inventory_summary_de_serialized.is_valid():
                    try:
                        product_inventory_summary_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Product_Inventory_Summary_Serializer(
                                PRODUCT_INVENTORY_SUMMARY.objects.filter(
                                    company_code=self.company_code,
                                    buyer=product_inventory_summary_de_serialized.validated_data[
                                        "buyer"
                                    ],
                                    id=product_inventory_summary_de_serialized.validated_data[
                                        "id"
                                    ],
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
                            success=True,
                            data=[product_inventory_summary_de_serialized.data],
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {product_inventory_summary_de_serialized.errors}",
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle DELETE request to delete an existing product_inventory_summary.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_inventory_summary_ref = PRODUCT_INVENTORY_SUMMARY.objects.get(
                    id=int(pk)
                )
                product_inventory_summary_de_serialized = (
                    Product_Inventory_Summary_Serializer(product_inventory_summary_ref)
                )
                product_inventory_summary_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_inventory_summary_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle OPTIONS request to provide information about supported methods and headers.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "buyer": "Integer : /master/master/cred/0",
            "status": "Integer : /master/check/order_stat/0",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "buyer": "Integer : /master/master/cred/0",
            "status": "Integer : /master/check/order_stat/0",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Product_Inventory_Item(View):
    """
    API endpoint for managing product_inventory_summaries.
    """

    serializer_class = Product_Inventory_Item_Serializer
    queryset = PRODUCT_INVENTORY_ITEM.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new product_inventory_Item.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        product_inventory_item_de_serialized = Product_Inventory_Item_Serializer(
            data=request.data
        )
        try:
            product_inventory_item_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                self.company_code
            )
        except AttributeError:
            pass
        if product_inventory_item_de_serialized.is_valid():
            try:
                product_inventory_item_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Product_Inventory_Item_Serializer(
                        PRODUCT_INVENTORY_ITEM.objects.filter(
                            company_code=self.company_code,
                            summary=product_inventory_item_de_serialized.validated_data[
                                "summary"
                            ],
                            product=product_inventory_item_de_serialized.validated_data[
                                "product"
                            ],
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[product_inventory_item_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="{SERIALIZING_ERROR} : {}".format(
                    product_inventory_item_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve product_inventory_Item(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            product_inventory_item_serialized = Product_Inventory_Item_Serializer(
                PRODUCT_INVENTORY_ITEM.objects.all(),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=product_inventory_item_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                product_inventory_Item_ref = PRODUCT_INVENTORY_ITEM.objects.get(
                    id=int(pk)
                )
                product_inventory_item_serialized = Product_Inventory_Item_Serializer(
                    product_inventory_Item_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[product_inventory_item_serialized.data]
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
        Handle PUT request to update an existing product_inventory_Item.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_inventory_Item_ref = PRODUCT_INVENTORY_ITEM.objects.get(
                    id=int(pk)
                )
                product_inventory_item_de_serialized = (
                    Product_Inventory_Item_Serializer(
                        product_inventory_Item_ref, data=request.data, partial=True
                    )
                )
                if product_inventory_item_de_serialized.is_valid():
                    try:
                        product_inventory_item_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Product_Inventory_Item_Serializer(
                                PRODUCT_INVENTORY_ITEM.objects.filter(
                                    company_code=self.company_code,
                                    summary=product_inventory_item_de_serialized.validated_data[
                                        "summary"
                                    ],
                                    product=product_inventory_item_de_serialized.validated_data[
                                        "product"
                                    ],
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
                            success=True,
                            data=[product_inventory_item_de_serialized.data],
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="{SERIALIZING_ERROR} : {}".format(
                            product_inventory_item_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle DELETE request to delete an existing product_inventory_Item.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_inventory_Item_ref = PRODUCT_INVENTORY_ITEM.objects.get(
                    id=int(pk)
                )
                product_inventory_item_de_serialized = (
                    Product_Inventory_Item_Serializer(product_inventory_Item_ref)
                )
                product_inventory_Item_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_inventory_item_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle OPTIONS request to provide information about supported methods and headers.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "summary": "Integer : /master/master/prod_inv/0",
            "product": "Integer : /master/check/product/0",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "buyer": "Integer : /master/master/cred/0",
            "status": "Integer : /master/check/order_stat/0",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
