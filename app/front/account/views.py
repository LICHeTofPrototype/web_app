from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response

from api.api_account.serializers import UserSerializer, SignInSerializer
from api.api_account.authentication import token_expire_handler, expires_in
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .form import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm

import logging
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin # authのみ制限する場合
from django.contrib.auth.mixins import PermissionRequiredMixin # 全てのpermissionで制限する場合


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

class Signup(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html.haml'
    def post(self, request, *args, **kwargs):
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # ここでログインさせる
            # login(request, user)
            # messages.info(request, form.cleaned_data.get('password'))
            return redirect(sign_in)
        else:
            return render(request, 'user/signup.html.haml', {'form': form})
    def get(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        return render(request, 'user/signup.html.haml', {"form": form})
sign_up = Signup.as_view()

class Signin(AuthLoginView):
    template_name = 'user/signin.html.haml'
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
            if not user:
                raise Exception("user not found.")
            return render(request, 'user/show.html.haml', {'user': user})
        else:
            return render(request, 'user/signin.html.haml', {"form": form})

sign_in=Signin.as_view()

class UserShow(LoginRequiredMixin, TemplateView):
    template_name = 'user/show.html.haml'
    
user_show = UserShow.as_view()
