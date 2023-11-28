#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
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