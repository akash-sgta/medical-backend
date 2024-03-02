# ========================================================================
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from utility.custom_permission import CustomPermission
from utility.methods import am_i_authorized
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from utility.abstract_models import COMPANY, COMPANY_CODE

# ========================================================================


class View(GenericAPIView):
    # renderer_classes = [JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]  # Default permission class

    def __init__(self):
        super().__init__()
        self.company_code = COMPANY
        self.C_COMPANY_CODE = COMPANY_CODE

    def create_payload(self, success: bool, message=None, data=[]) -> dict:
        data = {"success": success, "message": message, "data": data}
        return data

    def authorize(self, request) -> tuple:
        data = ([False, None], [False, None])
        is_authorized_api = am_i_authorized(request, "API")
        if not is_authorized_api[0]:
            payload = self.create_payload(
                success=False, message="ENDPOINT_NOT_AUTHORIZED"
            )
            data[0][1] = Response(data=payload, status=status.HTTP_401_UNAUTHORIZED)
        else:
            data[0][0] = True

        is_authorized_user = am_i_authorized(request, "USER")
        if not is_authorized_user[0]:
            payload = self.create_payload(success=False, message="USER_NOT_AUTHORIZED")
            data[1][1] = Response(data=payload, status=status.HTTP_401_UNAUTHORIZED)
        else:
            data[1][0] = True

        return data

    def get_permissions(self):
        if self.request.method == "POST":
            return [CustomPermission()]  # Apply custom permission for POST method
        return super().get_permissions()
