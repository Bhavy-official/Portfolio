from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .form import ContactForm

def home(request):
    form = ContactForm()
    form_submitted = False
    form_disabled = False

    if request.method == 'POST':
        # If you want to disable the form submission, set form_disabled to True
        form_disabled = True
        
        if not form_disabled:
            form = ContactForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                subject = form.cleaned_data['subject']

                html_message = render_to_string('contact/email_form.html', {
                    'name': name,
                    'email': email,
                    'message': message,
                    'subject': subject,
                })

                from_email = 'noreply@bhavy.com'
                recipient_list = ['bhavyb1234@gmail.com']

                email_message = EmailMultiAlternatives(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=recipient_list,
                )
                email_message.attach_alternative(html_message, 'text/html')
                email_message.send(fail_silently=False)

                form_submitted = True
                return redirect(request.path + '?form_submitted=true')

    return render(request, 'home/home.html', {
        'form': form,
        'form_submitted': form_submitted,
        'form_disabled': form_disabled,  # Pass this variable to the template
    
    })
