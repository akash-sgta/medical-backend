# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_company import COMPANY
from app_master.pkg_serializers.master_company import (
    Company as Company_Serializer,
)
from utility.abstract_view import View
from utility.constants import *

# ========================================================================


class Company(View):
    """
    API endpoint for managing companys.
    """

    serializer_class = Company_Serializer
    queryset = COMPANY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new company.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        company_de_serialized = Company_Serializer(data=request.data)
        if company_de_serialized.is_valid():
            try:
                company_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Company_Serializer(
                        COMPANY.objects.filter(
                            name=company_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()} {EXISTS}",
                )
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = super().create_payload(
                    success=True,
                    data=[company_de_serialized.data],
                )
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = super().create_payload(
                success=False,
                message=f"{SERIALIZING_ERROR} : {company_de_serialized.errors}",
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle GET request to retrieve company(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            company_serialized = Company_Serializer(COMPANY.objects.all(), many=True)
            payload = super().create_payload(success=True, data=company_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                company_ref = COMPANY.objects.get(id=int(pk))
                company_serialized = Company_Serializer(company_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[company_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle PUT request to update an existing company.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()} {DOES_NOT_EXIST}"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                company_ref = COMPANY.objects.get(id=int(pk))
                company_de_serialized = Company_Serializer(
                    company_ref, data=request.data, partial=True
                )
                if company_de_serialized.is_valid():
                    try:
                        company_de_serialized.save()
                    except IntegrityError:
                        payload = super().create_payload(
                            success=False,
                            data=Company_Serializer(
                                COMPANY.objects.filter(
                                    name=company_de_serialized.validated_data[
                                        "name"
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
                            success=True, data=[company_de_serialized.data]
                        )
                        return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message=f"{SERIALIZING_ERROR} : {company_de_serialized.errors}",
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
        """
        Handle DELETE request to delete an existing company.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False,
                data=f"{self.get_view_name()} {DOES_NOT_EXIST}",
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                company_ref = COMPANY.objects.get(id=int(pk))
                company_de_serialized = Company_Serializer(company_ref)
                try:
                    company_ref.delete()
                except Exception as e:
                    payload = super().create_payload(success=False, message=str(e))
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
                else:
                    payload = super().create_payload(
                        success=True, data=[company_de_serialized.data]
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
            "name": "String : 32",
        }
        payload["method"]["GET"] = None
        payload["method"]["PUT"] = {
            "name": "String : 32",
        }
        payload["method"]["DELETE"] = None

        return Response(data=payload, status=status.HTTP_200_OK)


class Company_Batch(View):
    """
    API endpoint for managing companys.
    """

    serializer_class = Company_Serializer
    queryset = COMPANY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        pk = self.update_pk(pk)
        """
        Handle POST request to create a new company.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if self.C_BATCH in request.data.keys():
            _status = status.HTTP_200_OK
            _payload = []
            _message = []
            for data in request.data[self.C_BATCH]:
                company_de_serialized = Company_Serializer(data=data)
                if company_de_serialized.is_valid():
                    try:
                        company_de_serialized.save()
                    except IntegrityError:
                        _payload.append(
                            Company_Serializer(
                                COMPANY.objects.get(
                                    name=company_de_serialized.validated_data[
                                        "name"
                                    ].upper(),
                                ),
                                many=False,
                            ).data
                        )
                        _message.append(f"{Company().get_view_name()} {EXISTS}")
                        _status = status.HTTP_409_CONFLICT
                    else:
                        _payload.append(company_de_serialized.data)
                        _message.append(None)
                else:
                    _payload.append(None)
                    _message.append(
                        f"{SERIALIZING_ERROR} : {company_de_serialized.errors}"
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
                    "name1": "String : 32",
                },
                {
                    "name2": "String : 32",
                },
                {
                    "name3": "String : 32",
                },
            ]
        }
        return Response(data=payload, status=status.HTTP_200_OK)
