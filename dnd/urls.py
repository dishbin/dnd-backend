from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.CharacterList.as_view(), name='character_list'),
    path('characters/<int:pk>', views.CharacterDetail.as_view(), name='character_detail'),
]