from config.urls import path
from main.apps import MainConfig
from main.views import ChainApiView, ChainCreateApi

app_name = MainConfig.name

urlpatterns = [
    path("list/", ChainApiView.as_view(), name="chain_list"),
    path("create/", ChainCreateApi.as_view(), name="chain_create"),
]
