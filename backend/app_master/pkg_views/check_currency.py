# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_currency import CURRENCY
from app_master.pkg_serializers.check_currency import (
    Currency as Currency_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Currency(View):
    serializer_class = Currency_Serializer
    queryset = CURRENCY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        currency_de_serialized = Currency_Serializer(data=request.data)
        try:
            currency_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if currency_de_serialized.is_valid():
            try:
                currency_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Currency_Serializer(
                        CURRENCY.objects.filter(
                            company_code=self.company_code,
                            code=currency_de_serialized.validated_data["code"].upper(),
                            eng_name=currency_de_serialized.validated_data[
                                "eng_name"
                            ].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[currency_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(currency_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            currency_serialized = Currency_Serializer(
                CURRENCY.objects.filter(company_code=View().company_code), many=True
            )
            payload = super().create_payload(
                success=True, data=currency_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                currency_ref = CURRENCY.objects.get(id=int(pk))
                currency_serialized = Currency_Serializer(currency_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[currency_serialized.data]
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
                currency_ref = CURRENCY.objects.get(id=int(pk))
                currency_de_serialized = Currency_Serializer(
                    currency_ref, data=request.data, partial=True
                )
                if currency_de_serialized.is_valid():
                    try:
                        currency_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Currency_Serializer(
                                CURRENCY.objects.filter(
                                    company_code=self.company_code,
                                    code=currency_de_serialized.validated_data[
                                        "code"
                                    ].upper(),
                                    eng_name=currency_de_serialized.validated_data[
                                        "eng_name"
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
                            success=True, data=[currency_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            currency_de_serialized.errors
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
                currency_ref = CURRENCY.objects.get(id=int(pk))
                currency_de_serialized = Currency_Serializer(currency_ref)
                currency_ref.delete()
                payload = super().create_payload(
                    success=True, data=[currency_de_serialized.data]
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
            "code": "String : 4",
            "eng_name": "String : 32",
            "local_name": "String : 32",
            "symbol": "String : 4",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "code": "String : 4",
            "eng_name": "String : 32",
            "local_name": "String : 32",
            "symbol": "String : 4",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
