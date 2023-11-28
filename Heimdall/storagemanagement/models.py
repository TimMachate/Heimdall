#--------------------------------------------------------------------------------
# Models File from App Storagemanagement
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth import get_user_model
#--------------------------------------------------------------------------------

if 'tools' in [app.name for app in apps.get_app_configs()]:
    from tools.createdata.models import CreateData
    from tools.referencenumber.models import ReferenceNumber
    from tools.slug.models import Slug
    from tools.updatedata.models import UpdateData
else:
    #----------------------------------------------------------------------------
    # Import CreateData
    #----------------------------------------------------------------------------
    class CreateData(models.Model):

        # fields/methodes for the creation of a object
        def create_date(self):
            return self.create_datetime_formated().split(" ")[0] if self.create_datetime else None

        create_datetime = models.DateTimeField(
            blank = False,
            default = timezone.now,
            editable = False,
            help_text = "Zeitpunkt der Erstellung.",
            name = 'create_datetime',
            null = False,
            verbose_name = 'Zeitpunkt der Erstellung',
        )

        def create_datetime_formated(self):
            return self.create_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.create_datetime else None

        def create_time(self):
            return self.create_datetime_formated().split(" ")[1] if self.create_datetime else None

        create_user_id = models.ForeignKey(
            blank = False,
            default = None,
            editable = False,
            help_text = "Person der Erstellung.",
            name = 'create_user_id',
            null = True,
            on_delete = models.PROTECT,
            related_name = "{}_create_user_id".format("%(app_label)s_%(class)ss"),
            related_query_name="%(app_label)s_%(class)ss",
            to = get_user_model(),
            verbose_name = 'Ersteller',
        )

        def create_username(self):
            return str(self.create_user_id.username) if self.create_user_id else None

        class Meta:
            abstract = True
    #----------------------------------------------------------------------------

    #----------------------------------------------------------------------------
    # Import ReferenceNumber
    #----------------------------------------------------------------------------
    class ReferenceNumber(models.Model):

        # Fields/Methodes for the reference number
        reference_number = models.CharField(
            blank = True,
            default = None,
            editable = False,
            help_text = "Referenznummer, mit der eine eindeutige Identifizierung ermöglicht wird.",
            max_length = 200,
            name = 'reference_number',
            null = True,
            verbose_name = 'Aktenzeichen',
        )

        # save methode 
        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            #------------------------------------------------------------------------
            # create a reference number
            #------------------------------------------------------------------------
            sn = self.short_name if self.short_name else "OBJ"
            self.reference_number = '{}-{}'.format(sn,self.id).upper()
            #------------------------------------------------------------------------
            super().save(*args, **kwargs)

        class Meta:
            abstract = True
    #----------------------------------------------------------------------------

    #----------------------------------------------------------------------------
    # Import Slug
    #----------------------------------------------------------------------------
    class Slug(models.Model):

        # save methode 
        def save(self, *args, **kwargs):
            #------------------------------------------------------------------------
            # create a slug
            #------------------------------------------------------------------------
            sn = self.short_name if self.short_name else "OBJ"
            self.slug = slugify('{}-{}'.format(sn,self.id))
            #------------------------------------------------------------------------
            super().save(*args, **kwargs)

        # Fields/Methodes for the slug
        slug = models.SlugField(
            blank = False,
            default = None,
            editable = False,
            help_text = "Slug, mit der eine eindeutige Identifizierung ermöglicht wird.",
            name = 'slug',
            null = True,
            unique = True,
            verbose_name = 'Slug',
        )

        class Meta:
            abstract = True
    #----------------------------------------------------------------------------

    #----------------------------------------------------------------------------
    # Import UpdateData
    #----------------------------------------------------------------------------
    class UpdateData(models.Model):

        # save methode 
        def save(self, *args, **kwargs):
            #------------------------------------------------------------------------
            # update datetime
            #------------------------------------------------------------------------
            self.update_datetime = timezone.now()
            #------------------------------------------------------------------------
            super().save(*args, **kwargs)

        # fields/methodes for the creation of a object
        def update_date(self):
            return self.update_datetime_formated().split(" ")[0] if self.update_datetime else None

        update_datetime = models.DateTimeField(
            blank = False,
            default = timezone.now,
            editable = False,
            help_text = "Zeitpunkt des letzten Updates.",
            name = 'update_datetime',
            null = False,
            verbose_name = 'Zeitpunkt des Updates',
        )

        def update_datetime_formated(self):
            return self.update_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.update_datetime else None

        def update_time(self):
            return self.update_datetime_formated().split(" ")[1] if self.update_datetime else None

        update_user_id = models.ForeignKey(
            blank = False,
            default = None,
            editable = False,
            help_text = "Person des letzten Updates.",
            name = 'update_user_id',
            null = True,
            on_delete = models.PROTECT,
            related_name = "{}_update_user_id".format("%(app_label)s_%(class)ss"),
            related_query_name="%(app_label)s_%(class)ss",
            to = get_user_model(),
            verbose_name = 'Updater',
        )

        def update_username(self):
            return str(self.update_user_id.username) if self.update_user_id else None

        class Meta:
            abstract = True
    #----------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------
