from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups == 'Applicant' :
                return redirect('home')

            else :
                return redirect('emphome')

        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed")
        return wrapper_func
    return decorator


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name

#         if group == 'applicant':
#             return redirect(to whatver we want)

#         if group =='employer':
#             return view_func(request, *args,**kwargs)
#     return wrapper_function