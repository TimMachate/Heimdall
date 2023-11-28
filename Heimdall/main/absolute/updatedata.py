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

    updateUser = models.ForeignKey(
        name = 'updateUser',
        verbose_name = 'Updater',
        related_name = "%(app_label)s_%(class)s_updateUser",
        related_query_name="%(app_label)s_%(class)ss",
        to = get_user_model(),
        on_delete = models.PROTECT,
        default = None,
        editable = False,
        blank = False,
        null = True,
    )

    updateTime = models.DateTimeField(
        name = 'updateTime',
        verbose_name = 'Zeitpunkt des Updates',
        default = timezone.now,
        editable = False,
        blank = False,
        null = False,
    )

    class Meta:
        abstract = True
#--------------------------------------------------------------------------------