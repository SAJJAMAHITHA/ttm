from django.contrib import admin
from django.urls import path
from.views import*

urlpatterns = [
   # path('admin/', admin.site.urls),
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('card/',travelpackage,name='travelpackage'),
    path("p/",print_to_console,name='print_to_console'),
    path("print1/",print1,name="print1"),
    path('ran1/', ran, name='ran'),
    path('ran/', random123, name='random123'),
    path('date/',get_date,name='get_date'),
    path('date1/',getdate1,name="getdate1"),
    path('timezfnccall/',timezfnccall,name='timezfnccall'),
    path('f/',registerloginfunction,name='registerloginfunction'),
    path('data/',registerfunctioncall,name='registerunctioncall'),
    path('m/',piechart,name='piecart'),
    path('n/',pie_chart,name='pie_chart'),
    path('q/',image,name='image'),
    path('page/',weatherpagecall,name='weatherpagecall'),
    path('z/',weatherlogic,name='weatherlogic'),
    path('login/',login,name="login"),
    path('signup/',singup,name="signup"),
    path('login1/',login1,name="login1"),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contactmail/',contactmail,name="contactmail"),
    path('contactmail1/',contactmail1,name="contactmail1"),








]