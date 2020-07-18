from django.contrib.messages.views import  SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course, ProfileModel, CustomUserModel, EnroledCourseModel
# Create your views here.
from .forms import CustomUserCreationForm,AddCourseForm,EnroldModelForm


class SignUpVeiw(CreateView,SuccessMessageMixin):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'courses/studentssignup.html'
    success_message = 'welcome, Now you can login'


class CoursesListView(ListView):
    model = Course
    template_name = 'home.html'
    context_object_name = 'courses'

# def course_list(request):
#     course = Course.objects.all()
#     print(course)
#     return render(request, 'home.html', {'courses': course})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/coursedetail.html'
    redirect_url = reverse_lazy('home')
    redirect_field_name = 'login'
    context_object_name = 'users_list'
    ordering = ['-id']


# ________________ admin actions-------------------
class AdminHome(TemplateView):
    template_name = 'adminhome.html'


class CreateNewCourse(CreateView,LoginRequiredMixin,SuccessMessageMixin):
    model = Course
    form_class = AddCourseForm
    template_name = 'courses/newcourse.html'
    success_url = reverse_lazy('course_list_view')
    success_message = 'New course is added'
    login_url = 'login'
    redirect_field_name = 'login'


class CourseList(ListView,LoginRequiredMixin):
    model = Course
    template_name = 'courses/course_list.html'
    login_url = 'login'
    redirect_field_name = 'login'


class CourseUpdate(UpdateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'updatecourse.html'
    success_url = reverse_lazy('course_list_view')
    login_url='login'
    redirect_field_name='login'


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'coursedelete.html'
    success_url = reverse_lazy('course_list_view')
    login_url = 'login'
    redirect_field_name = 'login'



class ProfileView(ListView,LoginRequiredMixin):
     model = ProfileModel
     template_name = 'courses/profilemodel_list.html'
     login_url = 'login'
     redirect_field_name = 'login'

     class DeleteUserView(LoginRequiredMixin, DeleteView):
         model = CustomUserModel
         template_name = 'adminhome.html'
         success_url = reverse_lazy('adminhome')
         login_url = 'login'
         redirect_field_name = 'login'

     class Enroll(LoginRequiredMixin, CreateView):
         model = EnroledCourseModel
         form_class = EnroldModelForm
         template_name = 'courses/profilemodel_list.html'
         success_url = 'profile'


     def enroledcourse(request):
         objects = EnroledCourseModel.objects.filter()
         for x in objects:
             print(x)
         return render(request, 'adminhome.html', {'objects': objects})