from rest_framework import routers
from details.views import ContactViewSet
router = routers.SimpleRouter()

router.register(r'', ContactViewSet)