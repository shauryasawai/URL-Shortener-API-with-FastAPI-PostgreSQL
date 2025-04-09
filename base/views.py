from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortenURL(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            shorturl = serializer.save()
            short_url = request.build_absolute_uri(f'/{shorturl.short_code}')
            return Response({"short_url": short_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectURL(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(short_url.original_url)
