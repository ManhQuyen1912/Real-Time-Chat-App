from django.shortcuts import render,redirect

def ChatPage(request, *args, **kwargs):
    if not request.user.id_authenticated:
        return redirect("login-user")
    context = {}
    return render (request, "chat/chatPage.html",context)
