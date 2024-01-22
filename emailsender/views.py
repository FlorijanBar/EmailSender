from django.shortcuts import render, redirect
from emailsend.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contect=form.cleaned_data['contect']
            html=render_to_string('contactform.html',{'name':name,'email':email,'contect':contect})
            send_mail('Contact form','This is message','noreply@florijan.com',['testemailflorijan@gmail.com'],html_message=html)
            return redirect('index')
        else:
            form=ContactForm()
    context={'form':form}
    return render(request, 'index.html',context)