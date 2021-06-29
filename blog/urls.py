from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('qwefqgar72534455qw/', views.about_site, name='about_site'),
    path('wqg3354rqe436rgwe/', views.all_about_seals_and_site, name='all_about_seals_and_site'),
    path('werghw452436ethe56354/', views.edit, name='edit'),
    path('awefe4r62thrt/', views.flag, name='flag'),
    path('efqr64gg5474rrqw/', views.hello, name='hello'),
    path('ghejbkeb4574tth/', views.omg_seals, name='omg_seals'),
    path('ouebrthbw4t543t/', views.more_about_seals, name='more_about_seals'),
    path('jhthegbl354y4t/', views.txt, name='txt'),
    path('oubjbelrgery45lb/', views.your_profil, name='your_profil'),
    path('rgqiuh34tiyb4btb55hj/', views.some, name='some'),
    path('jk4tb3htyubyn/', views.wow, name='wow'),
    path('hsfgb4uiy5vitu/', views.one, name='1'),
    path('hrtbgubtg4/', views.two, name='2'),
    path('qerjghrnghb5utbiu/', views.three, name='3'),
    path('hbtgkbeghj5hj/', views.add, name='add'),
    path('jghb4uy5bb5oy4/', views.momomo, name='momomo'),
    path('bh5i8ygt3by5bgn/', views.cttttf, name='cttttf'),
    path('settings/', views.settings),
]
