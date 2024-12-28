# ****** Authenticated *******
from django.shortcuts import  redirect
def auth(view_function):
    def wrapped_view(request,*args,**kargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kargs)
    return wrapped_view
    
#guest  user


def guest(view_function):
    def wrapped_view(request,*args,**kargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request, *args, **kargs)
    return wrapped_view
    

        