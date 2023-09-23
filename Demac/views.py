from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, 'main/creating.html', status=404)