from django.urls import path
from .views import home, about, blog_single, contact, category, tags, blog, search, comment_create

urlpatterns = [
    path('', home),
    path('about/', about, name="about"),
    path('blog-single/<int:pk>/', blog_single),
    path('contact/', contact, name="contact"),
    path('category/', category, name="category"),
    path('category/<str:name>', category),
    path('tags/<str:tags>' , tags ),
    path('tags/', tags),
    path('search/' , search),
    path('comment/<int:pk>' , comment_create)
]
