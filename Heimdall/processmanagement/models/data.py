#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.db import models
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from .abstract import CreateData
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class Data(CreateData):
    commission = models.ForeignKey(
        name = 'commission',
        verbose_name = 'Auftrag',
        to = 'commission.Commission',
        on_delete = models.PROTECT,
        blank = False,
        null = False,
    )

    statusreport = models.ForeignKey(
        name = 'statusreport',
        verbose_name = 'Statusmeldung',
        to = 'processmanagement.StatusReport',
        on_delete = models.PROTECT,
        blank = False,
        null = False,
    )

    defect = models.ForeignKey(
        name = "defect",
        verbose_name = 'Defekte',
        to = 'processmanagement.Defect',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    class Meta:
        verbose_name = 'Daten'
        verbose_name_plural = 'Daten'
#--------------------------------------------------------------------------------