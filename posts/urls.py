from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostList, PostDetail, PostViewSet, UserDetail, UserList, UserViewSet

router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path("", PostList.as_view(), name="post_list"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
# ]

urlpatterns = router.urls
