from django.shortcuts import render
from .models import MainPage, Socials
from django.views import View


class MainPageView(View):
    def get(self, request):
        main_page = MainPage.objects.first()
        socials = Socials.objects.all()
        context = {
            'image': main_page.image,
            'full_name': main_page.full_name,
            'job': main_page.job,
            'body': main_page.body,
            'socials': socials,
        }
        return render(request, 'mainpage/main_page.html', context=context)
