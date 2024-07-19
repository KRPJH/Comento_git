from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')  # 'accounts:login'을 사용하여 네임스페이스를 지정
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
