from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ItemListCreateAPIView

urlpatterns = [
    # jwt urls implements
    path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     # OAuth2 URLs implements
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth2 URLs
]
