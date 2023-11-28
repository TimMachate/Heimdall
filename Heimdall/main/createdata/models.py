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