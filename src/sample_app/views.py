from rest_framework.response import Response
from rest_framework.views import APIView

from common.business import get_now


class StartView(APIView):
    def get(self, request, format=None):
        now = get_now()
        return Response({'run_at': now})
