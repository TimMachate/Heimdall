"""
#--------------------------------------------------------------------------------
# Models File from Model SupplierContact
# 25.10.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.companycontact.models import (
    CompanyContactBaseModel,
    CompanyContactEmailBaseModel,
    CompanyContactTelephoneBaseModel
)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Model
#--------------------------------------------------------------------------------
class SupplierContact(CompanyContactBaseModel):
    """
    SupplierContact

    Args:
        SupplierContactBaseModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Supplier
    def supplier_id(self):
        """
        supplier_id

        Returns:
            int: id from supplier
        """
        result = self.company.id if self.company else None
        return result

    def supplier_name(self):
        """
        supplier_name

        Returns:
            string: name of supplier
        """
        result = self.company.name if self.company else None
        return result

    def supplier_reference_number(self):
        """
        supplier_reference_number

        Returns:
            string: reference number of supplier
        """
        result = self.company.reference_number if self.company else None
        return result

    def supplier_slug(self):
        """
        supplier_slug

        Returns:
            string: slug of supplier
        """
        result = self.company.slug if self.company else None
        return result

    def supplier_url_detail(self):
        """
        supplier_url_detail

        Returns:
            string: url of supplier detail page
        """
        return reverse(
                'storagemanagement:supplier_detail',
                kwargs={'supplier':self.supplier_slug()}
            )

    # Fields/Methodes for the email
    def emails(self):
        """
        emails

        Returns:
            queryset: contains all emails of contact
        """
        result = SupplierContactEmail.objects.filter(companycontact = self)
        if result == []:
            result = None
        return result

    def email_count(self):
        """
        email_count

        Returns:
            int: email count of contact
        """
        queryset = self.emails()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the name
    def name(self):
        """
        name

        Returns:
            string: name of the contact
        """
        if self.last_name and self.first_name:
            result = str(self.last_name) + ', ' + str(self.first_name)
        elif self.last_name and not self.first_name:
            result = str(self.last_name)
        elif not self.last_name and self.first_name:
            result = str(self.first_name)
        else:
            result = self.reference_number
        return result

    # Fields/Methodes for the telephone numbers
    def telephones(self):
        """
        telephones

        Returns:
            queryset: contains all telephone numbers of contact
        """
        result = SupplierContactTelephone.objects.filter(companycontact = self)
        if result == []:
            result = None
        return result

    def telephone_count(self):
        """
        telephone_count

        Returns:
            int: count of the telephone numbers
        """
        queryset = self.telephones()
        result = queryset.count() if queryset else 0
        return result

    # Fields/Methodes for the urls
    def url_detail(self):
        """
        url_detail

        Returns:
            string: url to detail page
        """
        return reverse(
            'storagemanagement:suppliercontact_detail',
            kwargs={"suppliercontact":self.slug}
        )

    def url_delete(self):
        """
        url_delete

        Returns:
            string: url to delete page
        """
        return reverse(
            'storagemanagement:suppliercontact_delete',
            kwargs={"suppliercontact":self.slug}
        )

    def url_qrcode(self):
        """
        url_qrcode

        Returns:
            string: url to qrcode page
        """
        return 'http://'+settings.HOST+self.url_detail()

    def url_update(self):
        """
        url_update

        Returns:
            string: url to update page
        """
        return reverse(
            'storagemanagement:suppliercontact_update',
            kwargs={"suppliercontact":self.slug}
        )

    def __str__(self):
        return f"{str(self.name())} ({str(self.reference_number)})"

    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'storagemanagement'
        ordering = []
        default_permissions = ()
        permissions = (
            ('add_suppliercontact','SupplierContact can view create'),
            ('change_suppliercontact','SupplierContact can view change'),
            ('delete_suppliercontact','SupplierContact can view delete'),
            ('detail_suppliercontact','SupplierContact can view detail'),
            ('list_suppliercontact','SupplierContact can view list'),
            ('table_suppliercontact','SupplierContact can view table'),
            ('view_suppliercontact','SupplierContact can view overview'),
        )
        proxy = True
        verbose_name = "Lieferantkontakt"
        verbose_name_plural = "Lieferantenkontakte"
#--------------------------------------------------------------------------------
class SupplierContactEmail(CompanyContactEmailBaseModel):
    """
    SupplierContactEmail

    Args:
        SupplierContactEmailBaseModel (_type_): _description_
    """
    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        proxy = True
        verbose_name = "Email"
        verbose_name_plural = "Emails"
#--------------------------------------------------------------------------------
class SupplierContactTelephone(CompanyContactTelephoneBaseModel):
    """
    SupplierContactTelephone

    Args:
        SupplierContactTelephoneBaseModel (_type_): _description_
    """
    class Meta:
        """
        contains all Meta data of the model
        """
        app_label = 'storagemanagement'
        default_permissions = ()
        proxy = True
        verbose_name = "Telefonnummer"
        verbose_name_plural = "Telefonnummern"
#--------------------------------------------------------------------------------
