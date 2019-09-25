from django.urls import path
from django.views.generic.detail import DetailView


from .views import *
from .models import clip

app_name = 'clip'

urlpatterns = [
    path('',clip_list, name='clip_list'),
    path('gallary/',clip_gallary, name='clip_gallary'),
    path('detail/<int:pk>/', DetailView.as_view(model=clip,template_name='clip/detail.html'), name='clip_detail'),
    path('upload/', clip_new, name='clip_new'),
    path('clip/tags/<tag>', clip_list, name='clip_search'),
#    path('delete/<int:pk>/', ClipDeleteView.as_view(), name='clip_delete'),
    path('update/<int:pk>/', ClipUpdateView.as_view(), name='clip_update'),
    
]
# 함수형 뷰는 뷰이름만 써주고
# 클래스형 뷰는 .as_view()붙이기
# app_name은 네임 스페이스 템플릿에서 url 템플릿 태그사용할때 app_name : URL패턴이름으로 사용
#
