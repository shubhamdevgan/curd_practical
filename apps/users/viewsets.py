from .models import UserModel
from .serializers import RegisterSerializer, UpdateSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SignUpViewSet(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UpdateProfileViewSet(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UpdateSerializer

    def get_object(self):
        return self.request.user


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class LogoutViewSet(APIView):
    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        data = {
            'status': 'Successfull',
            'message': 'Successfully Logged Out.'
        }
        return Response(data=data, status=status.HTTP_200_OK)


class DeleteUserViewSet(APIView):
    def get(self, request, *args, **kwargs):
        request.user.delete()
        data = {
            'status': 'Successfull',
            'message': 'User Successfully Deleted.'
        }
        return Response(data=data, status=status.HTTP_200_OK)
