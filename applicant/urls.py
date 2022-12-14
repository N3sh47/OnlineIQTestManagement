from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('applicantclick', views.studentclick_view),
path('applicantlogin', LoginView.as_view(template_name='applicant/applicantlogin.html'),name='applicantlogin'),
path('applicantsignup', views.student_signup_view,name='applicantsignup'),
path('applicant-dashboard', views.student_dashboard_view,name='applicant/applicant-dashboard'),
path('applicant-exam', views.student_exam_view,name='applicant-exam'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),

path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('applicant-marks', views.student_marks_view,name='applicant-marks'),
]