from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('companyclick', views.teacherclick_view),
path('companylogin', LoginView.as_view(template_name='company/companylogin.html'),name='companylogin'),
path('companysignup', views.teacher_signup_view,name='companysignup'),
path('company-dashboard', views.teacher_dashboard_view,name='company-dashboard'),
path('company-exam', views.teacher_exam_view,name='company-exam'),
path('company-add-exam', views.teacher_add_exam_view,name='company-add-exam'),
path('company-view-exam', views.teacher_view_exam_view,name='company-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('company-question', views.teacher_question_view,name='company-question'),
path('company-add-question', views.teacher_add_question_view,name='company-add-question'),
path('company-view-question', views.teacher_view_question_view,name='company-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]