from django.urls import path
from .views import complaint_detail, complaint_list, user_complaints


urlpatterns = [
    path("", complaint_list),
    path("my/", user_complaints, name='user-complaints'),
    path("<int:pk>/", complaint_detail, name='complaint-detail'),
]