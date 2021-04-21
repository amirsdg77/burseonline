from django.urls import path
from .views import add_blog, blog_page, add_blog_category, news, LatestNews, add_comment, EducationView, education_page\
    , add_edu, add_edu_comment

urlpatterns = [
    path('education', EducationView.as_view()),
    path('education/<int:pk>', education_page, name='education-page'),
    path('education/add_edu', add_edu),
    path('education/add_comment/<int:pk>', add_edu_comment, name='add-edu-comment'),
    path('blog', LatestNews.as_view()),
    path('blog/add_blog', add_blog),
    path('blog/<int:pk>', blog_page, name='blog-page'),
    path('blog/add_blog_category', add_blog_category),
    # path('blog/add_comment', AddComment.as_view(), name='add-comment')
    path('blog/add_comment/<int:pk>', add_comment, name='add-comment')

]