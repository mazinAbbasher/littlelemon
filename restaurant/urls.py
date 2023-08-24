from django.urls import path,include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.MenuItemsView.as_view(),name="bb"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]
