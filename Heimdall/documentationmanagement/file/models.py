#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

import os
from pathlib import Path
import qrcode
import shutil
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from main.createdata.models import CreateData
from main.referencenumber.models import ReferenceNumber
from main.slug.models import Slug
from main.updatedata.models import UpdateData

from documentationmanagement.direction.models import Direction
from documentationmanagement.document.models import Document
from documentationmanagement.formular.models import Formular
from documentationmanagement.general.models import General
from documentationmanagement.manual.models import Manual
from documentationmanagement.picture.models import Picture
from documentationmanagement.processinstruction.models import ProcessInstruction
from documentationmanagement.protocol.models import Protocol
from documentationmanagement.safetydatasheet.models import SafetyDataSheet
from documentationmanagement.technicaldatasheet.models import TechnicalDataSheet
from documentationmanagement.workingdescription.models import WorkingDescription
from documentationmanagement.workinginstruction.models import WorkingInstruction
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model Manager
#--------------------------------------------------------------------------------
class DirectionManager(models.Manager):
    def get_queryset(self):
        return super(DirectionManager,self).get_queryset().filter(type='DI')
#--------------------------------------------------------------------------------
class DocumentManager(models.Manager):
    def get_queryset(self):
        return super(DocumentManager,self).get_queryset().filter(type='DO')
#--------------------------------------------------------------------------------
class FormularManager(models.Manager):
    def get_queryset(self):
        return super(FormularManager,self).get_queryset().filter(type='FO')
#--------------------------------------------------------------------------------
class GeneralManager(models.Manager):
    def get_queryset(self):
        return super(GeneralManager,self).get_queryset().filter(type='GE')
#--------------------------------------------------------------------------------
class ManualManager(models.Manager):
    def get_queryset(self):
        return super(ManualManager,self).get_queryset().filter(type='MA')
#--------------------------------------------------------------------------------
class PictureManager(models.Manager):
    def get_queryset(self):
        return super(PictureManager,self).get_queryset().filter(type='PI')
#--------------------------------------------------------------------------------
class ProcessinstructionManager(models.Manager):
    def get_queryset(self):
        return super(ProcessinstructionManager,self).get_queryset().filter(type='PR')
#--------------------------------------------------------------------------------
class ProtocolManager(models.Manager):
    def get_queryset(self):
        return super(ProtocolManager,self).get_queryset().filter(type='PO')
#--------------------------------------------------------------------------------
class SaftydatasheetManager(models.Manager):
    def get_queryset(self):
        return super(SaftydatasheetManager,self).get_queryset().filter(type='SA')
#--------------------------------------------------------------------------------
class TechnicaldatasheetManager(models.Manager):
    def get_queryset(self):
        return super(TechnicaldatasheetManager,self).get_queryset().filter(type='TE')
#--------------------------------------------------------------------------------
class WorkingdescriptionManager(models.Manager):
    def get_queryset(self):
        return super(WorkingdescriptionManager,self).get_queryset().filter(type='WD')
