"""
simulate storagemanagement app
"""
# import all neccessary Models
import random

# import Faker Modul
from faker import Faker

from storagemanagement.supplier.models import Supplier
from storagemanagement.suppliercontact.models import SupplierContact
from storagemanagement.supplieritem.models import SupplierItem

from storagemanagement.storageitem.models import StorageItem

class StoragemanagementFaker():
    """
    StoragemanagementFaker
    """

    # create fake instance
    fake = Faker('de_DE')

    def create_booking(self,f=fake):
        """
        create_booking

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

    def create_suppliers(self,f=fake):
        """
        create_suppliers

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

        c = f.supplier()
        supplier_low = c.replace(" ","").lower
        obj = Supplier(
            name = c,
            street = f.street_name(),
            house_number = f.building_number(),
            post_code = f.postcode(),
            city = f.city(),
            country = f.current_country(),
            email = f"info@{supplier_low}.com",
            telephone = f.phone_number(),
            notice = f.paragraph(nb_sentences=5),
        )
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

    def create_suppliercontacts(self,f=fake):
        """
        create_suppliers

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

        co = list(Supplier.objects.all().values_list('id',flat=True))
        obj = SupplierContact(
            first_name = f.first_name(),
            last_name = f.last_name(),
            supplier = Supplier.objects.get(id=random.choice(co)),
            notice = f.paragraph(nb_sentences=2),
        )
        obj.save()
        print(f"""
        ---------------------------------------------------
        Vorname:    {obj.first_name}
        Nachname:   {obj.last_name}
        Firma:      {obj.supplier}
        Bemerkung:  {obj.notice}
        ---------------------------------------------------

        """)

    def create_supplieritems(self,f=fake):
        """
        create_suppliers

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

        co = list(Supplier.objects.all().values_list('id',flat=True))
        si = list(StorageItem.objects.all().values_list('id',flat=True))
        pr = float(random.randrange(100, 1000000))/100
        un = SupplierItem.Units.PIECE
        obj = SupplierItem(
            name = f.word(),
            item_number = f.ean(length=13),
            price = pr,
            unit = un,
            supplier = Supplier.objects.get(id=random.choice(co)),
            storageitem = StorageItem.objects.get(id=random.choice(si)),
        )
        obj.save()
        print(f"""
        ---------------------------------------------------
        Name:           {obj.name}
        Artikelnummer:  {obj.item_number}
        Preis:          {obj.price}
        Einheit:        {obj.unit}
        Firma:          {obj.supplier}
        Lagerartikel:   {obj.storageitem}
        ---------------------------------------------------

        """)

    def create_storageitems(self,f=fake):
        """
        create_suppliers

        Args:
            f (_type_, optional): _description_. Defaults to fake.
        """

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
        print(f"""
        ---------------------------------------------------
        Name:       {obj.name}
        Minimum:    {obj.minimum}
        Warnung:    {obj.warning}
        Maximum:    {obj.maximum}
        ---------------------------------------------------

        """)

    def run(self,):
        """
        create_suppliers
        """
        # creating suppliers
        n = 10
        for i in range(0,n,1):
            self.create_suppliers()

        # creating supplier contacts
        n = 15
        for i in range(0,n,1):
            self.create_suppliercontacts()

        # creating storage items
        n = 25
        for i in range(0,n,1):
            self.create_storageitems()

        # creating supplier items
        n = 75
        for i in range(0,n,1):
            self.create_supplieritems()

        for i in StorageItem.objects.all():
            if SupplierItem.objects.filter(storageitem=i).exists():
                queryset = list(
                    SupplierItem.objects.filter(
                        storageitem=i
                    ).values_list(
                        'id',
                        flat=True
                    ).distinct()
                )
                i.supplieritem = SupplierItem.objects.get(id=random.choice(queryset))
                i.save()

if __name__ == '__main__':
    StoragemanagementFaker().run()
