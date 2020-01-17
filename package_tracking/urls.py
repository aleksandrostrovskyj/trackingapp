from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PackageViewSet

package_list = PackageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

package_detail = PackageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',

})

urlpatterns = [
    path('list', package_list),
    path('<int:pk>', package_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)