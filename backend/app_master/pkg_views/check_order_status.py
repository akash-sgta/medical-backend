# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_order_status import (
    SALES_ORDER_STATUS,
    INVENTORY_ORDER_STATUS,
)
from app_master.pkg_serializers.check_order_status import (
    Sales_Order_Status as Sales_Order_Status_Serializer,
    Inventory_Order_Status as Inventory_Order_Status_Serializer,
)
from utility.abstract_view import View

# ========================================================================


class Sales_Order_Status(View):
    """
    API endpoint for managing sales_order_statuss.
    """

    serializer_class = Sales_Order_Status_Serializer
    queryset = SALES_ORDER_STATUS.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new sales_order_status.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        sales_order_status_de_serialized = Sales_Order_Status_Serializer(
            data=request.data
        )
        try:
            sales_order_status_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
        except AttributeError:
            pass
        if sales_order_status_de_serialized.is_valid():
            try:
                sales_order_status_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Sales_Order_Status_Serializer(
                        SALES_ORDER_STATUS.objects.filter(
                            company_code=self.company_code,
                            name=sales_order_status_de_serialized.validated_data[
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
                    success=True,
                    data=[sales_order_status_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(
                    sales_order_status_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve sales_order_status(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            sales_order_status_serialized = Sales_Order_Status_Serializer(
                SALES_ORDER_STATUS.objects.filter(
                    company_code=self.company_code,
                ),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=sales_order_status_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                sales_order_status_ref = SALES_ORDER_STATUS.objects.get(id=int(pk))
                sales_order_status_serialized = Sales_Order_Status_Serializer(
                    sales_order_status_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[sales_order_status_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle PUT request to update an existing sales_order_status.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                sales_order_status_ref = SALES_ORDER_STATUS.objects.get(id=int(pk))
                sales_order_status_de_serialized = Sales_Order_Status_Serializer(
                    sales_order_status_ref, data=request.data, partial=True
                )
                if sales_order_status_de_serialized.is_valid():
                    try:
                        sales_order_status_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Sales_Order_Status_Serializer(
                                SALES_ORDER_STATUS.objects.filter(
                                    company_code=self.company_code,
                                    name=sales_order_status_de_serialized.validated_data[
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
                            success=True, data=[sales_order_status_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            sales_order_status_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle DELETE request to delete an existing sales_order_status.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()}_DOES_NOT_EXIST",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                sales_order_status_ref = SALES_ORDER_STATUS.objects.get(id=int(pk))
                sales_order_status_de_serialized = Sales_Order_Status_Serializer(
                    sales_order_status_ref
                )
                sales_order_status_ref.delete()
                payload = super().create_payload(
                    success=True, data=[sales_order_status_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
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
            "name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Inventory_Order_Status(View):
    """
    API endpoint for managing inventory_order_statuss.
    """

    serializer_class = Inventory_Order_Status_Serializer
    queryset = INVENTORY_ORDER_STATUS.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new inventory_order_status.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        inventory_order_status_de_serialized = Inventory_Order_Status_Serializer(
            data=request.data
        )
        try:
            inventory_order_status_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
        except AttributeError:
            pass
        if inventory_order_status_de_serialized.is_valid():
            try:
                inventory_order_status_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Inventory_Order_Status_Serializer(
                        INVENTORY_ORDER_STATUS.objects.filter(
                            company_code=self.company_code,
                            name=inventory_order_status_de_serialized.validated_data[
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
                    success=True,
                    data=[inventory_order_status_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(
                    inventory_order_status_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve inventory_order_status(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            inventory_order_status_serialized = Inventory_Order_Status_Serializer(
                INVENTORY_ORDER_STATUS.objects.filter(
                    company_code=self.company_code,
                ),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=inventory_order_status_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                inventory_order_status_ref = INVENTORY_ORDER_STATUS.objects.get(
                    id=int(pk)
                )
                inventory_order_status_serialized = Inventory_Order_Status_Serializer(
                    inventory_order_status_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[inventory_order_status_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle PUT request to update an existing inventory_order_status.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                inventory_order_status_ref = INVENTORY_ORDER_STATUS.objects.get(
                    id=int(pk)
                )
                inventory_order_status_de_serialized = (
                    Inventory_Order_Status_Serializer(
                        inventory_order_status_ref, data=request.data, partial=True
                    )
                )
                if inventory_order_status_de_serialized.is_valid():
                    try:
                        inventory_order_status_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Inventory_Order_Status_Serializer(
                                INVENTORY_ORDER_STATUS.objects.filter(
                                    company_code=self.company_code,
                                    name=inventory_order_status_de_serialized.validated_data[
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
                            success=True,
                            data=[inventory_order_status_de_serialized.data],
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            inventory_order_status_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle DELETE request to delete an existing inventory_order_status.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()}_DOES_NOT_EXIST",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                inventory_order_status_ref = INVENTORY_ORDER_STATUS.objects.get(
                    id=int(pk)
                )
                inventory_order_status_de_serialized = (
                    Inventory_Order_Status_Serializer(inventory_order_status_ref)
                )
                inventory_order_status_ref.delete()
                payload = super().create_payload(
                    success=True, data=[inventory_order_status_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
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
            "name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
