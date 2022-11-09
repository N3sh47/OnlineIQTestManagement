from django.urls import path,include
from django.contrib import admin
from quiz import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('company/',include('teacher.urls')),
    path('applicant/',include('student.urls')),
    


    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='quiz/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),



    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='quiz/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-company', views.admin_teacher_view,name='admin-company'),
    path('admin-view-company', views.admin_view_teacher_view,name='admin-view-company'),
    path('update-company/<int:pk>', views.update_teacher_view,name='update-company'),
    path('delete-company/<int:pk>', views.delete_teacher_view,name='delete-company'),
    path('admin-view-pending-company', views.admin_view_pending_teacher_view,name='admin-view-pending-company'),
    path('admin-view-company-salary', views.admin_view_teacher_salary_view,name='admin-view-company-salary'),
    path('approve-company/<int:pk>', views.approve_teacher_view,name='approve-company'),
    path('reject-company/<int:pk>', views.reject_teacher_view,name='reject-company'),

    path('admin-applicant', views.admin_student_view,name='admin-applicant'),
    path('admin-view-applicant', views.admin_view_student_view,name='admin-view-applicant'),
    path('admin-view-applicant-marks', views.admin_view_student_marks_view,name='admin-view-applicant-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-applicant/<int:pk>', views.update_student_view,name='update-applicant'),
    path('delete-applicant/<int:pk>', views.delete_student_view,name='delete-applicant'),

    path('admin-field', views.admin_course_view,name='admin-field'),
    path('admin-add-field', views.admin_add_course_view,name='admin-add-field'),
    path('admin-view-field', views.admin_view_course_view,name='admin-view-field'),
    path('delete-field/<int:pk>', views.delete_course_view,name='delete-field'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>', views.view_question_view,name='view-question'),
    path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),


]
