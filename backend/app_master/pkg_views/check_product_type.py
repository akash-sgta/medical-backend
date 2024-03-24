# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_product_type import (
    PRODUCT_TYPE,
    PRODUCT_TYPE_T,
)
from app_master.pkg_serializers.check_product_type import (
    Product_Type as Product_Type_Serializer,
    Product_Type_T as Product_Type_T_Serializer,
)
from utility.abstract_view import View
from utility.constants import *

# ========================================================================


class Product_Type(View):
    serializer_class = Product_Type_Serializer
    queryset = PRODUCT_TYPE.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        product_type_de_serialized = Product_Type_Serializer(data=request.data)
        try:
            product_type_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                self.company_code
            )
        except AttributeError:
            pass
        if product_type_de_serialized.is_valid():
            try:
                product_type_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Product_Type_Serializer(
                        PRODUCT_TYPE.objects.filter(
                            company_code=self.company_code,
                            name=product_type_de_serialized.validated_data[
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
                    data=[product_type_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{C_SERIALIZING_ERROR} : {product_type_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            product_type_serialized = Product_Type_Serializer(
                PRODUCT_TYPE.objects.all(), many=True
            )
            payload = super().create_payload(
                success=True, data=product_type_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                product_type_ref = PRODUCT_TYPE.objects.get(id=int(pk))
                product_type_serialized = Product_Type_Serializer(
                    product_type_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[product_type_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_type_ref = PRODUCT_TYPE.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_Serializer(
                    product_type_ref, data=request.data, partial=True
                )
                if product_type_de_serialized.is_valid():
                    try:
                        product_type_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Product_Type_Serializer(
                                PRODUCT_TYPE.objects.filter(
                                    company_code=self.company_code,
                                    name=product_type_de_serialized.validated_data[
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
                            success=True, data=[product_type_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{C_SERIALIZING_ERROR} : {product_type_de_serialized.errors}",
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
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_type_ref = PRODUCT_TYPE.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_Serializer(product_type_ref)
                product_type_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_type_de_serialized.data]
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


class Product_Type_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Product_Type_Serializer
    queryset = PRODUCT_TYPE.objects.all()

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
                product_type_de_serialized = Product_Type_Serializer(data=data)
                try:
                    product_type_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                        self.company_code
                    )
                except AttributeError:
                    pass
                if product_type_de_serialized.is_valid():
                    try:
                        product_type_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            Product_Type_Serializer(
                                PRODUCT_TYPE.objects.get(
                                    name=product_type_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{Product_Type().get_view_name()} {C_EXISTS}")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(product_type_de_serialized.data)
                        _message.append(None)
                else:
                    _payload.append(None)
                    _message.append(
                        f"{C_SERIALIZING_ERROR} : {product_type_de_serialized.errors}"
                    )

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


class Product_Type_T(View):
    serializer_class = Product_Type_T_Serializer
    queryset = PRODUCT_TYPE_T.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        product_type_de_serialized = Product_Type_T_Serializer(data=request.data)
        product_type_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        if product_type_de_serialized.is_valid():
            try:
                product_type_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Product_Type_T_Serializer(
                        PRODUCT_TYPE_T.objects.filter(
                            type=product_type_de_serialized.validated_data["type"],
                            text=product_type_de_serialized.validated_data["text"],
                            lang=product_type_de_serialized.validated_data["lang"],
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {C_EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True,
                    data=[product_type_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            for error in product_type_de_serialized.errors.values():
                print(error[0].code)
                if error[0].code == "unique":
                    payload = super().create_payload(
                        success=False,
                        message=f"{Product_Type_T().get_view_name()} {C_EXISTS}",
                        data=[
                            Product_Type_T_Serializer(
                                PRODUCT_TYPE_T.objects.get(
                                    type=product_type_de_serialized.data["type"],
                                    text=product_type_de_serialized.data["text"],
                                    lang=product_type_de_serialized.data["lang"],
                                ),
                                many=False,
                            ).data
                        ],
                    )
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{C_SERIALIZING_ERROR} : {product_type_de_serialized.errors}",
                    )
                break
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            product_type_serialized = Product_Type_T_Serializer(
                PRODUCT_TYPE_T.objects.all(),
                many=True,
            )
            payload = super().create_payload(
                success=True, data=product_type_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                product_type_ref = PRODUCT_TYPE_T.objects.get(id=int(pk))
                product_type_serialized = Product_Type_T_Serializer(
                    product_type_ref, many=False
                )
                payload = super().create_payload(
                    success=True, data=[product_type_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {C_DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_type_ref = PRODUCT_TYPE_T.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_T_Serializer(
                    product_type_ref, data=request.data, partial=True
                )
                if product_type_de_serialized.is_valid():
                    try:
                        product_type_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Product_Type_T_Serializer(
                                PRODUCT_TYPE_T.objects.filter(
                                    type=product_type_de_serialized.validated_data[
                                        "type"
                                    ],
                                    text=product_type_de_serialized.validated_data[
                                        "text"
                                    ],
                                    lang=product_type_de_serialized.validated_data[
                                        "lang"
                                    ],
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
                            success=True, data=[product_type_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{C_SERIALIZING_ERROR} : {product_type_de_serialized.errors}",
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
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()} {C_DOES_NOT_EXIST}",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                product_type_ref = PRODUCT_TYPE_T.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_T_Serializer(product_type_ref)
                product_type_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_type_de_serialized.data]
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
        auth = super().authorize(request=request)  # TODO : Do stuff

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = self.get_view_name()
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "type": "Integer : /master/check/product_type/0",
            "lang": "Integer : /master/check/language/0",
            "text": "Integer : /master/master/text/0",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "type": "Integer : /master/check/product_type/0",
            "lang": "Integer : /master/check/language/0",
            "text": "Integer : /master/master/text/0",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Product_Type_T_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Product_Type_T_Serializer
    queryset = PRODUCT_TYPE_T.objects.all()

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
                product_type_t_de_serialized = Product_Type_T_Serializer(data=data)
                try:
                    product_type_t_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                        self.company_code
                    )
                except AttributeError:
                    pass
                if product_type_t_de_serialized.is_valid():
                    try:
                        product_type_t_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            Product_Type_T_Serializer(
                                PRODUCT_TYPE_T.objects.get(
                                    type=product_type_t_de_serialized.validated_data[
                                        "type"
                                    ],
                                    text=product_type_t_de_serialized.validated_data[
                                        "text"
                                    ],
                                    lang=product_type_t_de_serialized.validated_data[
                                        "lang"
                                    ],
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(
                            f"{Product_Type_T().get_view_name()} {C_EXISTS}"
                        )
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(product_type_t_de_serialized.data)
                        _message.append(None)
                else:
                    for error in product_type_t_de_serialized.errors.values():
                        if error[0].code == "unique":
                            _payload.append(
                                Product_Type_T_Serializer(
                                    PRODUCT_TYPE_T.objects.get(
                                        type=product_type_t_de_serialized.data["type"],
                                        text=product_type_t_de_serialized.data["text"],
                                        lang=product_type_t_de_serialized.data["lang"],
                                    ),
                                    many=False,
                                ).data
                            )
                            _message.append(
                                f"{Product_Type_T().get_view_name()} {C_EXISTS}"
                            )
                        else:
                            _payload.append(None)
                            _message.append(
                                f"{C_SERIALIZING_ERROR} : {product_type_t_de_serialized.errors}"
                            )
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
                    "type": "Integer : /master/check/product_type/0",
                    "lang": "Integer : /master/check/language/0",
                    "text": "Integer : /master/master/text/0",
                },
                {
                    "type": "Integer : /master/check/product_type/0",
                    "lang": "Integer : /master/check/language/0",
                    "text": "Integer : /master/master/text/0",
                },
                {
                    "type": "Integer : /master/check/product_type/0",
                    "lang": "Integer : /master/check/language/0",
                    "text": "Integer : /master/master/text/0",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
