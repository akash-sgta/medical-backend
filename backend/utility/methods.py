# ========================================================================
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# ========================================================================
@api_view(["GET"])
def check_server_status(request):
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    message = f"Server is live with current time : {date}"
    return Response(data=message, status=status.HTTP_200_OK)


def get_current_ts(f=0) -> float:
    epoch = datetime.utcfromtimestamp(f)
    dt = (datetime.utcnow() - epoch).total_seconds()
    return dt


def get_date_time_from_ts(ts=0) -> tuple:
    dt = datetime.utcfromtimestamp(ts)
    date = dt.strftime("%Y-%m-%d")
    time = dt.strftime("%H:%M:%S")
    return date, time


def post_error_to_terminal(text: str):
    now = datetime.now()
    current_date = f"{now.year}-{now.month}-{now.day}"
    current_time = now.strftime("%H:%M:%S")
    print(f"[!] [{current_date} {current_time}] {text}")


def post_message_to_terminal(text: str):
    now = datetime.now()
    current_date = f"{now.year}-{now.month}-{now.day}"
    current_time = now.strftime("%H:%M:%S")
    print(f"[.] [{current_date} {current_time}] {text}")


def am_i_authorized(request, name) -> tuple:
    return True, None
