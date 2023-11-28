# import all neccessary Models
from storagemanagement.company.models import Company
from storagemanagement.companycontact.models import CompanyContact
from storagemanagement.companyitem.models import CompanyItem

from storagemanagement.storageitem.models import StorageItem

import random

# import Faker Modul
from faker import Faker

class StoragemanagementFaker():

    # create fake instance
    fake = Faker('de_DE')

    def create_booking(self,f=fake):
        pass

    def create_companys(self,f=fake):
        c = f.company()
        obj = Company(
            name = c,
            street = f.street_name(),
            house_number = f.building_number(),
            post_code = f.postcode(),
            city = f.city(),
            country = f.current_country(),
            email = "info@{}.com".format(c.replace(" ","")).lower(),
            telephone = f.phone_number(),
            notice = f.paragraph(nb_sentences=5),
        )
        obj.save()
        print("""
        ---------------------------------------------------
        Name:       {}
        Adresse:    {} {},{} {}
        Land:       {}
        Email:      {}
        Telefon:    {}
        Bemerkung:  {}
        ---------------------------------------------------

        """.format(obj.name,obj.street,obj.house_number,obj.post_code,obj.city,obj.country,obj.email,obj.telephone,obj.notice))

    def create_companycontacts(self,f=fake):
        co = list(Company.objects.all().values_list('id',flat=True))
        obj = CompanyContact(
            first_name = f.first_name(),
            last_name = f.last_name(),
            company = Company.objects.get(id=random.choice(co)),
            notice = f.paragraph(nb_sentences=2),
        )
        obj.save()
        print("""
        ---------------------------------------------------
        Vorname:    {}
        Nachname:   {}
        Firma:      {}
        Bemerkung:  {}
        ---------------------------------------------------

        """.format(obj.first_name,obj.last_name,obj.company,obj.notice))

    def create_companyitems(self,f=fake):
        co = list(Company.objects.all().values_list('id',flat=True))
        si = list(StorageItem.objects.all().values_list('id',flat=True))
        pr = float(random.randrange(100, 1000000))/100
        un = CompanyItem.Units.PIECE
        obj = CompanyItem(
            name = f.word(),
            item_number = f.ean(length=13),
            price = pr,
            unit = un,
            company = Company.objects.get(id=random.choice(co)),
            storageitem = StorageItem.objects.get(id=random.choice(si)),
        )
        obj.save()
        print("""
        ---------------------------------------------------
        Name:           {}
        Artikelnummer:  {}
        Preis:          {}
        Einheit:        {}
        Firma:          {}
        Lagerartikel:   {}
        ---------------------------------------------------

        """.format(obj.name,obj.item_number,obj.price,obj.unit,obj.company,obj.storageitem))

    def create_storageitems(self,f=fake):
        stock = random.randint(2,200)
        mi = int(stock*0.1)
        wa = int(stock*0.5)
        ma = int(stock)
        obj = StorageItem(
            name = f.word(),
            minimum = mi,
            warning = wa,
            maximum = ma,
        )
        obj.save()
        print("""
        ---------------------------------------------------
        Name:       {}
        Minimum:    {}
        Warnung:    {}
        Maximum:    {}
        ---------------------------------------------------

        """.format(obj.name,obj.minimum,obj.warning,obj.maximum))

    def run(self,):
        # creating companys
        n = 10
        for i in range(0,n,1):
            self.create_companys()

        # creating company contacts
        n = 15
        for i in range(0,n,1):
            self.create_companycontacts()
        
        # creating storage items
        n = 25
        for i in range(0,n,1):
            self.create_storageitems()
        
        # creating company items
        n = 75
        for i in range(0,n,1):
            self.create_companyitems()

        for i in StorageItem.objects.all():
            if CompanyItem.objects.filter(storageitem=i).exists():
                queryset = list(CompanyItem.objects.filter(storageitem=i).values_list('id',flat=True).distinct())
                i.companyitem = CompanyItem.objects.get(id=random.choice(queryset))
                i.save()