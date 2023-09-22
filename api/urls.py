
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import CityViewSet , UserViewSet , OutletAssignmentViewSet , AttendenceViewSet , FormFieldViewSet

router = DefaultRouter()
router.register(r'city' , CityViewSet , basename='city')

userRouter = DefaultRouter()
userRouter.register(r'user' ,UserViewSet , basename='user' )

outletAssignrouter = DefaultRouter()
outletAssignrouter.register(r'outlet-assignments', OutletAssignmentViewSet)

attendenceRouter = DefaultRouter()
attendenceRouter.register(r'attendence' , AttendenceViewSet , basename='attendence')

formFieldRouter = DefaultRouter()
formFieldRouter.register(r'formField' ,FormFieldViewSet,basename='formField' )


urlpatterns = [
    path('' , include(router.urls)),
    path('' , include(userRouter.urls)),
    path('', include(outletAssignrouter.urls)),
    path('' , include(attendenceRouter.urls)),
    path('' , include(formFieldRouter.urls)),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