#--------------------------------------------------------------------------------
class WorkinginstructionManager(models.Manager):
    def get_queryset(self):
        return super(WorkinginstructionManager,self).get_queryset().filter(type='WO')
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class File(CreateData, ReferenceNumber, Slug, UpdateData):

    # Variables
    short_name="DO"

    class Types(models.TextChoices):
        DIRECTION = 'DI',_("Betriebsanweisung")
        DOCUMENT = 'DO',_("Dokument")
        FORMULAR = 'FO',_("Formular")
        GENERAL = 'GE',_("Sonstiges")
        MANUAL = 'MA',_("Handbuch")
        PICTURE = 'PI',_("Bild")
        PROCESSINSTRUCTION = 'PR',_("Verfahrensanweisung")
        PROTOCOL = 'PO',_("Protokoll")
        SAFTYDATASHEET = 'SA',_("Sicherheits Datenblatt")
        TECHNICALDATASHEET = 'TE',_("Technisches Datenblatt")
        WORKINGDESCRIPTION = 'WD',_("Arbeitsplatzbeschreibung")
        WORKINGINSTRUCTION = 'WO',_("Arbeitsanweisung")

    file = models.FileField(
        name = "file",
        verbose_name = "Datei",
        upload_to = '',
        blank = True,
        null = True,
    )

    keywords = HTMLField(
        name = 'keywords',
        verbose_name = 'Schlagwörter',
        blank = True,
        null = True,
    )

    name = models.CharField(
        max_length = 200,
        name = 'name',
        verbose_name = 'Name',
        blank = True,
        null = True,
    )

    qrcode_detail = models.ImageField(
        name = "qrcode_detail",
        verbose_name = "QRCode Detail",
        upload_to = '',
        editable = False,
        blank = True,
        null = True,
    )

    Type = models.CharField(
        max_length = 2,
        name="type",
        verbose_name="Typ",
        choices = Types.choices,
        default = Types.GENERAL,
    )

    version_prefix = models.IntegerField(
        name = 'version_prefix',
        verbose_name = 'Version',
        default = 1,
        blank = False,
        null = False,
    )

    version_suffix = models.IntegerField(
        name = 'version_suffix',
        verbose_name = 'Version',
        default=-1,
        editable = False,
        blank = False,
        null = False,
    )

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__original_version_prefix = self.version_prefix

    def __str__(self):
        return str(self.name)+' ('+str(self.reference_number)+')'

    def version(self):
        return str(self.version_prefix)+'-'+str(self.version_suffix)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #------------------------------------------------------------------------
        # Change Version after changes
        #------------------------------------------------------------------------
        self.version_suffix = self.version_suffix + 1 if self.__original_version_prefix == self.version_prefix else 0
        #------------------------------------------------------------------------

        #------------------------------------------------------------------------
        # safe file to correct location and rename it
        #------------------------------------------------------------------------
        if self.file:
            extend = self.file.name.split('.')[-1]
            new_file_name = self.name+'_V'+self.version()+'.'+extend
            media_root_path = Path(settings.MEDIA_ROOT)
            new_path = os.path.join(media_root_path,self._meta.app_label,self.type,self.reference_number)
            new_file_path = os.path.join(new_path,new_file_name)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            if not os.path.exists(os.path.join(new_path,"Archiv")):
                os.makedirs(os.path.join(new_path,"Archiv"))
            if self.file.path == os.path.join(media_root_path,self.file.name):
                os.rename(self.file.path,new_file_path)
                self.file = os.path.join(self._meta.app_label,self.type,self.reference_number,new_file_name)
                shutil.copy(self.file.path,os.path.join(new_path,"Archiv"))
            if self.file.path != new_file_path:
                shutil.copy(self.file.path,new_file_path)
                self.file = os.path.join(self._meta.app_label,self.type,self.reference_number,new_file_name)
        #------------------------------------------------------------------------
        return super().save(*args, **kwargs)

    def url_delete(self):
        url = reverse('documentationmanagement:file_delete',kwargs={'file':self.slug})
        return url
        
    def url_detail(self):
        url = reverse('documentationmanagement:file_detail',kwargs={'file':self.slug})
        return url

    def url_file(self):
        if self.file:
            result = self.file.url
        else:
            result = None
        return result

    def url_file_qrcode(self):
        if self.qrcode_detail:
            result = self.qrcode_detail.url
        else:
            result = None
        return result

    def url_update(self):
        url = reverse('documentationmanagement:file_update',kwargs={'file':self.slug})
        return url

    class Meta:
        app_label = 'documentationmanagement'
        ordering = ['name']
        permissions = (
            #('add_file','Can view add File'),
            #('change_file','Can view Change File'),
            #('delete_file','Can view Delete File'),
            ('detail_file','Can view Detail Datei'),
            ('list_file','Can view List Datei'),
            ('table_file','Can view Table Datei'),
            #('view_file','Can view Overview File')
        )
        verbose_name = "Datei"
        verbose_name_plural = "Dateien"
