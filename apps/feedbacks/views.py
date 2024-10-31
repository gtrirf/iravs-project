import time
from django.shortcuts import render, redirect
from .models import Feedbacks
from .forms import FeedbackForm
from django.views import View
from django.utils import timezone
from django.contrib import messages


class FeedbackView(View):

    def get(self, request):
        last_feedback_time = request.session.get('last_feedback_time')
        if last_feedback_time:
            elapsed_time = time.time() - last_feedback_time
            if elapsed_time < 300:
                messages.error(request, 'You can only submit feedback once every 5 minutes.')
                return redirect('about')

        feedback_form = FeedbackForm()
        context = {
            'feedback_form': feedback_form
        }
        return render(request, 'feedbacks/feedback_create.html', context=context)

    def post(self, request):
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            request.session['last_feedback_time'] = time.time()
            return redirect('about')
        else:
            context = {
                'feedback_form': feedback_form
            }
            return render(request, 'feedbacks/feedback_create.html', context=context)
