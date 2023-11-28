#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.urls import reverse

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
class Position(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STPO"

    # Fields/Methodes for the description of the position
    description = tinymce_models.HTMLField(
        name = 'description',
        verbose_name= "Beschreibung",
        blank=True,
        null=True,
    )

    # Fields/Methodes for the direction of the position
    directions = models.ManyToManyField(
        name = 'directions',
        verbose_name = 'Betriebsanweisungen',
        related_name = 'position_directions',
        to = 'documentationmanagement.DirectionProxy',
        blank = True,
    )

    # Fields/Methodes for the documents of the position
    documents = models.ManyToManyField(
        name = 'documents',
        verbose_name = 'Dokumente',
        related_name = 'position_documents',
        to = 'documentationmanagement.DocumentProxy',
        blank = True,
    )

    def department(self):
        result = self.section_id.department_id if self.section_id else None
        return result

    # Fields/Methodes for the employees of the position
    employees = models.ManyToManyField(
        name = 'employees',
        verbose_name = 'Mitarbeiter',
        related_name = 'position_employees',
        to = 'personalmanagement.Employee',
        blank = True,
    )

    # Fields/Methodes for the process instruction of the position
    picture_id = models.ForeignKey(
        blank=True,
        help_text = "Bild das den Bereich beschreibt.",
        name = "picture_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "position_picture_id",
        to = "documentationmanagement.PictureProxy",
        verbose_name = "Bild",
    )

    # Fields/Methodes for the name of the position
    name = models.CharField(
        blank = True,
        max_length = 200,
        name = "name",
        null = True,
        verbose_name = "Arbeitsplatz",
    )

    # Fields/Methodes for the responsible person of the position

    responsible_employee_id = models.ForeignKey(
        blank=True,
        help_text = "Verantwortliche Person des Bereiches.",
        name = "responsible_employee_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "position_responsible_employee_id" ,
        to = 'personalmanagement.Employee',
        verbose_name = "Verantwortlicher",
    )

    # Fields/Methodes for the safety data sheets of the position
    safety_data_sheets = models.ManyToManyField(
        name = 'safety_data_sheets',
        verbose_name = 'Datensicherheitsblätter',
        related_name = 'position_safety_data_sheets',
        to = 'documentationmanagement.SafetyDataSheetProxy',
        blank = True,
    )

    # Fields/Methodes for the section of the position
    section_id = models.ForeignKey(
        name = 'section_id',
        verbose_name = 'Abteilungen',
        related_name = 'position_section_id',
        to = 'structuremanagement.Section', 
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    # Fields/Methodes for the substitute of the position

    substitute_employee_id = models.ForeignKey(
        blank=True,
        help_text = "Stellvertreter des Bereiches.",
        name = "substitute_employee_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "position_substitute_employee_id" ,
        to = 'personalmanagement.Employee',
        verbose_name = "Stellvertreter",
    )

    # Fields/Methodes for the urls of the position
    def url_delete(self):
        return reverse('structuremanagement:position_delete',kwargs={'position':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:position_detail',kwargs={'position':self.slug})
    
    def url_update(self):
        return reverse('structuremanagement:position_update',kwargs={'position':self.slug})

    # Fields/Methodes for the working description of the position
    working_description_id = models.ForeignKey(
        name = 'working_description_id',
        verbose_name = 'Arbeitsplatzbeschreibung',
        related_name = 'position_working_description_id',
        to = 'documentationmanagement.WorkingDescriptionProxy',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    # Fields/Methodes for the working instruction of the position
    working_instructions = models.ManyToManyField(
        name = 'working_instructions',
        verbose_name = 'Arbeitsanweisungen',
        related_name = 'positionWorking_instructions',
        to = 'documentationmanagement.WorkingInstructionProxy',
        blank = True,
    )

    # methode for the return string of the position
    def __str__(self):
        return "{} ({})".format(self.name,self.reference_number)

    # define meta data
    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_position','Can view List Arbeitsplatz'),
            ('table_position','Can view Table Arbeitsplatz'),
            ('detail_position','Can view Detail Arbeitsplatz')
        )
        verbose_name = "Arbeitsplatz"
        verbose_name_plural = "Arbeitsplatz"
#--------------------------------------------------------------------------------