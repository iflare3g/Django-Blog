from django.conf.urls import url
from . import views as post_views
from django.views.generic import ListView,DetailView
from .models import Post

# lista dei post
# post singoli del blog 
# sezione contatti

urlpatterns = [
    url(r'^$',ListView.as_view(
        queryset = Post.objects.all().order_by('-date'), # ordine decrescente
        template_name = 'lista_post.html',
        paginate_by = 5
        ),name = "all"),
    
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$',DetailView.as_view(
        model = Post,
        template_name = 'singolo.html'
        ),name = "single"),
    url(r'^contacts/$',post_views.contacts,name = "contacts"),
]
