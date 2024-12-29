from .auth_users.urls import urlpatterns as auth_user_urlpatterns
from .chats.urls import urlpatterns as chat_urlpatterns
from .subnets.urls import urlpatterns as subnet_urlpatterns

urlpatterns = [
    *chat_urlpatterns,
    *subnet_urlpatterns,
    *auth_user_urlpatterns,
]
