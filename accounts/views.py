from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/registration.html', {'form': form})


# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'accounts/profile.html', args)
#
#
# @transaction.atomic
# def edit_profile(request):
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, instance=request.user)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('accounts:profile')
#     else:
#         profile_form = ProfileForm(instance=request.user)
#         return render(request, 'accounts/edit-profile.html', {'profile_form': profile_form})


class ProfileUpdate(UpdateView):
    # fields = ['avatar', 'gender', 'phone_number', 'alt_phone', 'address', 'zip_code', 'town', 'region']
    form_class = ProfileForm
    template_name = 'accounts/edit-profile.html'
    success_url = reverse_lazy('accounts:my-profile')

    def get_object(self):
        return self.request.user.profile


class MyProfile(DetailView):

    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user.profile
