# ========================================================================
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

# ========================================================================


class Product_Type(View):
    serializer_class = Product_Type_Serializer
    queryset = PRODUCT_TYPE.objects.filter(company_code=View().company_code)

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        product_type_de_serialized = Product_Type_Serializer(data=request.data)
        try:
            product_type_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
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
                    message=f"{self.get_view_name()}_EXISTS",
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
                message="SERIALIZING_ERROR : {}".format(
                    product_type_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if pk is None or int(pk) <= 0:
            product_type_serialized = Product_Type_Serializer(
                PRODUCT_TYPE.objects.filter(company_code=View().company_code), many=True
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
            except PRODUCT_TYPE.DoesNotExist:
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
                product_type_ref = PRODUCT_TYPE.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_Serializer(
                    product_type_ref, data=request.data, partial=True
                )
                if product_type_de_serialized.is_valid():
                    product_type_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[product_type_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            product_type_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except PRODUCT_TYPE.DoesNotExist:
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
                product_type_ref = PRODUCT_TYPE.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_Serializer(product_type_ref)
                product_type_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_type_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except PRODUCT_TYPE.DoesNotExist:
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
            "name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Product_Type_T(View):
    serializer_class = Product_Type_T_Serializer
    queryset = PRODUCT_TYPE_T.objects.filter(company_code=View().company_code)

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
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
                            company_code=self.company_code,
                            type=product_type_de_serialized.validated_data["type"],
                            text=product_type_de_serialized.validated_data["text"],
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
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
                message="SERIALIZING_ERROR : {}".format(
                    product_type_de_serialized.errors
                ),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            product_type_serialized = Product_Type_T_Serializer(
                PRODUCT_TYPE_T.objects.filter(company_code=View().company_code),
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
            except PRODUCT_TYPE_T.DoesNotExist:
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
                product_type_ref = PRODUCT_TYPE_T.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_T_Serializer(
                    product_type_ref, data=request.data, partial=True
                )
                if product_type_de_serialized.is_valid():
                    product_type_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[product_type_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            product_type_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except PRODUCT_TYPE_T.DoesNotExist:
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
                product_type_ref = PRODUCT_TYPE_T.objects.get(id=int(pk))
                product_type_de_serialized = Product_Type_T_Serializer(product_type_ref)
                product_type_ref.delete()
                payload = super().create_payload(
                    success=True, data=[product_type_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except PRODUCT_TYPE_T.DoesNotExist:
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
