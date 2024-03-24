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
from utility.constants import *

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
            sales_order_status_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                self.company_code
            )
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
                            name=sales_order_status_de_serialized.validated_data[
                                "name"
                            ].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {C_EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True,
                    data=[sales_order_status_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            for error in sales_order_status_de_serialized.errors.values():
                if error[0].code == "unique":
                    payload = super().create_payload(
                        success=False,
                        message=f"{Sales_Order_Status().get_view_name()} {C_EXISTS}",
                        data=[
                            Sales_Order_Status_Serializer(
                                SALES_ORDER_STATUS.objects.get(
                                    name=sales_order_status_de_serialized.data["name"],
                                ),
                                many=False,
                            ).data
                        ],
                    )
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{C_SERIALIZING_ERROR} : {sales_order_status_de_serialized.errors}",
                    )
                break
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve sales_order_status(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            sales_order_status_de_serialized = Sales_Order_Status_Serializer(
                SALES_ORDER_STATUS.objects.all(),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=sales_order_status_de_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                sales_order_status_ref = SALES_ORDER_STATUS.objects.get(id=int(pk))
                sales_order_status_de_serialized = Sales_Order_Status_Serializer(
                    sales_order_status_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[sales_order_status_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
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
                success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
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
                                    name=sales_order_status_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=True,
                            ).data,
                            message=f"{self.get_view_name()} {C_EXISTS}",
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
                        message=f"{C_SERIALIZING_ERROR} : {sales_order_status_de_serialized.errors}",
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
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
                data=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
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
                    message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
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


class Sales_Order_Status_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Sales_Order_Status_Serializer
    queryset = SALES_ORDER_STATUS.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new continent.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if self.C_BATCH in request.data.keys():
            _status = status.HTTP_200_OK
            _payload = []
            _message = []
            for data in request.data[self.C_BATCH]:
                sales_order_status_de_serialized = Sales_Order_Status_Serializer(
                    data=data
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
                    except IntegrityError as e:
                        _payload.append(
                            Sales_Order_Status_Serializer(
                                SALES_ORDER_STATUS.objects.get(
                                    name=sales_order_status_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(
                            f"{Sales_Order_Status().get_view_name()} {C_EXISTS}"
                        )
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(sales_order_status_de_serialized.data)
                        _message.append(None)
                else:
                    for error in sales_order_status_de_serialized.errors.values():
                        if error[0].code == "unique":
                            _status = status.HTTP_409_CONFLICT
                            _payload.append(
                                Sales_Order_Status_Serializer(
                                    SALES_ORDER_STATUS.objects.get(
                                        name=sales_order_status_de_serialized.data[
                                            "name"
                                        ],
                                    ),
                                    many=False,
                                ).data
                            )
                            _message.append(
                                f"{Sales_Order_Status().get_view_name()} {C_EXISTS}"
                            )
                        else:
                            _payload.append(
                                f"{C_SERIALIZING_ERROR} : {sales_order_status_de_serialized.errors}"
                            )
                            _message.append(None)
                        break

            payload = super().create_payload(
                success=True if _status == status.HTTP_200_OK else False,
                data=_payload,
                message=_message,
            )
            return Response(data=payload, status=_status)
        else:
            payload = super().create_payload(
                success=False,
                message="BATCH DATA NOT PROVIDED",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def options(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle OPTIONS request to provide information about supported methods and headers.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        payload = dict()
        payload["Allow"] = "POST OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "batch": [
                {
                    "name": "String : 32",
                },
                {
                    "name": "String : 32",
                },
                {
                    "name": "String : 32",
                },
            ]
        }
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
            inventory_order_status_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                self.company_code
            )
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
                    message=f"{self.get_view_name()} {C_EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True,
                    data=[inventory_order_status_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            for error in inventory_order_status_de_serialized.errors.values():
                if error[0].code == "unique":
                    payload = super().create_payload(
                        success=False,
                        message=f"{Inventory_Order_Status().get_view_name()} {C_EXISTS}",
                        data=[
                            Inventory_Order_Status_Serializer(
                                INVENTORY_ORDER_STATUS.objects.get(
                                    name=inventory_order_status_de_serialized.data[
                                        "name"
                                    ],
                                ),
                                many=False,
                            ).data
                        ],
                    )
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{C_SERIALIZING_ERROR} : {inventory_order_status_de_serialized.errors}",
                    )
                break
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve inventory_order_status(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            inventory_order_status_serialized = Inventory_Order_Status_Serializer(
                INVENTORY_ORDER_STATUS.objects.all(),
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
                    success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
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
                success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
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
                                    name=inventory_order_status_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=True,
                            ).data,
                            message=f"{self.get_view_name()} {C_EXISTS}",
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
                        message=f"{C_SERIALIZING_ERROR} : {inventory_order_status_de_serialized.errors}",
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
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
                data=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
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
                    message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
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


class Inventory_Order_Status_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Inventory_Order_Status_Serializer
    queryset = INVENTORY_ORDER_STATUS.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new continent.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if self.C_BATCH in request.data.keys():
            _status = status.HTTP_200_OK
            _payload = []
            _message = []
            for data in request.data[self.C_BATCH]:
                inventory_order_status_de_serialized = (
                    Inventory_Order_Status_Serializer(data=data)
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
                    except IntegrityError as e:
                        _payload.append(
                            Inventory_Order_Status_Serializer(
                                INVENTORY_ORDER_STATUS.objects.get(
                                    name=inventory_order_status_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(
                            f"{Inventory_Order_Status().get_view_name()} {C_EXISTS}"
                        )
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(inventory_order_status_de_serialized.data)
                        _message.append(None)
                else:
                    for error in inventory_order_status_de_serialized.errors.values():
                        if error[0].code == "unique":
                            _status = status.HTTP_409_CONFLICT
                            _payload.append(
                                Inventory_Order_Status_Serializer(
                                    INVENTORY_ORDER_STATUS.objects.get(
                                        name=inventory_order_status_de_serialized.data[
                                            "name"
                                        ],
                                    ),
                                    many=False,
                                ).data
                            )
                            _message.append(
                                f"{Inventory_Order_Status().get_view_name()} {C_EXISTS}"
                            )
                        else:
                            _payload.append(
                                f"{C_SERIALIZING_ERROR} : {inventory_order_status_de_serialized.errors}"
                            )
                            _message.append(None)
                        break

            payload = super().create_payload(
                success=True if _status == status.HTTP_200_OK else False,
                data=_payload,
                message=_message,
            )
            return Response(data=payload, status=_status)
        else:
            payload = super().create_payload(
                success=False,
                message="BATCH DATA NOT PROVIDED",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def options(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle OPTIONS request to provide information about supported methods and headers.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        payload = dict()
        payload["Allow"] = "POST OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "batch": [
                {
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
