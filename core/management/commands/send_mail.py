from decouple import config
from django.core.mail import send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "This is send test mail command"

    def handle(self, *args, **options):
        print("Start")

        send_mail(
            'Salamlar',
            'Bu mail sadece yoxlama meqsedil ile gonderilmishdir.',
            config('EMAIL_HOST_USER'),
            ['elxjd.2014@gmail.com'],
            fail_silently=False,
        )
        print("DONE")
