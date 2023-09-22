from django.urls import path
from .views import login_view ,dash , logout_user ,upbeatPlan,updateFields,delete_data,updateActivity,outActivity,assign_outlet, area ,areaReg,updateOutlet ,import_page ,export_data,import_data,update_city, userManage , register ,add_city , city , update_user, attendence , outlet , outReg,fields,fieldsReg,raw , outActivity


urlpatterns = [
    path('' , login_view, name= 'login'),
    path('logout/' , logout_user, name= 'logout'),
    path('register/' , register , name = 'register'),
    path('user/' , userManage , name = 'user'),
    path('update/<int:id>/', update_user, name='update'),
    path('import_page/', import_page, name='import_page'),
    path('import/', import_data, name='import_data'),
    path('export/', export_data, name='export_data'),
    path('city/' , city , name = 'city'),
    path('add_city/' , add_city, name = 'add_city'),
    path('update_city/<int:id>/' , update_city, name = 'update_city'),
    path('attendence/' , attendence, name = 'attendence'),
    path('outReg/' , outReg, name = 'outReg'),
    path('outlet/' , outlet, name = 'outlet'),
    path('updateOutlet/<int:id>/' , updateOutlet, name = 'updateOutlet'),
    path('area/' , area, name = 'area'),
    path('areaReg/' , areaReg, name = 'areaReg'),
    path('outActivity/' , outActivity, name = 'outActivity'),
    path('updateActivity/<int:id>/' , updateActivity, name = 'updateActivity'),
    path('fields/' , fields, name = 'fields'),
    path('fieldsReg/' , fieldsReg, name = 'fieldsReg'),
    path('updateField/<int:id>/' , updateFields, name = 'updateField'),
    path('dash/' ,dash , name= 'dash'),
    path('raw/' ,raw , name= 'raw'),
    path('upbeatPlan/' ,upbeatPlan , name= 'upbeatPlan'),
    path('<int:id>',delete_data, name='deletedata'),
    path('assign_outlet/<int:id>/' ,assign_outlet , name= 'assign'),
    # path('gptReport/' ,gptReport , name= 'gptReport'),
    # path('gpt/' ,gpt , name= 'gpt'),
    
  
]
