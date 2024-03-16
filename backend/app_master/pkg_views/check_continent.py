# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
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
    """
    API endpoint for managing continents.
    """

    serializer_class = Continent_Serializer
    queryset = CONTINENT.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new continent.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        continent_de_serialized = Continent_Serializer(data=request.data)
        try:
            continent_de_serialized.initial_data[
                self.C_COMPANY_CODE
            ] = self.company_code
        except AttributeError:
            pass
        if continent_de_serialized.is_valid():
            try:
                continent_de_serialized.save()
            except IntegrityError as e:
                payload = super().create_payload(
                    success=False,
                    data=Continent_Serializer(
                        CONTINENT.objects.filter(
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
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve continent(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            continent_serialized = Continent_Serializer(
                CONTINENT.objects.filter(), many=True
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
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle PUT request to update an existing continent.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                continent_ref = CONTINENT.objects.get(id=int(pk))
                continent_de_serialized = Continent_Serializer(
                    continent_ref, data=request.data, partial=True
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
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle DELETE request to delete an existing continent.
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
                continent_ref = CONTINENT.objects.get(id=int(pk))
                continent_de_serialized = Continent_Serializer(continent_ref)
                continent_ref.delete()
                payload = super().create_payload(
                    success=True, data=[continent_de_serialized.data]
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
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Continent_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Continent_Serializer
    queryset = CONTINENT.objects.all()

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
                continent_de_serialized = Continent_Serializer(data=data)
                try:
                    continent_de_serialized.initial_data[
                        self.C_COMPANY_CODE
                    ] = self.company_code
                except AttributeError:
                    pass
                if continent_de_serialized.is_valid():
                    try:
                        continent_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            Continent_Serializer(
                                CONTINENT.objects.get(
                                    eng_name=continent_de_serialized.validated_data[
                                        "eng_name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{Continent().get_view_name()}_EXISTS")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(continent_de_serialized.data)
                        _message.append(None)
                else:
                    _payload.append(None)
                    _message.append(
                        "SERIALIZING_ERROR : {}".format(continent_de_serialized.errors)
                    )

            payload = super().create_payload(
                success=True if _status == status.HTTP_200_OK else False,
                data=_payload,
                message=_message,
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
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
                {"eng_name": "String : 32", "local_name": "String : 32"},
                {"eng_name": "String : 32", "local_name": "String : 32"},
                {"eng_name": "String : 32", "local_name": "String : 32"},
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
