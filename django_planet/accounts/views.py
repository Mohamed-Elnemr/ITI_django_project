from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    current_user = request.user

    if request.user.is_authenticated():
        if request.user.is_staff:
            # user is an admin
            return redirect("/admin/")
        else:
            context = {'current_user': current_user}
            #return render(request, 'user_templates/profile.html', context)
            return redirect("/users/profile")
            # return redirect("/users/profile/"+current_user.id)
    else:
        return redirect("/accounts/login")