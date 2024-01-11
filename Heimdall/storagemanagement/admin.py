"""
#--------------------------------------------------------------------------------
# Admin File from App Storagemanagement
# 10.11.2023
# Tim Machate
#--------------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
# There are no Moduls necessary
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
# There are no Models necessary
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
# import Admin Class Booking
from storagemanagement.booking.admin import BookingAdmin
# import Admin Class Offer
from storagemanagement.offer.admin import OfferAdmin
# import Admin Class Offer Data
from storagemanagement.offerdata.admin import OfferDataAdmin
# import Admin Class Order
from storagemanagement.order.admin import OrderAdmin
# import Admin Class Order Data
from storagemanagement.orderdata.admin import OrderDataAdmin
# import Admin Class Request Data
from storagemanagement.requestdata.admin import RequestDataAdmin
# import Admin Class Supplier
from storagemanagement.supplier.admin import SupplierAdmin
# import Admin Class SupplierContact
from storagemanagement.suppliercontact.admin import SupplierContactAdmin
# import Admin Class SupplierItem
from storagemanagement.supplieritem.admin import SupplierItemAdmin
# import Admin Class Storage
from storagemanagement.storage.admin import StorageAdmin
# import Admin Class StorageItem
from storagemanagement.storageitem.admin import StorageItemAdmin
# import Admin Class StorageManagementSupplierUserSettings
from storagemanagement.storagemanagementusersetting.booking.admin import (
    StorageManagementBookingOverviewUserSettingAdmin,
    StorageManagementBookingListUserSettingAdmin,
    StorageManagementBookingTableUserSettingAdmin
)
from storagemanagement.storagemanagementusersetting.supplier.admin import (
    StorageManagementSupplierListUserSettingAdmin,
    StorageManagementSupplierTableUserSettingAdmin
)
from storagemanagement.storagemanagementusersetting.suppliercontact.admin import (
    StorageManagementSupplierContactListUserSettingAdmin,
    StorageManagementSupplierContactTableUserSettingAdmin
)
from storagemanagement.storagemanagementusersetting.supplieritem.admin import (
    StorageManagementSupplierItemOverviewUserSettingAdmin,
    StorageManagementSupplierItemListUserSettingAdmin,
    StorageManagementSupplierItemTableUserSettingAdmin
)
from storagemanagement.storagemanagementusersetting.requestdata.admin import (
    StorageManagementRequestDataListUserSettingAdmin,
    StorageManagementRequestDataTableUserSettingAdmin
)
from storagemanagement.storagemanagementusersetting.storage.admin import (
    StorageManagementStorageOverviewUserSettingAdmin,
    StorageManagementStorageListUserSettingAdmin,
    StorageManagementStorageTableUserSettingAdmin
)
from storagemanagement.storagemanagementusersetting.storageitem.admin import (
    StorageManagementStorageItemOverviewUserSettingAdmin,
    StorageManagementStorageItemListUserSettingAdmin,
    StorageManagementStorageItemTableUserSettingAdmin
)
#--------------------------------------------------------------------------------
