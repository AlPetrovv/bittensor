from drf_spectacular import views

from django.urls import path

urlpatterns = [
    path("api/schema/v1/", views.SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/v1/swagger-ui/",
        views.SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
