from django.conf.urls import url

from posts import views

urlpatterns = [
    url(r'^perfil/$',
        views.PerfilList.as_view(),
        name=views.PerfilList.name),
    url(r'^perfil/(?P<pk>[0-9]+)/$',
        views.PerfilDetail.as_view(),
        name=views.PerfilDetail.name),
    url(r'^post/$',
        views.PostList.as_view(),
        name=views.PostList.name),
    url(r'^post/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(),
        name=views.PostDetail.name),
    url(r'^comment/$',
        views.CommentList.as_view(),
        name=views.CommentList.name),
    url(r'^comment/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(),
        name=views.CommentDetail.name),
    url(r'^user/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^user/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]