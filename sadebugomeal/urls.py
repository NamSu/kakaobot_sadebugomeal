from django.conf.urls import url
from . import views

# 카카오 플러스 친구에서 요구하는 ~/keyboard/, ~/message에 반응
# fail 415 에러시에만 수정.
urlpatterns = [
        url(r'^keyboard/', views.keyboard),
        url(r'^keyboard', views.keyboard),
        url(r'^message', views.message),
]
