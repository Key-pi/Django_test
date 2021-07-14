from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.person, name='person'),
    path('person/<int:pk>/', views.person_update, name='person_update'),
    path('board/', views.BoardListView.as_view(), name='board_view'),
    path('board/<int:pk>/', views.BoardInfoView.as_view(), name='board_info'),
    path('board/update/<int:pk>/', views.BoardUpdateView.as_view(), name='board_update'),
    path('board/delete/<int:pk>/', views.BoardDeleteView.as_view(), name='board_delete'),
    path('board/create/', views.BoardCreate.as_view(), name='board_create'),
]
