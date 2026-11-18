from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import LoginForm, SignupForm


@user_passes_test(lambda user: user.is_superuser, login_url='admin:login')
def user_signup(request):
    if request.method == 'POST':
        if (form := SignupForm(request.POST)).is_valid():
            user = form.save()
            user.is_staff = True
            user.save(update_fields=['is_staff'])
            return redirect('admin:index')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

@require_POST
def user_logout(request):
    logout(request)
    return redirect('admin:index')

def user_login(request):
    FALLBACK_REDIRECT = 'admin:index'

    if request.user.is_authenticated:
        return redirect(FALLBACK_REDIRECT)
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(request, username=username, password=password):
                if not user.is_staff:
                    form.add_error(None, 'Esta cuenta no tiene acceso a la intranet.')
                    return render(request, 'accounts/login.html', {'form': form})

                login(request, user)

                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and url_has_allowed_host_and_scheme(
                    next_url,
                    allowed_hosts={request.get_host()},
                    require_https=request.is_secure(),
                ):
                    return redirect(next_url)
                return redirect(FALLBACK_REDIRECT)

            else:
                form.add_error(None, 'Incorrect username or password.')

    else:
        form = LoginForm()
    return render( request, 'accounts/login.html', {'form': form})
