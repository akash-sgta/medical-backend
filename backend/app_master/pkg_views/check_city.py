# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_company import COMPANY
from app_master.pkg_models.check_city import CITY
from app_master.pkg_serializers.check_city import (
    City as City_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class City(View):
    """
    API endpoint for managing cities.
    """

    serializer_class = City_Serializer
    queryset = CITY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new city.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        city_de_serialized = City_Serializer(data=request.data)
        try:
            city_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if city_de_serialized.is_valid():
            try:
                city_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=City_Serializer(
                        CITY.objects.filter(
                            state=city_de_serialized.validated_data["state"],
                            eng_name=city_de_serialized.validated_data[
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
                    success=True, data=[city_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            for error in city_de_serialized.errors.values():
                if error[0].code == "unique":
                    payload = super().create_payload(
                        success=False,
                        message=f"{City().get_view_name()}_EXISTS",
                        data=[
                            City_Serializer(
                                CITY.objects.get(
                                    state=city_de_serialized.validated_data["state"],
                                    eng_name=city_de_serialized.validated_data[
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
                        message="SERIALIZING_ERROR : {}".format(
                            city_de_serialized.errors
                        ),
                    )
                break
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve city(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            city_serialized = City_Serializer(CITY.objects.all(), many=True)
            payload = super().create_payload(success=True, data=city_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                city_ref = CITY.objects.get(id=int(pk))
                city_serialized = City_Serializer(city_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[city_serialized.data]
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
        Handle PUT request to update an existing city.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                city_ref = CITY.objects.get(id=int(pk))
                city_de_serialized = City_Serializer(
                    city_ref, data=request.data, partial=True
                )
                if city_de_serialized.is_valid():
                    try:
                        city_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=City_Serializer(
                                CITY.objects.filter(
                                    state=city_de_serialized.validated_data["state"],
                                    eng_name=city_de_serialized.validated_data[
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
                            success=True, data=[city_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            city_de_serialized.errors
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
        """
        Handle DELETE request to delete an existing city.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                city_ref = CITY.objects.get(id=int(pk))
                city_de_serialized = City_Serializer(city_ref)
                city_ref.delete()
                payload = super().create_payload(
                    success=True, data=[city_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
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
            "state": "Integer : /master/check/state/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "state": "Integer : /master/check/state/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class City_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = City_Serializer
    queryset = CITY.objects.all()

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
                city_de_serialized = City_Serializer(data=data)
                try:
                    city_de_serialized.initial_data[
                        self.C_COMPANY_CODE
                    ] = self.company_code
                except AttributeError:
                    pass
                if city_de_serialized.is_valid():
                    try:
                        city_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            City_Serializer(
                                CITY.objects.get(
                                    state=city_de_serialized.validated_data["state"],
                                    eng_name=city_de_serialized.validated_data[
                                        "eng_name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{City().get_view_name()}_EXISTS")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(city_de_serialized.data)
                        _message.append(None)
                else:
                    for error in city_de_serialized.errors.values():
                        if error[0].code == "unique":
                            _payload.append(
                                City_Serializer(
                                    CITY.objects.get(
                                        state=city_de_serialized.validated_data[
                                            "state"
                                        ],
                                        eng_name=city_de_serialized.validated_data[
                                            "eng_name"
                                        ].upper(),
                                    ),
                                    many=False,
                                ).data
                            )
                            _message.append(
                                f"{City().get_view_name()}_EXISTS",
                            )
                        else:
                            _payload.append(None)
                            _message.append(
                                "SERIALIZING_ERROR : {}".format(
                                    city_de_serialized.errors
                                )
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
                    "state": "Integer : /master/check/state/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "state": "Integer : /master/check/state/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "state": "Integer : /master/check/state/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
