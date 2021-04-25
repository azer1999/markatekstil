from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_mail_notify_task(to_mail,instance,template):
    subject = "New Contact"
    from_email = "info@.com"
    html_content = render_to_string(f'Mail/{template}.html',
                                    {'instance': instance
                                     })
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_mail])
    msg.attach_alternative(html_content, "text/html")
    msg.send()