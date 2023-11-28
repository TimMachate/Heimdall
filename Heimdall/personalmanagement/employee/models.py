#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
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
class Employee(CreateData,ReferenceNumber,Slug,UpdateData):

    short_name = "PEEM"

    user = models.OneToOneField(
        name = "user",
        verbose_name = "Benutzername",
        related_name = "employeeUser",
        to = get_user_model(),
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        unique = True,
        )

    shortname = models.CharField(
        max_length = 200,
        name = "shortName",
        verbose_name = "Kürzel",
        blank=True,
        null=True,
    )

    birthday = models.DateField(
        name = "birthday",
        verbose_name = "Geburtstag",
        blank=True,
        null=True,
    )

    nation = models.CharField(
        max_length = 200,
        name = 'nation',
        verbose_name = 'Staatsangehörigkeit',
        blank = True,
        null = True,
    )

    street = models.CharField(
        max_length = 200,
        name = 'street',
        verbose_name = 'Straße',
        blank = True,
        null = True,
    )

    houseNumber = models.CharField(
        max_length = 200,
        name = 'houseNumber',
        verbose_name = 'Hausnummer',
        blank = True,
        null = True,
    )

    postCode = models.CharField(
        max_length = 200,
        name = 'postCode',
        verbose_name = 'Postleitzahl',
        blank = True,
        null = True,
    )

    city = models.CharField(
        max_length = 200,
        name = 'city',
        verbose_name = 'Stadt',
        blank = True,
        null = True,
    )

    country = models.CharField(
        max_length = 200,
        name = 'country',
        verbose_name = 'Land',
        blank = True,
        null = True,
    )

    telephone = models.CharField(
        max_length = 200,
        name = 'telephone',
        verbose_name = 'Telefonnummer',
        blank = True,
        null = True,
    )

    email = models.EmailField(
        name = 'email',
        verbose_name = 'Email',
        blank = True,
        null = True,
    )

    notice = models.TextField(
        name = 'notice',
        verbose_name = 'Bemerkung',
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name()

    def name(self):
        return "{}, {}".format(self.user.last_name,self.user.first_name)
        
    def url_delete(self):
        return "#"#reverse('personalmanagement:employee_delete',kwargs={'employee':self.id})

    def url_detail(self):
        return "#"#reverse('personalmanagement:employee_detail',kwargs={'employee':self.id})
    
    def url_update(self):
        return "#"#reverse('personalmanagement:employee_update',kwargs={'employee':self.id})

    class Meta:
        app_label = 'personalmanagement'
        ordering = []
        permissions = (
            ('list_employee','Can view List Unternehmen'),
            ('table_employee','Can view Table Unternehmen'),
            ('detail_employee','Can view Detail Unternehmen')
        )
        verbose_name = "Mitarbeiter"
        verbose_name_plural = "Mitarbeiter"
#--------------------------------------------------------------------------------