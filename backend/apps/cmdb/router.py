from rest_framework.routers import DefaultRouter
from . import views


cmdbRouter = DefaultRouter()
cmdbRouter.register(r'serverInfo', views.serverInfoView, basename="serverInfo")
cmdbRouter.register(r'cmdbCeleryTaskResult', views.celerytaskresultView, basename="cmdbCeleryTaskResult")
cmdbRouter.register(r'cmdbFlushCmdb', views.flushcmdbView, basename="cmdbFlushCmdb")
