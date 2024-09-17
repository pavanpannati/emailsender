from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EmailForm
# Create your views here.

def send_email(request):
    if request.method=='POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            recipient=form.cleaned_data['recipient']
            send_mail(subject,message,'pavan@gmail.com',[recipient])
            return redirect('emailsent')
    else:
        form=EmailForm()
    return render(request,'email_app/send_email.html',{'form': form})

def email_sent(request):
    return render(request,'email_app/email_sent.html')