from django.shortcuts import render
from .models import Ticket
from .models import TicketForm, UserForm
from datetime import datetime
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
class Home(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("/login/")

        print(request.POST)
        if request.POST["source"] == "update":
            id = request.POST["id"]
            t = Ticket.objects.get(id=id)
            f = TicketForm(request.POST, instance = t)

            location = f.data['location']
            date_received = f.data['date_received']
            time_marked = f.data['time_marked']
            time_issued = f.data['time_issued']
            time_limit = f.data['time_limit']
            region = f.data['region']
            weather = f.data['weather']
            username = request.user

            t = Ticket(id=id, location=location, date_received=date_received, time_marked=time_marked, time_issued=time_issued,
                       time_limit=time_limit, region=region, weather=weather, username=username)
            t.save()
            print("update")
            return redirect("/results/")
        else:
            f = TicketForm(request.POST)
            print("create")

        if f.is_valid():
            location = f.cleaned_data['location']
            date_received = f.cleaned_data['date_received']
            time_marked = f.cleaned_data['time_marked']
            time_issued = f.cleaned_data['time_issued']
            time_limit = f.cleaned_data['time_limit']
            region = f.cleaned_data['region']
            weather = f.cleaned_data['weather']

            if not isinstance(request.user, User):
                return redirect("/login/")

            username = request.user

            t = Ticket(location=location, date_received=date_received, time_marked=time_marked, time_issued=time_issued, time_limit=time_limit, region=region, weather=weather, username=username)
            t.save()
            ret = redirect("/results/")
        else:
            ret = render(request, "index.html", {'form':f, "update":request.POST["update"]})
        return ret

    def get(self, request):
        if not request.user.is_authenticated:
            redirect("/login/")
        form = TicketForm()
        return render(request, "index.html", {'form': form, 'action': "/", "source": "create"})


class Delete(View):
    def get(self, request):
        id = request.GET['id']
        t = Ticket.objects.get(id=id)
        t.delete()
        return redirect("/results/")


class Results(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/login/")
        tickets = Ticket.objects.all()
        return render(request, "results.html", {'tickets':tickets})


class Update(View):
    def get(self, request):
        id = request.GET['id']
        action = '/'
        t = Ticket.objects.get(id=id)
        form = TicketForm(instance=t)
        return render(request, "index.html", {'form': form, 'action': "/", "source": "update", "id":id})


class MyLogin(View):
    def get(self, request):
        form = UserForm()
        return render(request, "login.html", {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "invalid.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("/login/")
