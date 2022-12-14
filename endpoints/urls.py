from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import PredictView
from .views import (EndpointViewSet, MLAlgorithmViewSet,
                    MLAlgorithmStatusViewSet, MLRequestViewSet)

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoinds", EndpointViewSet, basename='endpoints')
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename='mlalgorithms')
router.register(r'mlalgorithmstatuses', MLAlgorithmStatusViewSet, basename='mlalgorithmstatuses')
router.register(r'mlrequests', MLRequestViewSet, basename='mlrequests')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    #add predict url
    url(
        r'^api/v1/(?P<endpoint_name>.+)/predict$', PredictView.as_view(), name='predict'
    ),
]
