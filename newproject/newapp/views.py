from django.forms import forms
from django.views.generic.list import ListView
from .models import Student
from django.views.generic.detail import DetailView
from .forms import ContactForm
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


# List view
class StuListView(ListView):
    model = Student
    # template_name_suffix ='_data'
    ordering = ['name']
    template_name = 'newapp/student.html'
    context_object_name = 'object'
    '''custom object name = object, by default-student_data'''

    def get_queryset(self):
        # return Student.objects.filter(course='english')
        return Student.objects.all()

    # custom context object name...
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context


# when user cookie set then this method is override..
# def get_template_names(self):
#     if self.request.COOKIES['user'] =='raj':
#         template_name = 'newapp/raj.html'
#     else:
#         template_name = self.template_name
#     return [template_name]

# Detail view
class StuDetailView(DetailView):
    model = Student
    template_name = 'newapp/student1.html'
    context_object_name = 'obj'


# form-view
class ContactFormView(FormView):
    template_name = 'newapp/contact.html'
    form_class = ContactForm
    success_url = '/student/'

    def form_valid(self, form):
        # print(form.cleaned_data) #check form data check in terminal
        return super().form_valid(form)

# create-view
class StudentCreateView(CreateView):
    template_name = 'newapp/create.html'
    model = Student
    fields = ['name', 'roll', 'course']
    success_url = '/student/'

# update-view
class StudentUpdateView(UpdateView):
    model = Student
    success_url = '/student/'
    fields = ['name', 'roll', 'course']
    template_name = 'newapp/update.html'

# delete-view
class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'
    template_name = 'newapp/delete.html'
