from django.http import Http404
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Link
from .serializers import LinkSerializer, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from . permissions import IsPremiumUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class GetUsersProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many = False)
        return Response(serializer.data)

# Create your views here.
class ShortenerUrlApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        queryset = Link.objects.all()
        serializer = LinkSerializer(queryset, many=True, context={"user": user})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = LinkSerializer(data=data, context={"request": request, "user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class RetrieveUrlApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Link.objects.all().filter(pk=pk).first()
        except Exception:
            raise Http404

    def get(self, request, pk=None):
        url = self.get_object(pk=pk)
        if url:
            url.count += 1
            url.save()
            serializer = LinkSerializer(url, context={'user': request.user})
            return Response(serializer.data)
        return Response({'error': 'Object not found!'})

    def delete(self, request, pk=None):
        url = self.get_object(pk=pk)
        url.delete()

        return Response({'Object deleted!'})
        
class Redirector(APIView):
    def get(self, request, shortener_link= None, *args, **kwargs):
        redirect_link = Link.objects.filter(shortened_link__contains = shortener_link).first()
        redirect_link.count += 1
        redirect_link.save()
        return redirect(redirect_link.original_link)

