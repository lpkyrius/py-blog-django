from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views # o . indica que vou importar do mesmo diretório o views.py

# Mapeando as urls
# ----------------
# este urls.py é referenciado no urls.py principal
# Novamente, a cada linha, indico: quando abrirem o site/pagina...
# quero que direcione para o .urls do app x
# ----------------
# alterando para pegar a home do views - nomeio como blog-home...
# para não confundir com o home principal ou outros nas rotas
# na 1a indico que, se receber string vazia no parâmetro...
# direciono para views.home
# ----------------
# path('post/<pint:pk>', PostDetailView.as_view() assim posso enviar
# a primarykey do post como variável montando uma rota e enviando
# a pk para a View

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]


# blog/post_list.html
# <app>/<model>_<viewtype>.html
