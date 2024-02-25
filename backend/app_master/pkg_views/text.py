# ========================================================================
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.text import TEXT
from app_master.pkg_serializers.text import (
    Text as Text_Serializer,
)
from utility.abstract_view import View


# ========================================================================


class Text(View):
    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        text_de_serialized = Text_Serializer(data=request.data)
        if text_de_serialized.is_valid():
            text_de_serialized.save()
            payload = super().create_payload(
                success=True, data=[text_de_serialized.data]
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message="SERIALIZING_ERROR : {}".format(text_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            text_serialized = Text_Serializer(TEXT.objects.all(), many=True)
            payload = super().create_payload(success=True, data=text_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                text_ref = TEXT.objects.get(id=int(pk))
                text_serialized = Text_Serializer(text_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[text_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except TEXT.DoesNotExist:
                payload = super().create_payload(
                    success=False, message="TEXT_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message="TEXT_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                text_ref = TEXT.objects.get(id=int(pk))
                text_de_serialized = Text_Serializer(text_ref, data=request.data)
                if text_de_serialized.is_valid():
                    text_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[text_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            text_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except TEXT.DoesNotExist:
                payload = super().create_payload(
                    success=False, message="TEXT_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        if int(pk) <= 0:
            payload = super().create_payload(success=False, data="TEXT_DOES_NOT_EXIST")
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                text_ref = TEXT.objects.get(id=int(pk))
                text_de_serialized = Text_Serializer(text_ref)
                text_ref.delete()
                payload = super().create_payload(
                    success=True, data=[text_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except TEXT.DoesNotExist:
                payload = super().create_payload(
                    success=False, message="TEXT_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
        auth = super().authorize(request=request)  # TODO : Do stuff

        payload = dict()
        payload["Allow"] = "POST GET PUT DELETE OPTIONS".split()
        payload["HEADERS"] = dict()
        payload["HEADERS"]["Content-Type"] = "application/json"
        payload["HEADERS"]["Authorization"] = "Token JWT"
        payload["name"] = "Text"
        payload["method"] = dict()
        payload["method"]["POST"] = {
            "text": "String : 128",
            "lang_id": "Integer",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "text": "String : 128",
            "lang_id": "Integer",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)
