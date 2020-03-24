from django.shortcuts import render

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response

from .serializers import UserSerializer, UserSigninSerializer
from .authentication import token_expire_handler, expires_in
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views.generic import CreateView
from .form import CreateUserForm

@api_view(["POST"])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def signin_api(request):
    signin_serializer = UserSigninSerializer(data = request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status = HTTP_400_BAD_REQUEST)


    user = authenticate(
            username = signin_serializer.data['username'],
            password = signin_serializer.data['password'] 
        )
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        
    #TOKEN STUFF
    token, _ = Token.objects.get_or_create(user = user)
    
    #token_expire_handler will check, if the token is expired it will generate new one
    is_expired, token = token_expire_handler(token)     # The implementation will be described further
    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data, 
        'expires_in': expires_in(token),
        'token': token.key
    }, status=HTTP_200_OK)


@api_view(["GET"])
def user_info_api(request):
    return Response({
        'user': request.user.username,
        'expires_in': expires_in(request.auth)
    }, status=HTTP_200_OK)

class CreateUser(CreateView):
    def post(self, request, *args, **kwargs):
        form = CreateUserForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # ここでログインさせる
            return redirect('/')
        return render(request, 'user/create.html.haml', {'form': form})
    def get(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        return render(request, 'user/create.html.haml', {"form": form})
create_account = CreateUser.as_view()

class LoginView(AuthLoginView):
    template_name = 'user/login.html.haml'


login=LoginView.as_view()
