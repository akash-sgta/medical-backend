# ========================================================================
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_state import STATE
from app_master.pkg_serializers.check_state import (
    State as State_Serializer,
)
from utility.abstract_view import View

# ========================================================================


class State(View):
    serializer_class = State_Serializer
    queryset = STATE.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        state_de_serialized = State_Serializer(data=request.data)
        state_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
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
                    message=f"{self.get_view_name()}_EXISTS",
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
                message="SERIALIZING_ERROR : {}".format(state_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
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
            except STATE.DoesNotExist:
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
                state_ref = STATE.objects.get(id=int(pk))
                state_de_serialized = State_Serializer(state_ref, data=request.data)
                if state_de_serialized.is_valid():
                    state_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[state_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            state_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except STATE.DoesNotExist:
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
                state_ref = STATE.objects.get(id=int(pk))
                state_de_serialized = State_Serializer(state_ref)
                state_ref.delete()
                payload = super().create_payload(
                    success=True, data=[state_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except STATE.DoesNotExist:
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
            "state": "Integer : /master/state/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "state": "Integer : /master/state/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
