from django.urls import path
from .views import StudentList, StudentDetail,UserBookListView

urlpatterns = [  
    path('', StudentList.as_view()),                
    path('<int:pk>', StudentDetail.as_view()),
    path('my', UserBookListView.as_view()),
    
]