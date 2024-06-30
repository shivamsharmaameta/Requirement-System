from django.shortcuts import render,redirect
from .forms import StudentLoginForm

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            # Handle student login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate and redirect as needed
            return redirect('index')  # Redirect to a success page or dashboard
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})
