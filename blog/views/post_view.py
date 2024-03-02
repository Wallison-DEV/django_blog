from django.views.generic import View
from django.shortcuts import render

class MyView(View):
    def get(self, request):
        return render(request, 'hello.html', {'name': 'Wallison'})
