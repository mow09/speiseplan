from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class DUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth=None, first_name=None, last_name=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class DUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Emailadresse',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(verbose_name='Vorname', max_length=127, blank=True, null=True)
    last_name = models.CharField(verbose_name='Nachname', max_length=127, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Geburtstag', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Ist aktiv')
    is_admin = models.BooleanField(verbose_name='Ist Admin', default=False)

    objects = DUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    class Meta:
        verbose_name = "Benutzer:in"
        verbose_name_plural = "Benutzer:innen"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def full_name(self):
        "Get full user name."
        return self.first_name + ' ' + self.last_name


class Contact(models.Model):
    created = models.DateTimeField('erstellt am', auto_now_add=True, editable=False)
    first_name = models.CharField('Vorname', max_length=127)
    last_name = models.CharField('Nachname', max_length=127)
    e_mail = models.EmailField('E-Mail')
    message = models.TextField('Nachricht', max_length=2055)
    place = models.ForeignKey('content.Place', on_delete=models.PROTECT, verbose_name='Ort')

    class Meta:
        verbose_name = "Kontaktformular"
        verbose_name_plural = "Kontaktformulare"

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
