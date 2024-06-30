from django.shortcuts import render, redirect
from .forms import TeacherLoginForm

def teacher_login(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            # Handle teacher login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate and redirect as needed
            return redirect('index')  # Redirect to a success page or dashboard
    else:
        form = TeacherLoginForm()
    return render(request, 'teacher_login.html', {'form': form})
