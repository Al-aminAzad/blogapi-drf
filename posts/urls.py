from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostList, PostDetail, PostViewSet, UserDetail, UserList, UserViewSets

router = SimpleRouter()

router.register("users", UserViewSets, basename="users")
router.register("posts", PostViewSet, basename="posts")

# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path("", PostList.as_view(), name="post_list"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
# ]

urlpatterns = router.urls
