"""Task Scheduling ans Sending mail's."""

# Django Rest
from rest_framework.response import Response

# Celery
from celery import shared_task

# Django
import logging
from django.core.mail import send_mail
from smtplib import (
    SMTPAuthenticationError,
    SMTPConnectError,
    SMTPDataError,
    SMTPException,
    SMTPNotSupportedError,
    SMTPRecipientsRefused,
    SMTPResponseException,
    SMTPSenderRefused,
)
from django.template.loader import render_to_string
from django.conf import settings
from django.http import BadHeaderError

logger = logging.getLogger(__name__)
logger = logging.getLogger("django")


@shared_task
def send_user_email(subject, message, emails):
    """Mail send function using celery."""
    subject = f"Marketing OTP For {subject}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = emails

    context = {"message": message}
    html_message = render_to_string("myuser/email_template.html", context)
    try:
        send_mail(
            subject=subject,
            message="",
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        logging.info("Mail send successfully to user's")
    except BadHeaderError:
        return Response({"error": "BadHeaderError"})
    except SMTPAuthenticationError:
        return Response({"error": "SMTPAuthenticationError"})
    except SMTPDataError:
        return Response({"error": "SMTPDataError"})
    except SMTPConnectError:
        return Response({"error": "SMTPConnectError"})
    except SMTPRecipientsRefused:
        return Response({"error": "SMTPRecipientsRefused"})
    except SMTPSenderRefused:
        return Response({"error": "SMTPSenderRefused"})
    except SMTPNotSupportedError:
        return Response({"error": "SMTPNotSupportedError"})
    except SMTPResponseException:
        return Response({"error": "SMTPResponseException"})
    except SMTPException:
        return Response({"error": "SMTPException"})
