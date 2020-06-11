from django.urls import path, re_path, include
from rest_auth.views import PasswordResetConfirmView

# from accounts import views as accounts_views

# from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    # path('add/', accounts_views.register_user, name='add'),
    #
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #
    # path('reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',
    #                                                     email_template_name='password_reset_email.html',
    #                                                     subject_template_name='password_reset_subject.txt'),
    #      name='password-reset'),
    #
    # path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
    #      name='password-reset-done'),
    #
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
    #         name='password-reset-confirm'),
    #
    # path('reset/complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    #      name='password-reset-complete'),
    #
    # path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
    #      name='password-change'),
    #
    # path('settings/password/done/',
    #      auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
    #      name='password-change-done'),
    #
    # # path('profile/', accounts_views.view_profile, name='profile'),
    # #
    # # path('profile/edit/', accounts_views.edit_profile, name='edit_profile'),
    #
    # path('profile/', accounts_views.MyProfile.as_view(), name='my-profile'),
    # path('profile/edit/', accounts_views.ProfileUpdate.as_view(), name='edit-profile'),
    path('', include('rest_auth.urls')),

    path('register/', include('rest_auth.registration.urls')),

    re_path(
        r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),

]
