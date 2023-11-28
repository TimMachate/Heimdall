#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from main.createdata.models import CreateData
from main.referencenumber.models import ReferenceNumber
from main.slug.models import Slug
from main.updatedata.models import UpdateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class EmailPerson(models.Model):

    person_id = models.ForeignKey(
        blank = True,
        help_text = "Person die zur Email gehört.",
        name = 'person_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = "email_person_id",
        to = "relationshipmanagement.Person",
        verbose_name = 'Person',
    )

    email = models.EmailField(
        blank = True,
        help_text = "Email-Adresse.",
        name = 'email',
        null = True,
        verbose_name = 'Email',
    )

    class Meta:
        app_label = 'relationshipmanagement'
        verbose_name = "Email"
        verbose_name_plural = "Emails"
#--------------------------------------------------------------------------------
class Person(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "REPE"

    company_id = models.ForeignKey(
        name = 'company_id',
        verbose_name = 'Firma',
        related_name = 'person_company_id',
        to = 'relationshipmanagement.Company',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    # Fields/Methodes for the email
    def emails(self):
        return EmailPerson.objects.filter(person_id = self)

    first_name = models.CharField(
        max_length = 200,
        name = 'first_name',
        verbose_name = 'Vorname',
        blank = True,
        null = True,
    )

    last_name = models.CharField(
        max_length = 200,
        name = 'last_name',
        verbose_name = 'Nachname',
        blank = True,
        null = True,
    )

    notice = tinymce_models.HTMLField(
        name = 'notice',
        verbose_name = 'Bemerkung',
        blank = True,
        null = True,
    )

    # Fields/Methodes for the telephone numbers
    def telephones(self):
        return TelephonePerson.objects.filter(person_id = self)

    def url_detail(self):
        return reverse('relationshipmanagement:person_detail',kwargs={"person":self.slug})

    def url_delete(self):
        return reverse('relationshipmanagement:person_delete',kwargs={"person":self.slug})
    
    def url_update(self):
        return reverse('relationshipmanagement:person_update',kwargs={"person":self.slug})

    def __str__(self):
        return str(self.lastName) + ', ' + str(self.firstName)

    class Meta:
        app_label = 'relationshipmanagement'
        ordering = []
        permissions = (
            ('list_person','Can view List Person'),
            ('table_person','Can view Table Person'),
            ('detail_person','Can view Detail Person')
        )
        verbose_name = "Person"
        verbose_name_plural = "Personen"
#--------------------------------------------------------------------------------
class TelephonePerson(models.Model):

    class Types(models.IntegerChoices):
        TELEPHONE = 1,_("Telefon")
        MOBILEPHONE = 2,_("Handy")
        FAX = 3,_("Fax")

    person_id = models.ForeignKey(
        blank = True,
        help_text = "Person die zur Telefonnummer gehört.",
        name = 'person_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = "telephone_person_id",
        to = "relationshipmanagement.Person",
        verbose_name = 'Person',
    )

    number = models.CharField(
        blank = True,
        help_text = "Telefonnummer.",
        max_length = 200,
        name = 'number',
        null = True,
        verbose_name = 'Telefonnummer',
    )

    # Fields/Methodes for the type
    type = models.IntegerField(
        choices = Types.choices,
        default = Types.TELEPHONE,
        name="type",
        verbose_name="Typ",
    )

    class Meta:
        app_label = 'relationshipmanagement'
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"
#--------------------------------------------------------------------------------