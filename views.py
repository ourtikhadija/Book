from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required

# View for sign-up
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required
def account_view(request):
    return render(request, 'accounts/account.html')