#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.core.validators import MinValueValidator, MaxValueValidator
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

from personalmanagement.employee.models import Employee
from structuremanagement.position.models import Position
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Section(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STSE"

    # Fields/Methodes for the department of the section
    department_id = models.ForeignKey(
        name = 'department_id',
        verbose_name = 'Bereich',
        related_name = 'section_department_id',
        to = 'structuremanagement.department', 
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    # Fields/Methodes for the employee of the section
    def employees(self):
        li = []
        for position in self.positions():
            for employee in position.employees.all():
                li.append(employee.id)
        result = Employee.objects.filter(id__in = li)
        return result

    def employee_count(self):
        result = self.employees().count()
        return result

    # Fields/Methodes for the process instruction of the section
    picture_id = models.ForeignKey(
        blank=True,
        help_text = "Bild das den Bereich beschreibt.",
        name = "picture_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "section_picture_id",
        to = "documentationmanagement.PictureProxy",
        verbose_name = "Bild",
    )

    # Fields/Methodes for the name of the section
    name = models.CharField(
        blank = True,
        max_length = 200,
        name = "name",
        null = True,
        verbose_name = "Abteilung",
    )

    # Fields/Methodes for the position of the section
    def positions(self):
        return Position.objects.filter(section_id = self.id)

    def position_count(self):
        result = self.positions().count()
        return result

    # Fields/Methodes for the process instruction of the section
    process_instruction_id = models.ForeignKey(
        blank = True,
        help_text = "Verfahrensanweisung für den Bereich.",
        name = 'process_instruction_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'section_process_instruction_id',
        to = 'documentationmanagement.ProcessInstructionProxy',
        verbose_name = 'Verfahrensanweisung',
    )

    # Fields/Methodes for the responsible person of the section

    responsible_employee_id = models.ForeignKey(
        blank=True,
        help_text = "Verantwortliche Person des Bereiches.",
        name = "responsible_employee_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "section_responsible_employee_id" ,
        to = 'personalmanagement.Employee',
        verbose_name = "Verantwortlicher",
    )

    # Fields/Methodes for the color of the section
    rgba_alpha = models.DecimalField(
        decimal_places = 2,
        default = 1,
        help_text = "Sichtbarkeit des Hintergrundes zwischen 0 und 1. 1 = 0% transparent. 0 = 100% transparent",
        max_digits = 3,
        name = 'rgba_alpha',
        validators=[MaxValueValidator(1),MinValueValidator(0)],
        verbose_name = 'Sichtbarkeit',
    )

    rgba_blue = models.PositiveSmallIntegerField(
        default = 0,
        help_text = "Blau-Wert der Hintergrundfarbe",
        name = 'rgba_blue',
        validators=[MaxValueValidator(255),MinValueValidator(0)],
        verbose_name = 'Blau-Anteil',
    )

    rgba_green = models.PositiveSmallIntegerField(
        default = 0,
        help_text = "Grün-Wert der Hintergrundfarbe",
        name = 'rgba_green',
        validators=[MaxValueValidator(255),MinValueValidator(0)],
        verbose_name = 'Grün-Anteil',
    )

    rgba_red = models.PositiveSmallIntegerField(
        default = 0,
        help_text = "Rot-Wert der Hintergrundfarbe",
        name = 'rgba_red',
        validators=[MaxValueValidator(255),MinValueValidator(0)],
        verbose_name = 'Rot-Anteil',
    )

    def rgba_style(self):
        return "style=background-color:rgba("+str(self.rgba_red)+","+str(self.rgba_green)+","+str(self.rgba_blue)+","+str(self.rgba_alpha)+")"

    def rgba_value(self):
        return "{},{},{},{}".format(str(self.rgba_red),str(self.rgba_green),str(self.rgba_blue),str(self.rgba_alpha))

    # Fields/Methodes for the short form of the section
    short_form = models.CharField(
        max_length = 6,
        name = "short_form",
        verbose_name = "Abkürzung der Abteilung",
        blank = True,
        null = True,
        )

    # Fields/Methodes for the substitute of the section

    substitute_employee_id = models.ForeignKey(
        blank=True,
        help_text = "Stellvertreter des Bereiches.",
        name = "substitute_employee_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "section_substitute_employee_id" ,
        to = 'personalmanagement.Employee',
        verbose_name = "Stellvertreter",
    )

    # Fields/Methodes for the urls of the section
    def url_delete(self):
        return reverse('structuremanagement:section_delete',kwargs={'section':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:section_detail',kwargs={'section':self.slug})
    
    def url_update(self):
        return reverse('structuremanagement:section_update',kwargs={'section':self.slug})

    # methode for the return string of the section
    def __str__(self):
        return "{} ({})".format(self.name,self.reference_number)

    # define meta data
    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_section','Can view List Abteilung'),
            ('table_section','Can view Table Abteilung'),
            ('detail_section','Can view Detail Abteilung')
        )
        verbose_name = "Abteilung"
        verbose_name_plural = "Abteilungen"
#--------------------------------------------------------------------------------