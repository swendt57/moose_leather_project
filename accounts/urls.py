from django.urls import path, include
from accounts.views import logout, login, register, user_profile, change_password

urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='profile'),
    path('change_password/', change_password, name='change_password'),  # use this one if the user is authenticated

    path('', include('django.contrib.auth.urls')),  # used for password resetting if the user forgets their password
]

# The auth.urls included are:
# password_reset
# password_reset/done
# reset/<uid>/<token>
# reset/done
