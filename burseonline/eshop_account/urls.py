from django.urls import path

from .views import login_user, register, log_out, user_account_main_page, edit_user_profile, add_product\
    , PurchasedProductsList, PurchasedProduct, PurchasedProductVideo, support, consulting_request,\
    factor, my_answers, my_questions, consultation_request, add_ticket, change_password, forum_question,\
    ForumView, q_a, answer, view_ticket, forum

from eshop_order.views import wallet

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register),
    path('log-out', log_out),

    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),
    path('user/change_password', change_password),
    path('user/support', support),
    path('user/support/<int:pk>', view_ticket, name="view-ticket"),
    path('user/add_ticket', add_ticket),
    path('user/consulting_request', consulting_request),
    path('user/factor', factor),
    path('user/my-answers', my_answers),
    path('user/my-questions', my_questions),
    path('user/consultation_request', consultation_request),
    path('user/wallet', wallet),
    path('user/question', q_a),

    path('user/add_product', add_product),
    path('user/products', PurchasedProductsList.as_view()),
    path('user/products/<int:pk>', PurchasedProduct.as_view(), name="show-product"),
    path('user/products/product/<int:pk>', PurchasedProductVideo.as_view(), name="show-product-video"),

    path('forum', ForumView.as_view()),
    path('forum/category/<int:pk>', forum, name="forum-category"),
    path('forum/<int:pk>', forum_question, name="show-question"),
    path('forum/answer/<int:pk>', answer, name='answer'),
]
