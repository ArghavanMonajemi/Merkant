from rest_framework import exceptions
from rest_framework.views import exception_handler as drf_exception_handler
from django.http import JsonResponse


ERROR_CODES = {
    400: "bad_request",
    401: "not_authenticated",
    403: "permission_denied",
    404: "not_found",
    405: "method_not_allowed",
    415: "unsupported_media_type",
    429: "throttled",
}

def not_found(request, exception=None):
    return JsonResponse(
        {"error": {"code": "not_found", "message": "Resource not found."}},
        status=404,
    )

def server_error(request):
    return JsonResponse(
        {"error": {"code": "server_error", "message": "Internal server error."}},
        status=500,
    )

def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        # Unexpected error: let Django handle it (see handler500 below)
        return None

    if isinstance(exc, exceptions.ValidationError):
        error = {
            "code": "validation_error",
            "message": "Invalid input.",
            "details": response.data,
        }
    else:
        data = response.data
        message = data.get("detail", "Error") if isinstance(data, dict) else str(data)
        error = {
            "code": ERROR_CODES.get(response.status_code, "error"),
            "message": str(message),
        }

    response.data = {"error": error}
    return response