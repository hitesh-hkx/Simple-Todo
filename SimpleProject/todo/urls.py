from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post',views.TodoViewSets,base_name='Post')
router.register(r'acc',views.UserRegViewSets,base_name='Reg')


urlpatterns = [
    path('',views.index,name="index"),
    path(r'complete/<todo_id>',views.complete,name="complete"),
    path(r'add',views.add,name="add"),
    path(r'delete_completed',views.delete_completed,name="delete_completed"),
    path(r'del_all',views.del_all,name="del_all")
]


urlpatterns += router.urls