#--------------------------------------------------------------------------------
class DirectionProxy(File):
    objects = DirectionManager()

    def content(self):
        result = Direction.objects.get(file_id=self.id) if Direction.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = Direction.objects.get(file_id=self.id).reference_number if Direction.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = Direction.objects.get(file_id=self.id).slug if Direction.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:direction_delete',kwargs={'direction':Direction.objects.get(file_id=self.id).slug if Direction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:direction_delete',kwargs={'direction':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:direction_detail',kwargs={'direction':Direction.objects.get(file_id=self.id).slug if Direction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:direction_detail',kwargs={'direction':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:direction_update',kwargs={'direction':Direction.objects.get(file_id=self.id).slug if Direction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:direction_update',kwargs={'direction':self.slug})
        return url

    class Meta:
        proxy = True
        verbose_name = 'Betriebsanweisung'
        verbose_name_plural = 'Betriebsanweisungen'
#--------------------------------------------------------------------------------
class DocumentProxy(File):
    objects = DocumentManager()

    def content(self):
        result = Document.objects.get(file_id=self.id) if Document.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = Document.objects.get(file_id=self.id).reference_number if Document.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = Document.objects.get(file_id=self.id).slug if Document.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:document_delete',kwargs={'document':Document.objects.get(file_id=self.id).slug if Document.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:document_delete',kwargs={'document':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:document_detail',kwargs={'document':Document.objects.get(file_id=self.id).slug if Document.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:document_detail',kwargs={'document':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:document_update',kwargs={'document':Document.objects.get(file_id=self.id).slug if Document.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:document_update',kwargs={'document':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_document','Can view List Document'),
            ('table_document','Can view Table Document'),
            ('detail_document','Can view Detail Document')
        )
        proxy = True
        verbose_name = 'Dokument'
        verbose_name_plural = 'Dokumente'
#--------------------------------------------------------------------------------
class FormularProxy(File):
    objects = FormularManager()

    def content(self):
        result = Formular.objects.get(file_id=self.id) if Formular.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = Formular.objects.get(file_id=self.id).reference_number if Formular.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = Formular.objects.get(file_id=self.id).slug if Formular.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:formular_delete',kwargs={'formular':Formular.objects.get(file_id=self.id).slug if Formular.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:formular_delete',kwargs={'formular':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:formular_detail',kwargs={'formular':Formular.objects.get(file_id=self.id).slug if Formular.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:formular_detail',kwargs={'formular':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:formular_update',kwargs={'formular':Formular.objects.get(file_id=self.id).slug if Formular.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:formular_update',kwargs={'formular':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_formular','Can view List Formular'),
            ('table_formular','Can view Table Formular'),
            ('detail_formular','Can view Detail Formular')
        )
        proxy = True
        verbose_name = 'Formular'
        verbose_name_plural = 'Formulare'
#--------------------------------------------------------------------------------
class GeneralProxy(File):
    objects = GeneralManager()

    def content(self):
        result = General.objects.get(file_id=self.id) if General.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = General.objects.get(file_id=self.id).reference_number if General.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = General.objects.get(file_id=self.id).slug if General.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:general_delete',kwargs={'general':General.objects.get(file_id=self.id).slug if General.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:general_delete',kwargs={'general':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:general_detail',kwargs={'general':General.objects.get(file_id=self.id).slug if General.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:general_detail',kwargs={'general':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:general_update',kwargs={'general':General.objects.get(file_id=self.id).slug if General.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:general_update',kwargs={'general':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_general','Can view List General'),
            ('table_general','Can view Table General'),
            ('detail_general','Can view Detail General')
        )
        proxy = True
        verbose_name = 'Sontiges'
        verbose_name_plural = 'Sontiges'
#--------------------------------------------------------------------------------
class ManualProxy(File):
    objects = ManualManager()

    def content(self):
        result = Manual.objects.get(file_id=self.id) if Manual.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = Manual.objects.get(file_id=self.id).reference_number if Manual.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = Manual.objects.get(file_id=self.id).slug if Manual.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:manual_delete',kwargs={'manual':Manual.objects.get(file_id=self.id).slug if Manual.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:manual_delete',kwargs={'manual':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:manual_detail',kwargs={'manual':Manual.objects.get(file_id=self.id).slug if Manual.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:manual_detail',kwargs={'manual':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:manual_update',kwargs={'manual':Manual.objects.get(file_id=self.id).slug if Manual.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:manual_update',kwargs={'manual':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_manual','Can view List Manual'),
            ('table_manual','Can view Table Manual'),
            ('detail_manual','Can view Detail Manual')
        )
        proxy = True
        verbose_name = 'Handbuch'
        verbose_name_plural = 'Handbücher'
#--------------------------------------------------------------------------------
class PictureProxy(File):
    objects = PictureManager()

    def content(self):
        result = Picture.objects.get(file_id=self.id) if Picture.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = Picture.objects.get(file_id=self.id).reference_number if Picture.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = Picture.objects.get(file_id=self.id).slug if Picture.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:picture_delete',kwargs={'picture':Picture.objects.get(file_id=self.id).slug if Picture.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:picture_delete',kwargs={'picture':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:picture_detail',kwargs={'picture':Picture.objects.get(file_id=self.id).slug if Picture.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:picture_detail',kwargs={'picture':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:picture_update',kwargs={'picture':Picture.objects.get(file_id=self.id).slug if Picture.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:picture_update',kwargs={'picture':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_picture','Can view List Picture'),
            ('table_picture','Can view Table Picture'),
            ('detail_picture','Can view Detail Picture')
        )
        proxy = True
        verbose_name = 'Bild'
        verbose_name_plural = 'Bilder'
#--------------------------------------------------------------------------------
class ProcessInstructionProxy(File):
    objects = ProcessinstructionManager()

    def content(self):
        result = ProcessInstruction.objects.get(file_id=self.id) if ProcessInstruction.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = ProcessInstruction.objects.get(file_id=self.id).reference_number if ProcessInstruction.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = ProcessInstruction.objects.get(file_id=self.id).slug if ProcessInstruction.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:processinstruction_delete',kwargs={'processinstruction':ProcessInstruction.objects.get(file_id=self.id).slug if ProcessInstruction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:processinstruction_delete',kwargs={'processinstruction':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:processinstruction_detail',kwargs={'processinstruction':ProcessInstruction.objects.get(file_id=self.id).slug if ProcessInstruction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:processinstruction_detail',kwargs={'processinstruction':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:processinstruction_update',kwargs={'processinstruction':ProcessInstruction.objects.get(file_id=self.id).slug if ProcessInstruction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:processinstruction_update',kwargs={'processinstruction':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_processinstruction','Can view List Process Instruction'),
            ('table_processinstruction','Can view Table Process Instruction'),
            ('detail_processinstruction','Can view Detail Process Instruction')
        )
        proxy = True
        verbose_name = 'Verfahrensanweisung'
        verbose_name_plural = 'Verfahrensanweisung'
#--------------------------------------------------------------------------------
class ProtocolProxy(File):
    objects = ProtocolManager()

    class Meta:
        permissions = (
            ('list_protocol','Can view List Protocol'),
            ('table_protocol','Can view Table Protocol'),
            ('detail_protocol','Can view Detail Protocol')
        )
        proxy = True
        verbose_name = 'Protokoll'
        verbose_name_plural = 'Protokolle'
#--------------------------------------------------------------------------------
class SafetyDataSheetProxy(File):
    objects = SaftydatasheetManager()

    def content(self):
        result = SafetyDataSheet.objects.get(file_id=self.id) if SafetyDataSheet.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = SafetyDataSheet.objects.get(file_id=self.id).reference_number if SafetyDataSheet.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = SafetyDataSheet.objects.get(file_id=self.id).slug if SafetyDataSheet.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:safetydatasheet_delete',kwargs={'safetydatasheet':SafetyDataSheet.objects.get(file_id=self.id).slug if SafetyDataSheet.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:safetydatasheet_delete',kwargs={'safetydatasheet':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:safetydatasheet_detail',kwargs={'safetydatasheet':SafetyDataSheet.objects.get(file_id=self.id).slug if SafetyDataSheet.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:safetydatasheet_detail',kwargs={'safetydatasheet':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:safetydatasheet_update',kwargs={'safetydatasheet':SafetyDataSheet.objects.get(file_id=self.id).slug if SafetyDataSheet.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:safetydatasheet_update',kwargs={'safetydatasheet':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_safetydatasheet','Can view List Safety Data Sheet'),
            ('table_safetydatasheet','Can view Table Safety Data Sheet'),
            ('detail_safetydatasheet','Can view Detail Safety Data Sheet')
        )
        proxy = True
        verbose_name = 'Sicherheitsdatenblatt'
        verbose_name_plural = 'Sicherheitsdatenblätter'
#--------------------------------------------------------------------------------
class TechnicalDataSheetProxy(File):
    objects = TechnicaldatasheetManager()

    def content(self):
        result = TechnicalDataSheet.objects.get(file_id=self.id) if TechnicalDataSheet.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = TechnicalDataSheet.objects.get(file_id=self.id).reference_number if TechnicalDataSheet.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = TechnicalDataSheet.objects.get(file_id=self.id).slug if TechnicalDataSheet.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:technicaldatasheet_delete',kwargs={'technicaldatasheet':TechnicalDataSheet.objects.get(file_id=self.id).slug if TechnicalDataSheet.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:technicaldatasheet_delete',kwargs={'technicaldatasheet':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:technicaldatasheet_detail',kwargs={'technicaldatasheet':TechnicalDataSheet.objects.get(file_id=self.id).slug if TechnicalDataSheet.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:technicaldatasheet_detail',kwargs={'technicaldatasheet':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:technicaldatasheet_update',kwargs={'technicaldatasheet':TechnicalDataSheet.objects.get(file_id=self.id).slug if TechnicalDataSheet.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:technicaldatasheet_update',kwargs={'technicaldatasheet':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_technicaldatasheet','Can view List Technical Data Sheet'),
            ('table_technicaldatasheet','Can view Table Technical Data Sheet'),
            ('detail_technicaldatasheet','Can view Detail Technical Data Sheet')
        )
        proxy = True
        verbose_name = 'Technischesdatenblatt'
        verbose_name_plural = 'Technischedatenblätter'
#--------------------------------------------------------------------------------
class WorkingDescriptionProxy(File):
    objects = WorkingdescriptionManager()

    def content(self):
        result = WorkingDescription.objects.get(file_id=self.id) if WorkingDescription.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = WorkingDescription.objects.get(file_id=self.id).reference_number if WorkingDescription.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = WorkingDescription.objects.get(file_id=self.id).slug if WorkingDescription.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:workingdescription_delete',kwargs={'workingdescription':WorkingDescription.objects.get(file_id=self.id).slug if WorkingDescription.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:workingdescription_delete',kwargs={'workingdescription':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:workingdescription_detail',kwargs={'workingdescription':WorkingDescription.objects.get(file_id=self.id).slug if WorkingDescription.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:workingdescription_detail',kwargs={'workingdescription':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:workingdescription_update',kwargs={'workingdescription':WorkingDescription.objects.get(file_id=self.id).slug if WorkingDescription.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:workingdescription_update',kwargs={'workingdescription':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_workingdescription','Can view List Working Description'),
            ('table_workingdescription','Can view Table Working Description'),
            ('detail_workingdescription','Can view Detail Working Description')
        )
        proxy = True
        verbose_name = 'Arbeitsplatzbeschreibung'
        verbose_name_plural = 'Arbeitsblattbeschreibungen'
#--------------------------------------------------------------------------------
class WorkingInstructionProxy(File):
    objects = WorkinginstructionManager()

    def content(self):
        result = WorkingInstruction.objects.get(file_id=self.id) if WorkingInstruction.objects.filter(file_id=self.id).count() == 1 else None
        return result
    
    def reference_number(self):
        result = WorkingInstruction.objects.get(file_id=self.id).reference_number if WorkingInstruction.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def slug(self):
        result = WorkingInstruction.objects.get(file_id=self.id).slug if WorkingInstruction.objects.filter(file_id=self.id).count() == 1 else None
        return result

    def url_delete(self):
        #url = reverse('documentationmanagement:workinginstruction_delete',kwargs={'workinginstruction':WorkingInstruction.objects.get(file_id=self.id).slug if WorkingInstruction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:workinginstruction_delete',kwargs={'workinginstruction':self.slug})
        return url
        
    def url_detail(self):
        #url = reverse('documentationmanagement:workinginstruction_detail',kwargs={'workinginstruction':WorkingInstruction.objects.get(file_id=self.id).slug if WorkingInstruction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:workinginstruction_detail',kwargs={'workinginstruction':self.slug})
        return url

    def url_update(self):
        #url = reverse('documentationmanagement:workinginstruction_update',kwargs={'workinginstruction':WorkingInstruction.objects.get(file_id=self.id).slug if WorkingInstruction.objects.filter(file_id=self.id).count() == 1 else self.slug})
        url = reverse('documentationmanagement:workinginstruction_update',kwargs={'workinginstruction':self.slug})
        return url

    class Meta:
        permissions = (
            ('list_workinginstruction','Can view List Working Instruction'),
            ('table_workinginstruction','Can view Table Working Instruction'),
            ('detail_workinginstruction','Can view Detail Working Instruction')
        )
        proxy = True
        verbose_name = 'Arbeitsanweisung'
        verbose_name_plural = 'Arbeitsanweisung'
#--------------------------------------------------------------------------------