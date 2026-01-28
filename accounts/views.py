from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from forum.models import ForumPost

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    my_posts = ForumPost.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'accounts/profile.html', {
        'my_posts': my_posts
    })