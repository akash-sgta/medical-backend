# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_state import STATE
from app_master.pkg_serializers.check_state import (
    State as State_Serializer,
)
from utility.abstract_view import View
from utility.constants import *

# ========================================================================


class State(View):
    serializer_class = State_Serializer
    queryset = STATE.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        state_de_serialized = State_Serializer(data=request.data)
        try:
            state_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if state_de_serialized.is_valid():
            try:
                state_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=State_Serializer(
                        STATE.objects.filter(
                            company_code=self.company_code,
                            eng_name=state_de_serialized.validated_data[
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
                    success=True,
                    data=[state_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {state_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            state_serialized = State_Serializer(STATE.objects.all(), many=True)
            payload = super().create_payload(success=True, data=state_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                state_ref = STATE.objects.get(id=int(pk))
                state_serialized = State_Serializer(state_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[state_serialized.data]
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
                state_ref = STATE.objects.get(id=int(pk))
                state_de_serialized = State_Serializer(
                    state_ref, data=request.data, partial=True
                )
                if state_de_serialized.is_valid():
                    try:
                        state_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=State_Serializer(
                                STATE.objects.filter(
                                    company_code=self.company_code,
                                    eng_name=state_de_serialized.validated_data[
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
                            success=True,
                            data=[state_de_serialized.data],
                        )
                        return Response(data=payload, status=status.HTTP_200_OK)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {state_de_serialized.errors}",
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()} {DOES_NOT_EXIST}",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()} {DOES_NOT_EXIST}",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                state_ref = STATE.objects.get(id=int(pk))
                state_de_serialized = State_Serializer(state_ref)
                state_ref.delete()
                payload = super().create_payload(
                    success=True, data=[state_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()} {DOES_NOT_EXIST}",
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
            "country": "Integer : /master/check/country/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "country": "Integer : /master/check/country/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class State_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = State_Serializer
    queryset = STATE.objects.all()

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
                state_de_serialized = State_Serializer(data=data)
                try:
                    state_de_serialized.initial_data[self.C_COMPANY_CODE] = (
                        self.company_code
                    )
                except AttributeError:
                    pass
                if state_de_serialized.is_valid():
                    try:
                        state_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            State_Serializer(
                                STATE.objects.get(
                                    country=state_de_serialized.validated_data[
                                        "country"
                                    ],
                                    eng_name=state_de_serialized.validated_data[
                                        "eng_name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{State().get_view_name()} {EXISTS}")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(state_de_serialized.data)
                        _message.append(None)
                else:
                    _payload.append(None)
                    _message.append(
                        "{SERIALIZING_ERROR} : {}".format(state_de_serialized.errors)
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
                    "country": "Integer : /master/check/country/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "country": "Integer : /master/check/country/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "country": "Integer : /master/check/country/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
