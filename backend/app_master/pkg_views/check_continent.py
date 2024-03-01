# ========================================================================
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_continent import CONTINENT
from app_master.pkg_serializers.check_continent import (
    Continent as Continent_Serializer,
)
from utility.abstract_view import View

# ========================================================================


class Continent(View):
    serializer_class = Continent_Serializer
    queryset = CONTINENT.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        continent_de_serialized = Continent_Serializer(data=request.data)
        continent_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        if continent_de_serialized.is_valid():
            try:
                continent_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Continent_Serializer(
                        CONTINENT.objects.filter(
                            company_code=self.company_code,
                            eng_name=continent_de_serialized.validated_data[
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
                    data=[continent_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(continent_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            continent_serialized = Continent_Serializer(
                CONTINENT.objects.all(), many=True
            )
            payload = super().create_payload(
                success=True, data=continent_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                continent_ref = CONTINENT.objects.get(id=int(pk))
                continent_serialized = Continent_Serializer(continent_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[continent_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except CONTINENT.DoesNotExist:
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
                continent_ref = CONTINENT.objects.get(id=int(pk))
                continent_de_serialized = Continent_Serializer(
                    continent_ref, data=request.data
                )
                if continent_de_serialized.is_valid():
                    continent_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[continent_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            continent_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except CONTINENT.DoesNotExist:
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
                continent_ref = CONTINENT.objects.get(id=int(pk))
                continent_de_serialized = Continent_Serializer(continent_ref)
                continent_ref.delete()
                payload = super().create_payload(
                    success=True, data=[continent_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except CONTINENT.DoesNotExist:
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
