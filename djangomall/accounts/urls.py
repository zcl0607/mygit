from django.conf.urls import re_path

from accounts import views

urlpatterns = [
    # 用户登录
    re_path(r'^user/login/$', views.user_login, name='user_login'),
    # 用户退出
    re_path(r'^user/logout/$', views.user_logout, name='user_logout'),
    # 用户注册
    re_path(r'^user/register/$', views.user_register, name='user_register'),
    re_path(r'^yanz/$', views.email_code, name='email_code'),

    # 地址列表
    re_path(r'^user/address/list/$', views.address_list, name='address_list'),
    # 地址的修改和编辑
    # user/address/edit/add/   user/address/edit/12/
    re_path(r'^user/address/edit/(?P<pk>\S+)/$', views.address_edit, name='address_edit'),
    re_path(r'^user/address/delete/(?P<pk>\d+)/$', views.address_delete, name='address_delete'),

]