from rest_framework import routers
from appa.views import *

router = routers.SimpleRouter()
router.register(r'address', AddressViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)
urlpatterns = router.urls