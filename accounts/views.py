from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.utils.translation import activate

from .models import CustomUser


class SignUpView(CreateView):
    activate('uz')
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def profile(request):
    user = request.user
    user_info = CustomUser.objects.get(username=user.username)
    return render(request, 'UserProfile.html', {'user_info': user_info})
