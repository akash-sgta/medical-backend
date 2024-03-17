# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_country import COUNTRY
from app_master.pkg_serializers.check_country import (
    Country as Country_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Country(View):
    """
    API endpoint for managing countries.
    """

    serializer_class = Country_Serializer
    queryset = COUNTRY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new country.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        country_de_serialized = Country_Serializer(data=request.data)
        try:
            country_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if country_de_serialized.is_valid():
            try:
                country_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Country_Serializer(
                        COUNTRY.objects.filter(
                            continent=country_de_serialized.validated_data["continent"],
                            eng_name=country_de_serialized.validated_data[
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
                    success=True, data=[country_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(country_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve country(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            country_serialized = Country_Serializer(COUNTRY.objects.all(), many=True)
            payload = super().create_payload(success=True, data=country_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                country_ref = COUNTRY.objects.get(id=int(pk))
                country_serialized = Country_Serializer(country_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[country_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle PUT request to update an existing country.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                country_ref = COUNTRY.objects.get(id=int(pk))
                country_de_serialized = Country_Serializer(
                    country_ref, data=request.data, partial=True
                )
                if country_de_serialized.is_valid():
                    try:
                        country_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Country_Serializer(
                                COUNTRY.objects.filter(
                                    continent=country_de_serialized.validated_data[
                                        "continent"
                                    ],
                                    eng_name=country_de_serialized.validated_data[
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
                            success=True, data=[country_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_200_OK)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            country_de_serialized.errors
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
        Handle DELETE request to delete an existing country.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                country_ref = COUNTRY.objects.get(id=int(pk))
                country_de_serialized = Country_Serializer(country_ref)
                country_ref.delete()
                payload = super().create_payload(
                    success=True, data=[country_de_serialized.data]
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
            "continent": "Integer : /master/check/continent/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "continent": "Integer : /master/check/continent/0",
            "eng_name": "String : 32",
            "local_name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Country_Batch(View):
    """
    API endpoint for managing continents.
    """

    serializer_class = Country_Serializer
    queryset = COUNTRY.objects.all()

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
                country_de_serialized = Country_Serializer(data=data)
                try:
                    country_de_serialized.initial_data[
                        self.C_COMPANY_CODE
                    ] = self.company_code
                except AttributeError:
                    pass
                if country_de_serialized.is_valid():
                    try:
                        country_de_serialized.save()
                    except IntegrityError as e:
                        _payload.append(
                            Country_Serializer(
                                COUNTRY.objects.get(
                                    continent=country_de_serialized.validated_data[
                                        "continent"
                                    ],
                                    eng_name=country_de_serialized.validated_data[
                                        "eng_name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{Country().get_view_name()}_EXISTS")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(country_de_serialized.data)
                        _message.append(None)
                else:
                    _payload.append(None)
                    _message.append(
                        "SERIALIZING_ERROR : {}".format(country_de_serialized.errors)
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
                    "continent": "Integer : /master/check/continent/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "continent": "Integer : /master/check/continent/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
                {
                    "continent": "Integer : /master/check/continent/0",
                    "eng_name": "String : 32",
                    "local_name": "String : 32",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
