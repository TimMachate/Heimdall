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
class CreateData(models.Model):

    createUser = models.ForeignKey(
        name = 'createUser',
        verbose_name = 'Ersteller',
        related_name = "{}_createUser".format("%(app_label)s_%(class)ss"),
        related_query_name="%(app_label)s_%(class)ss",
        to = get_user_model(),
        on_delete = models.PROTECT,
        default = None,
        editable = False,
        blank = False,
        null = True,
    )

    createTime = models.DateTimeField(
        name = 'createTime',
        verbose_name = 'Zeitpunkt der Erstellung',
        default = timezone.now,
        editable = False,
        blank = False,
        null = False,
    )

    class Meta:
        abstract = True
#--------------------------------------------------------------------------------