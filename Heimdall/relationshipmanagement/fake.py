"""
simulate relationshipmanagement app
"""
# import all neccessary Models
import random

# import Faker Modul
from faker import Faker

from relationshipmanagement.company.models import Company
from relationshipmanagement.companycontact.models import (
    CompanyContact,
    CompanyContactEmail,
    CompanyContactTelephone
)
from relationshipmanagement.companyitem.models import CompanyItem

class RelationshipManagementFaker():
    """
    RelationshipmanagementFaker
    """

    # create fake instance
    fake = Faker('de_DE')

    def __init__(
        self,
        company_count = 0,
        contact_count = 0,
        item_count = 0,
    ):
        """
        Initialisierung

        Args:
            company_count (int, optional): count of companys. Defaults to 0.
            contact_count (int, optional): count of contacts. Defaults to 0.
            item_count (int, optional): count of item. Defaults to 0.
        """
        self.company_count = company_count
        self.contact_count = contact_count
        self.item_count = item_count

    def create_companys(self,f=fake):
        """
        create_companys

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

        c = f.company()
        company_low = c.replace(" ","-").lower()
        obj = Company(
            name = c,
            street = f.street_name(),
            house_number = f.building_number(),
            post_code = f.postcode(),
            city = f.city(),
            country = f.current_country(),
            email = f"info@{company_low}.com",
            telephone = f.phone_number(),
            notice = f.paragraph(nb_sentences=5),
        )
        # supplier yes or no
        possibility = True if random.randint(0,100) < 80 else False
        obj.supplier = possibility
        obj.save()
        print(f"""
        ---------------------------------------------------
        Name:       {obj.name}
        Adresse:    {obj.street} {obj.house_number},{obj.post_code} {obj.city}
        Land:       {obj.country}
        Email:      {obj.email}
        Telefon:    {obj.telephone}
        Bemerkung:  {obj.notice}
        ---------------------------------------------------

        """)

    def create_companycontacts(self,f=fake):
        """
        create_companys

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

        co = list(Company.objects.all().values_list('id',flat=True))
        obj = CompanyContact(
            first_name = f.first_name(),
            last_name = f.last_name(),
            company = Company.objects.get(id=random.choice(co)),
            notice = f.paragraph(nb_sentences=2),
        )
        obj.save()
        comp = obj.company.name.replace(" ","-").lower
        email = CompanyContactEmail(
            email = f"{obj.first_name.lower()}.{obj.last_name.lower()}@{comp}.com",
            companycontact = obj,
        )
        email.save()
        telephone = CompanyContactTelephone(
            number = f.phone_number(),
            companycontact = obj
        )
        telephone.save()
        print(f"""
        ---------------------------------------------------
        Vorname:    {obj.first_name}
        Nachname:   {obj.last_name}
        Firma:      {obj.company}
        Bemerkung:  {obj.notice}
        ---------------------------------------------------

        """)

    def create_companyitems(self,f=fake):
        """
        create_companys

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

        co = list(Company.objects.filter(supplier=True).values_list('id',flat=True))
        pr = float(random.randrange(100, 1000000))/100
        un = CompanyItem.Units.PIECE
        obj = CompanyItem(
            name = f.word(),
            item_number = f.ean(length=13),
            price = pr,
            unit = un,
            company = Company.objects.get(id=random.choice(co)),
        )
        obj.save()
        print(f"""
        ---------------------------------------------------
        Name:           {obj.name}
        Artikelnummer:  {obj.item_number}
        Preis:          {obj.price}
        Einheit:        {obj.unit}
        Firma:          {obj.company}
        ---------------------------------------------------

        """)

    def run(
        self,
        company=0,
        contact=0,
        item=0
    ):
        """
        Generator for company, contact and item 

        Args:
            company (int, optional): Count of companys. Defaults to 0.
            contact (int, optional): Count of contacts. Defaults to 0.
            item (int, optional): Count of items. Defaults to 0.
        """
        # define counts
        company = company if company != 0 else self.company_count
        contact = contact if contact != 0 else self.contact_count
        item = item if item != 0 else self.item_count

        # creating companys
        i = 0
        while i < company:
            self.create_companys()
            i+=1

        # creating company contacts
        i = 0
        while i < contact:
            self.create_companycontacts()
            i+=1

        # creating company items
        i = 0
        while i < item:
            self.create_companyitems()
            i+=1

if __name__ == '__main__':
    RelationshipManagementFaker(
        company_count = 25,
        contact_count = 40,
        item_count = 75
    ).run()
