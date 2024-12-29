from django.urls import include
from django.urls import path

from .routers import subnet_router

urlpatterns = [
    path("", include((subnet_router.urls, "subnets"), namespace="subnet")),
]