# Import CreateData
#--------------------------------------------------------------------------------
try:
    from tools.createdata.models import CreateData
except:
    class CreateData(models.Model):

        # fields/methodes for the creation of a object
        def create_date(self):
            return self.create_datetime_formated().split(" ")[0] if self.create_datetime else None

        create_datetime = models.DateTimeField(
            blank = False,
            default = timezone.now,
            editable = False,
            help_text = "Zeitpunkt der Erstellung.",
            name = 'create_datetime',
            null = False,
            verbose_name = 'Zeitpunkt der Erstellung',
        )

        def create_datetime_formated(self):
            return self.create_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.create_datetime else None

        def create_time(self):
            return self.create_datetime_formated().split(" ")[1] if self.create_datetime else None

        create_user_id = models.ForeignKey(
            blank = False,
            default = None,
            editable = False,
            help_text = "Person der Erstellung.",
            name = 'create_user_id',
            null = True,
            on_delete = models.PROTECT,
            related_name = "{}_create_user_id".format("%(app_label)s_%(class)ss"),
            related_query_name="%(app_label)s_%(class)ss",
            to = get_user_model(),
            verbose_name = 'Ersteller',
        )

        def create_username(self):
            return str(self.create_user_id.username) if self.create_user_id else None

        class Meta:
            abstract = True
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import ReferenceNumber
#--------------------------------------------------------------------------------
try:
    from tools.referencenumber.models import ReferenceNumber
except:
    class ReferenceNumber(models.Model):

        # Fields/Methodes for the reference number
        reference_number = models.CharField(
            blank = True,
            default = None,
            editable = False,
            help_text = "Referenznummer, mit der eine eindeutige Identifizierung ermöglicht wird.",
            max_length = 200,
            name = 'reference_number',
            null = True,
            verbose_name = 'Aktenzeichen',
        )

        # save methode 
        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            #------------------------------------------------------------------------
            # create a reference number
            #------------------------------------------------------------------------
            sn = self.short_name if self.short_name else "OBJ"
            self.reference_number = '{}-{}'.format(sn,self.id).upper()
            #------------------------------------------------------------------------
            super().save(*args, **kwargs)

        class Meta:
            abstract = True
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import Slug
#--------------------------------------------------------------------------------
try:
    from tools.slug.models import Slug
except:
    class Slug(models.Model):

        # save methode 
        def save(self, *args, **kwargs):
            #------------------------------------------------------------------------
            # create a slug
            #------------------------------------------------------------------------
            sn = self.short_name if self.short_name else "OBJ"
            self.slug = slugify('{}-{}'.format(sn,self.id))
            #------------------------------------------------------------------------
            super().save(*args, **kwargs)

        # Fields/Methodes for the slug
        slug = models.SlugField(
            blank = False,
            default = None,
            editable = False,
            help_text = "Slug, mit der eine eindeutige Identifizierung ermöglicht wird.",
            name = 'slug',
            null = True,
            unique = True,
            verbose_name = 'Slug',
        )

        class Meta:
            abstract = True
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import UpdateData
#--------------------------------------------------------------------------------
try:
    from tools.updatedata.models import UpdateData
except:
    class UpdateData(models.Model):

        # save methode 
        def save(self, *args, **kwargs):
            #------------------------------------------------------------------------
            # update datetime
            #------------------------------------------------------------------------
            self.update_datetime = timezone.now()
            #------------------------------------------------------------------------
            super().save(*args, **kwargs)

        # fields/methodes for the creation of a object
        def update_date(self):
            return self.update_datetime_formated().split(" ")[0] if self.update_datetime else None

        update_datetime = models.DateTimeField(
            blank = False,
            default = timezone.now,
            editable = False,
            help_text = "Zeitpunkt des letzten Updates.",
            name = 'update_datetime',
            null = False,
            verbose_name = 'Zeitpunkt des Updates',
        )

        def update_datetime_formated(self):
            return self.update_datetime.strftime("%d.%m.%Y %H:%M:%S") if self.update_datetime else None

        def update_time(self):
            return self.update_datetime_formated().split(" ")[1] if self.update_datetime else None

        update_user_id = models.ForeignKey(
            blank = False,
            default = None,
            editable = False,
            help_text = "Person des letzten Updates.",
            name = 'update_user_id',
            null = True,
            on_delete = models.PROTECT,
            related_name = "{}_update_user_id".format("%(app_label)s_%(class)ss"),
            related_query_name="%(app_label)s_%(class)ss",
            to = get_user_model(),
            verbose_name = 'Updater',
        )

        def update_username(self):
            return str(self.update_user_id.username) if self.update_user_id else None

        class Meta:
            abstract = True
#--------------------------------------------------------------------------------
"""