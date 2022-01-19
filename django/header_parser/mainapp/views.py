from rest_framework.views import APIView
from rest_framework.response import Response

class HeaderParserView(APIView):
    def get(self, request):
        return Response({
            "ipaddres": request.META['REMOTE_ADDR'],
            "language": request.META['HTTP_ACCEPT_LANGUAGE'],
            "software": request.META['HTTP_USER_AGENT']})