from config.urls import path
from main.apps import MainConfig
from main.views import ChainApiView, ChainCreateApi, ChainUpdateApiView, ChainRetrieveApiView, ChainDestroyApiView

app_name = MainConfig.name

urlpatterns = [
    path("list/", ChainApiView.as_view(), name="chain_list"),
    path("create/", ChainCreateApi.as_view(), name="chain_create"),
    path("update/<int:pk>/", ChainUpdateApiView.as_view(), name="chain_update"),
    path("retrieve/<int:pk>/", ChainRetrieveApiView.as_view(), name="chain_retrieve"),
    path("destroy/<int:pk>/", ChainDestroyApiView.as_view(), name="chain_destroy"),
]
