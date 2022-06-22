from django.shortcuts import render
from rest_framework import generics, views, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# class LogoutView(views.APIView):
#     serializer_class = LogoutSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status.HTTP_204_NO_CONTENT)

class BlacklistRefreshView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")

