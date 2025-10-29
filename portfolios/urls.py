from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet, basename='portfolio')

urlpatterns = router.urls
