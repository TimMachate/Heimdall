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
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Department(CreateData,ReferenceNumber,Slug,UpdateData):

    # Variables
    short_name = "STDE"

    # Fields/Methodes for the employee of the department
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

    # Fields/Methodes for the process instruction of the department
    picture_id = models.ForeignKey(
        blank=True,
        help_text = "Bild das den Bereich beschreibt.",
        name = "picture_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "department_picture_id",
        to = "documentationmanagement.PictureProxy",
        verbose_name = "Bild",
    )

    # Fields/Methodes for the name of the department
    name = models.CharField(
        blank = True,
        max_length = 200,
        name = "name",
        null = True,
        verbose_name = "Bereich",
    )

    # Fields/Methodes for the position of the department
    def positions(self):
        return Position.objects.filter(section_id__department_id = self.id)

    def position_count(self):
        result = self.positions().count()
        return result

    # Fields/Methodes for the process instruction of the department
    process_instruction_id = models.ForeignKey(
        blank = True,
        help_text = "Verfahrensanweisung für den Bereich.",
        name = 'process_instruction_id',
        null = True,
        on_delete = models.CASCADE,
        related_name = 'department_process_instruction_id',
        to = 'documentationmanagement.ProcessInstructionProxy',
        verbose_name = 'Verfahrensanweisung',
    )

    # Fields/Methodes for the responsible person of the department

    responsible_employee_id = models.ForeignKey(
        blank=True,
        help_text = "Verantwortliche Person des Bereiches.",
        name = "responsible_employee_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "department_responsible_employee_id" ,
        to = 'personalmanagement.Employee',
        verbose_name = "Verantwortlicher",
    )

    # Fields/Methodes for the color of the department
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

    # Fields/Methodes for the section of the department
    def sections(self):
        return Section.objects.filter(department_id = self.id)

    def section_count(self):
        result = self.sections().count()
        return result
    
    # Fields/Methodes for the substitute of the department

    substitute_employee_id = models.ForeignKey(
        blank=True,
        help_text = "Stellvertreter des Bereiches.",
        name = "substitute_employee_id",
        null=True,
        on_delete= models.PROTECT,
        related_name= "department_substitute_employee_id" ,
        to = 'personalmanagement.Employee',
        verbose_name = "Stellvertreter",
    )

    # Fields/Methodes for the urls of the department
    def url_delete(self):
        return reverse('structuremanagement:department_delete',kwargs={'department':self.slug})

    def url_detail(self):
        return reverse('structuremanagement:department_detail',kwargs={'department':self.slug})
    
    def url_update(self):
        return reverse('structuremanagement:department_update',kwargs={'department':self.slug})

    # methode for the return string of the department
    def __str__(self):
        return "{} ({})".format(self.name,self.reference_number)

    # define meta data
    class Meta:
        app_label = 'structuremanagement'
        ordering = ['name']
        permissions = (
            ('list_department','Can view List Bereich'),
            ('table_department','Can view Table Bereich'),
            ('detail_department','Can view Detail Bereich')
        )
        verbose_name = "Bereich"
        verbose_name_plural = "Bereiche"
#--------------------------------------------------------------------------------