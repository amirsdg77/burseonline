from django.urls import path
from .views import add_blog, blog_page, add_blog_category, LatestNews, add_comment, SearchBlogView

urlpatterns = [
    path('blog', LatestNews.as_view()),
    path('blog/search', SearchBlogView.as_view()),
    path('blog/add_blog', add_blog),
    path('blog/<int:pk>', blog_page, name='blog-page'),
    path('blog/add_blog_category', add_blog_category),
    # path('blog/add_comment', AddComment.as_view(), name='add-comment')
    path('blog/add_comment/<int:pk>', add_comment, name='add-comment')

]