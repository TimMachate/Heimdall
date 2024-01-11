"""
#--------------------------------------------------------------------------------
# Models File from Model Programm
# 17.12.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

from tinymce import models as tinymce_models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from programmmanagement.models import (
    CreateData,
    ReferenceNumber,
    Slug,
    UpdateData
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class ProgrammBaseModel(CreateData,ReferenceNumber,Slug,UpdateData):
    """
    ProgrammBaseModel

    Args:
        CreateData (_type_): _description_
        ReferenceNumber (_type_): _description_
        Slug (_type_): _description_
        UpdateData (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Variables
    short_name = "PrPr"

    description = tinymce_models.HTMLField(
        blank = True,
        help_text = "Kurze Beschreibung des Programms.",
        name = 'description',
        null = True,
        verbose_name = 'Beschreibung',
    )

    name = models.CharField(
        name = 'name',
        verbose_name = 'Name',
        max_length = 200,
        blank = False,
        null = False,
    )

    htmlfile = models.FileField(
        name = 'htmlfile',
        verbose_name = 'HTML Datei',
        upload_to = 'programmmanagement/programm/',
        blank = True,
        null = True,
    )

    users = models.ManyToManyField(
        blank = True,
        name = 'users',
        to = get_user_model(),
        verbose_name = 'Benutzer',
    )

    class Meta:
        """
        Meta Data from ProgrammBaseModel
        """
        app_label = 'programmmanagement'
        default_permissions = ()
#--------------------------------------------------------------------------------
class Programm(ProgrammBaseModel):
    """
    Programm

    Args:
        ProgrammBaseModel (_type_): _description_
    """

    # HTMLFile
    def htmlfile_name(self):
        """
        htmlfile_name

        Returns:
            string: name of html file
        """
        return self.htmlfile.name.split("/")[-1] if self.htmlfile else None

    def htmlfile_url(self):
        """
        htmlfile_url

        Returns:
            string: url to html file
        """
        return self.htmlfile.url if self.htmlfile else None

    # Urls
    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to programm detail page
        """
        return reverse(
            'programmmanagement:programm_detail',
            kwargs={"programm":self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to programm delete page
        """
        return reverse(
            'programmmanagement:programm_delete',
            kwargs={"programm":self.slug}
        )

    def url_programm(self):
        """
        url_programm

        Returns:
            string: url to programm page
        """
        return reverse(
            'programmmanagement:programmmanagement_page',
            kwargs={"programm":self.slug}
        )

    def url_qrcode(self):
        """
        url qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        """
        url_update

        Returns:
            string: url to programm update page
        """
        return reverse(
            'programmmanagement:programm_update',
            kwargs={"programm":self.slug}
        )

    def users_count(self):
        """
        users_count

        Returns:
            int: count from users they are allowed to use the programm
        """
        return self.users.count()

    def __str__(self):
        return f"{self.name} ({self.reference_number})"

    class Meta:
        """
        Meta Data from Model
        """
        app_label = 'programmmanagement'
        default_permissions = ()
        ordering = []
        permissions = (
            ('add_programm','Programm can view create'),
            ('change_programm','Programm can view change'),
            ('delete_programm','Programm can view delete'),
            ('detail_programm','Programm can view detail'),
            ('list_programm','Programm can view list'),
            ('programm_programm','Programm can view page'),
            ('table_programm','Programm can view table'),
            ('view_programm','Programm can view overview'),
        )
        proxy = True
        verbose_name = "Programm"
        verbose_name_plural = "Programme"
#--------------------------------------------------------------------------------
