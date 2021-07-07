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
    path('board/create', views.CreateBoardView.as_view(), name='board_create'),
    path('board/', views.IndexBoardView.as_view(), name='board_view'),
    #path('board/<int:pk>/edit', views.EditBoardView.as_view(), name='board_edit'),
    #path('board/<int:pk>/delete', views.DeleteBoardView.as_view(), name='board_delete'),

]
