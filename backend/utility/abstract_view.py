# ========================================================================
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from utility.methods import am_i_authorized
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


# ========================================================================


class View(GenericAPIView):
    # renderer_classes = [JSONRenderer]

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
