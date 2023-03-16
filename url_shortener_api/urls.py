from url_shortener_api.views import ShortenerUrlApiView, RetrieveUrlApiView, Redirector, GetUsersProfile
from django.urls import path
from url_shortener_api.views import MyTokenObtainPairView
urlpatterns = [
    path('user/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("user/profile/", GetUsersProfile.as_view()),
    path('short-url/', ShortenerUrlApiView.as_view()),
    path('short-url/<int:pk>/', RetrieveUrlApiView.as_view()),
    path('<str:shortener_link>/',Redirector.as_view())
]
 