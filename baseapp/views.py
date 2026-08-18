# from django.shortcuts import render


# # Create your views here.

# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
#         # Handle message delivery or database saving here
#     return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def index(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # Validate that all required fields are present
        if name and email and subject and message:
            full_subject = f"Portfolio Contact: {subject} (from {name})"
            full_message = f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{message}"
            recipient_list = [settings.EMAIL_HOST_USER]  # Delivered to your inbox

            try:
                send_mail(
                    subject=full_subject,
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                messages.success(request, "Thank you! Your message has been sent successfully.")
            except Exception as e:
                messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
        else:
            messages.error(request, "Please fill out all fields before submitting.")

        return redirect('/#contact')

    return render(request, "index.html")