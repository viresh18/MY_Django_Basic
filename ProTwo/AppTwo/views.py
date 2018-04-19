from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request, 'AppTwo/index.html')


def help(request):
    helpdic = {'help_insert': 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context=helpdic)


# def user(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {"users_record": user_list}
#     return render(request, 'AppTwo/users.html', context=user_dict)

def user(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")
    return render(request, 'AppTwo/users.html', {'form': form})
