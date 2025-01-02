from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from account.infrastructure.tokens import user_tokenizer_generate


def send_verification_email(user, request):
    uidb64 = urlsafe_base64_encode(force_bytes(user.id))
    token = user_tokenizer_generate.make_token(user)

    verification_link = request.build_absolute_uri(
        reverse('account:email-verification', args=[uidb64, token])
    )
    subject = "Verify your email"
    message = f"Click the link to verify your email: {verification_link}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])



