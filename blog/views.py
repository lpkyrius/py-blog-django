from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

#from django.http import HttpResponse

# se chamam home, retorno uma HttpResponse com o código html
def home(request):

    # return HttpResponse('<h1>Blog Home</h1>')
    # passo a utilizar o render com 2 args:
        # a solicitação
        # o nome do template com diretório
        # context to fill the page

   # context dictionary
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html no lugar de # blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # -nomedocampo o traço, indica que desejo em ordem decrescente, invertendo a query
    paginate_by = 5 #para paginar os posts



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html no lugar de # blog/post_list.html
    context_object_name = 'posts'
    # a ordenação abaixo foi transferida para a linha final da get_query_set()
    # ordering = ['-date_posted'] # -nomedocampo o traço, indica que desejo em ordem decrescente, invertendo a query
    paginate_by = 5 #para paginar os posts

    # sobrescrevendo o método para poder filtrar o user
    def get_queryset(self):
        # get_object_or_404 retornará o user e já faz o tratamento caso não tenha user, o que retornaria um erro 404
        user = get_object_or_404(User, username=self.kwargs.get('username')) # kwargs são os parâmetros
        # retorno o filtro pelo usuário, ordenado por data decrescente
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # se quiser que retorne à home após criar é só deixar um atributo conforme abaixo:
    # success_url = '/'

    # para sobrepor a função de validação default
    def form_valid(self, form):
        # pega a instância do form de inclusão de post e alimenta o author com o user logado
        # agora, quando salvar o post, já terá o campo author alimentado
        form.instance.author = self.request.user
        return super().form_valid(form)



# exigir que estaja logado = LoginRequiredMixin
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # para verificar se o autor está editando um post próprio
    def test_func(self):
        post = self.get_object() # post que estou tentando editar
        if self.request.user == post.author:
            return True # libera se for do mesmo autor
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # para verificar se o autor está editando um post próprio
    def test_func(self):
        post = self.get_object() # post que estou tentando editar
        if self.request.user == post.author:
            return True # libera se for do mesmo autor
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
