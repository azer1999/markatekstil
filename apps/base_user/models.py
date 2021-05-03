from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('İstifadəçi adı'),
        max_length=150,
        unique=True,
        help_text=_('Tələb olunur. 150 simvol və ya daha az. Yalnız hərflər, rəqəmlər və @ /. / + / - / _.'),
        error_messages={
            'unique': _("Bu istifadəçi adli istifadəçi artıq mövcuddur."),
        }
    )
    first_name = models.CharField(_('Ad'), max_length=30)
    last_name = models.CharField(_('Soyad'), max_length=150)
    birthdate = models.DateTimeField(_("Doğum Tarixi"), null=True, blank=True)
    email = models.EmailField(_('E-poçt'), unique=True, error_messages={
        'unique': _("Bu e-poçtu olan istifadəçi artıq mövcuddur."),
    })
    profile_photo = models.ImageField(_("Profil Şəkil *"), upload_to='profile_pic', default="default.jpg", null=True,
                                      blank=True)
    gender = models.CharField(_("Gender"), choices=(
        ("Male", _("Male")),
        ("Female", _("Female"))
    ), default="Male", max_length=30)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


User = MyUser()
