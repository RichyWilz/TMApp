from django.core.mail import EmailMessage
from django.conf import settings

def send_email_task(subject, email_address, message):
    """Sends an email when the feedback form has been submitted."""
    # sleep(20)  # Simulate expensive operation(s) that freeze Django
   
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email_address],
    )
    email.reply_to = settings.EMAIL_HOST_USER
    email.send(fail_silently=False)