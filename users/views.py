from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.views import View
from rest_framework import generics
from .models import GeekUser
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = GeekUser.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeekUser.objects.all()
    serializer_class = UserSerializer


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.clean_password2())
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": user_form})


class UserRegisterView(View):
    template_name = "registration/register.html"

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
        
            return redirect("registration")

        return render(request, self.template_name, {'form': form})