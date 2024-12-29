from rest_framework.routers import SimpleRouter

from .handlers import SubnetViewSet

subnet_router = SimpleRouter()
subnet_router.register("subnets", SubnetViewSet)
