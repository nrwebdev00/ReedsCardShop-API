from django.urls import path
from user import views


app_name = 'user'


urlpatterns = [
    # User urls Public
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('create_collector/', views.CreateCollectorView.as_view(), name='create_collector'),
    path('create_seller/', views.CreateSellerView.as_view(), name='create_seller'),

    # User Token Urls
    path('login/', views.CreateTokenView.as_view(), name='login'),
]