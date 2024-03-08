# ========================================================================
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from app_master.pkg_models.master_company import COMPANY
from app_master.pkg_serializers.master_company import (
    Compamy as Compamy_Serializer,
)
from utility.abstract_view import View

# ========================================================================


class Compamy(View):
    """
    API endpoint for managing companys.
    """

    serializer_class = Compamy_Serializer
    queryset = COMPANY.objects.all()

    def __init__(self):
        super().__init__()

    def post(self, request, pk=None):
        """
        Handle POST request to create a new company.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        company_de_serialized = Compamy_Serializer(data=request.data)
        try:
            company_de_serialized.initial_data[self.C_COMPANY_CODE] = self.company_code
        except AttributeError:
            pass
        if company_de_serialized.is_valid():
            try:
                company_de_serialized.save()
            except IntegrityError:
                payload = super().create_payload(
                    success=False,
                    data=Compamy_Serializer(
                        COMPANY.objects.filter(
                            name=company_de_serialized.validated_data["name"].upper(),
                        ),
                        many=True,
                    ).data,
                    message=f"{self.get_view_name()}_EXISTS",
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
                message="SERIALIZING_ERROR : {}".format(company_de_serialized.errors),
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        """
        Handle GET request to retrieve company(s).
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if pk is None or int(pk) <= 0:
            company_serialized = Compamy_Serializer(COMPANY.objects.all(), many=True)
            payload = super().create_payload(success=True, data=company_serialized.data)
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            try:
                company_ref = COMPANY.objects.get(id=int(pk))
                company_serialized = Compamy_Serializer(company_ref, many=False)
                payload = super().create_payload(
                    success=True, data=[company_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except COMPANY.DoesNotExist:
                payload = super().create_payload(
                    success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        """
        Handle PUT request to update an existing company.
        """
        auth = super().authorize(request=request)  # Authorization logic - TODO

        if int(pk) <= 0:
            payload = super().create_payload(
                success=False, message=f"{self.get_view_name()}_DOES_NOT_EXIST"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                company_ref = COMPANY.objects.get(id=int(pk))
                company_de_serialized = Compamy_Serializer(
                    company_ref, data=request.data, partial=True
                )
                if company_de_serialized.is_valid():
                    company_de_serialized.save()
                    payload = super().create_payload(
                        success=True, data=[company_de_serialized.data]
                    )
                    return Response(data=payload, status=status.HTTP_201_CREATED)
                else:
                    payload = super().create_payload(
                        success=False,
                        message="SERIALIZING_ERROR : {}".format(
                            company_de_serialized.errors
                        ),
                    )
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            except COMPANY.DoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        """
        Handle DELETE request to delete an existing company.
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
                company_ref = COMPANY.objects.get(id=int(pk))
                company_de_serialized = Compamy_Serializer(company_ref)
                company_ref.delete()
                payload = super().create_payload(
                    success=True, data=[company_de_serialized.data]
                )
                return Response(data=payload, status=status.HTTP_200_OK)
            except COMPANY.DoesNotExist:
                payload = super().create_payload(
                    success=False,
                    message=f"{self.get_view_name()}_DOES_NOT_EXIST",
                )
                return Response(data=payload, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, pk=None):
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
