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
from utility.constants import *


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
                            code=currency_de_serialized.validated_data["code"].upper(),
                            eng_name=currency_de_serialized.validated_data[
                                "eng_name"
                            ].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True, data=[currency_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            for error in currency_de_serialized.errors.values():
                if error[0].code == "unique":
                    payload = super().create_payload(
                        success=False,
                        message=f"{Currency().get_view_name()} {EXISTS}",
                        data=[
                            Currency_Serializer(
                                CURRENCY.objects.get(
                                    code=currency_de_serialized.validated_data[
                                        "code"
                                    ].upper(),
                                    eng_name=currency_de_serialized.validated_data[
                                        "eng_name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        ],
                    )
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {currency_de_serialized.errors}",
                    )
                break
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {currency_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            currency_serialized = Currency_Serializer(CURRENCY.objects.all(), many=True)
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
                                    code=currency_de_serialized.validated_data[
                                        "code"
                                    ].upper(),
                                    eng_name=currency_de_serialized.validated_data[
                                        "eng_name"
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
                            success=True, data=[currency_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {currency_de_serialized.errors}",
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
                currency_ref = CURRENCY.objects.get(id=int(pk))
                currency_de_serialized = Currency_Serializer(currency_ref)
                currency_ref.delete()
                payload = super().create_payload(
                    success=True, data=[currency_de_serialized.data]
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


class Currency_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Currency_Serializer
    queryset = CURRENCY.objects.all()

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
                currency_de_serialized = Currency_Serializer(data=data)
                try:
                    currency_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                        self.company_code
                    )
                except AttributeError:
                    pass
                if currency_de_serialized.is_valid():
                    try:
                        currency_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            Currency_Serializer(
                                CURRENCY.objects.get(
                                    code=currency_de_serialized.validated_data["code"],
                                    eng_name=currency_de_serialized.validated_data[
                                        "eng_name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{Currency().get_view_name()} {EXISTS}")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(currency_de_serialized.data)
                        _message.append(None)
                else:
                    for error in currency_de_serialized.errors.values():
                        if error[0].code == "unique":
                            _payload.append(
                                Currency_Serializer(
                                    CURRENCY.objects.get(
                                        code=currency_de_serialized.validated_data[
                                            "code"
                                        ].upper(),
                                        eng_name=currency_de_serialized.validated_data[
                                            "eng_name"
                                        ].upper(),
                                    ),
                                    many=False,
                                ).data
                            )
                            _message.append(
                                f"{Currency().get_view_name()} {EXISTS}",
                            )
                        else:
                            _payload.append(None)
                            _message.append(
                                f"{SERIALIZING_ERROR} : {currency_de_serialized.errors}"
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
                    "code": "String : 4",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                    "symbol": "String : 4",
                },
                {
                    "code": "String : 4",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                    "symbol": "String : 4",
                },
                {
                    "code": "String : 4",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                    "symbol": "String : 4",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
