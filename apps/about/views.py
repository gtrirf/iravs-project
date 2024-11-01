from django.shortcuts import render
from django.views import View
from .models import About
from django.utils.translation import get_language


class AboutView(View):
    def get(self, request):
        lang = get_language()
        about_section = About.objects.all().order_by('order')
        context = {
            'about_section': about_section,
            'lang': lang
        }
        return render(request, 'about/about.html', context=context)
