"""DataLossPrev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import get_user_model


from DataListener.views import DSL
from django.urls import path
from DataListener.models import regexCombs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DSL/', DSL.as_view()),
]

# Since urls.py runs only once when the server starts, this is where
# we check if there is an entry in the regexCombs table. If the table 
# is empty we create a default entry
#Also default super user is created then the container spins up again
try:
    if not len(regexCombs.objects.all()):
        initEntry = regexCombs(regexName = 'Visa Debit Card',regexPattern='^4[0-9]{12}(?:[0-9]{3})?$')
        initEntry.save()
        print('No default')

    User = get_user_model()
    if not len(User.objects.all()):
        User.objects.create_superuser('root', 'test@test.com', 'password')

except Exception as e:
    print(e)
    pass