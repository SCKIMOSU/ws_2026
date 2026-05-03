from django.urls import path

from . import views


app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/pybo/
    path('<int:question_id>/', views.detail, name='detail'), # 127.0.0.1:8000/pybo/2/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

    path('question/create', views.question_create, name='question_create'),

]

# app_name = 'question'
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
# ]
