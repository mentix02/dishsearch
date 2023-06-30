from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, authenticate


class LoginView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "user/login.html")

    def post(self, request: HttpRequest) -> HttpResponse:

        username, password = request.POST.get("username"), request.POST.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dish:home")
            else:
                return render(request, "user/login.html", {"error": "Invalid credenrtials."}, status=400)
        else:
            return render(request, "user/login.html", {"error": "Username or password not provided."}, status=400)
