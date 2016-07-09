from django.shortcuts import render


def join_my_newsletter(request):
    context = {}
    return render(request, 'join_my_newsletter.html', context)
