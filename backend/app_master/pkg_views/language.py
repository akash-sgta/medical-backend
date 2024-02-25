# ========================================================================
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.check_language import LANGUAGE
from app_master.pkg_serializers.language import (
    Language as Language_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Language(View):
    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        language_de_serialized = Language_Serializer(data=request.data)
        if language_de_serialized.is_valid():
            language_de_serialized.save()
            payload = super().create_payload(
                success=True, data=[language_de_serialized.data]
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(language_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            language_serialized = Language_Serializer(LANGUAGE.objects.all(), many=True)
            payload = super().create_payload(
                success=True, data=language_serialized.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                language_ref = LANGUAGE.objects.get(id=int(pk))
                language_serialized = Language_Serializer(language_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[language_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except LANGUAGE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message="LANGUAGE_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message="LANGUAGE_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                language_ref = LANGUAGE.objects.get(id=int(pk))
                language_de_serialized = Language_Serializer(
                    language_ref, data=request.data
                )
                if language_de_serialized.is_valid():
                    language_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[language_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            language_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except LANGUAGE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message="LANGUAGE_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, data="LANGUAGE_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                language_ref = LANGUAGE.objects.get(id=int(pk))
                language_de_serialized = Language_Serializer(language_ref)
                language_ref.delete()
                payload = super().create_payload(
                    success=True, data=[language_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except LANGUAGE.DoesNotExist:
                payload = super().create_payload(
                    success=False, message="LANGUAGE_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = "Language"
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
