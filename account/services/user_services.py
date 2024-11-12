<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from account.token import user_tokenizer_generate


def send_verification_email(user, request):
    """Sends a verification email to the user."""
    subject = 'Activate your account'
    message = render_to_string('account/email-verification/email-verification.html', {
        'user': user,
        'domain': request.get_host(),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': user_tokenizer_generate.make_token(user),
    })
<<<<<<< Updated upstream
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
=======
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
>>>>>>> Stashed changes
