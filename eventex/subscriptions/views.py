# coding: utf-8
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.is_valid()
        obj = Subscription(**form.cleaned_data)
        obj.save()
        return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
    else:
        return render(request,'subscriptions/subscription_form.html', {'form': SubscriptionForm()})