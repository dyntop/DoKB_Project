from django.urls import path

from . import views
app_name = "predict"
urlpatterns = [
    path('', views.index, name='index'),
    #path(여기다 넣은 번호는 id로 쓰일거다, 이 로직으로 호출되면 view의 detil을 호출해라, 이름)
    path('<int:Client_id>/', views.detail, name='detail'),
    path('<int:Client_id>/results/', views.result, name='result'),
    path('<int:Client_id>/pred/', views.pred, name='pred'),
]