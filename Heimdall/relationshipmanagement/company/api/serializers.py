#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import Company,Email,Telephone
from relationshipmanagement.person.models import Person,EmailPerson,TelephonePerson
from relationshipmanagement.ware.models import Ware
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from main.api.serializers import CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class EmailPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailPerson
        fields = ['email',]
#--------------------------------------------------------------------------------
class TelephonePersonSerializer(serializers.ModelSerializer):

    type = serializers.SerializerMethodField()

    def get_type(self,obj):
        result = TelephonePerson.Types(obj.type).label
        return result

    class Meta:
        model = TelephonePerson
        fields = ['type','number']
#--------------------------------------------------------------------------------
class PersonSerializer(serializers.ModelSerializer):

    emails = serializers.SerializerMethodField()

    telephones = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_emails(self,obj):
        result = {}
        result["count"] = obj.emails().count()
        result["data"] = EmailPersonSerializer(instance=obj.emails(),many=True,read_only=True).data
        return result

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def get_telephones(self,obj):
        result = {}
        result["count"] = obj.telephones().count()
        result["data"] = TelephonePersonSerializer(instance=obj.telephones(),many=True,read_only=True).data
        return result

    class Meta:
        model = Person
        fields = ['id','last_name','first_name','url','telephones','emails']
#--------------------------------------------------------------------------------
class WareSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = Ware
        fields = ['id','name','ware_number','unit_package','unit','price','url']
#--------------------------------------------------------------------------------
class CompanyListSerializer(CreateSerializer,UpdateSerializer):

    emails = serializers.SerializerMethodField()

    persons = serializers.SerializerMethodField()

    telephones = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    wares = serializers.SerializerMethodField()

    def get_emails(self,obj):
        result = {}
        if not self.values or 'emails__count' in self.values or 'emails' in self.values:
            result["count"] = obj.emails().count()
        for e in obj.emails():
            dic = {}
            if not self.values or 'emails__data' in self.values or 'emails' in self.values:
                dic["id"] = e.id
            if not self.values or 'emails__data__email' in self.values or 'emails__data' in self.values or 'emails' in self.values:
                dic["email"] = e.email
            if not self.values or 'emails__data__target' in self.values or 'emails__data' in self.values or 'emails' in self.values:
                dic["target"] = e.target
            if dic:
                if "data" in result:
                    result["data"].append(dic)
                else:
                    result["data"] = []
                    result["data"].append(dic)
        return result

    def get_persons(self,obj):
        result = {}
        result["count"] = obj.persons().count()
        result["data"] = PersonSerializer(instance=obj.persons(),many=True,read_only=True).data
        return result

    def get_telephones(self,obj):
        result = {}
        if not self.values or 'telephones__count' in self.values or 'telephones' in self.values:
            result["count"] = obj.telephones().count()
        for tn in obj.telephones():
            dic = {}
            if not self.values or 'telephones__data' in self.values or 'telephones' in self.values:
                dic["id"] = tn.id
            if not self.values or 'telephones__data__type' in self.values or 'telephones__data' in self.values or 'telephones' in self.values:
                dic["type"] = Telephone.Types(tn.type).label
            if not self.values or 'telephones__data__number' in self.values or 'telephones__data' in self.values or 'telephones' in self.values:
                dic["number"] = tn.number
            if not self.values or 'telephones__data__target' in self.values or 'telephones__data' in self.values or 'telephones' in self.values:
                dic["target"] = tn.target
            if dic:
                if "data" in result:
                    result["data"].append(dic)
                else:
                    result["data"] = []
                    result["data"].append(dic)
        return result

    def get_url(self,obj):
        result = {}
        if not self.values or 'url__delete' in self.values or 'url' in self.values:
            result['delete'] = obj.url_delete()
        if not self.values or 'url__detail' in self.values or 'url' in self.values:
            result['detail'] = obj.url_detail()
        if not self.values or 'url__update' in self.values or 'url' in self.values:
            result['update'] = obj.url_update()
        return result

    def get_wares(self,obj):
        if obj.supplier_information():
            result = {}
            result["count"] = obj.supplier_information().wares().count()
            result["data"] = WareSerializer(instance=obj.supplier_information().wares(),many=True,read_only=True).data
        else:
            result=None
        return result

    class Meta:
        model = Company
        exclude = [
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class CompanyDetailSerializer(CreateSerializer,UpdateSerializer):

    emails = serializers.SerializerMethodField()

    persons = serializers.SerializerMethodField()

    telephones = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    wares = serializers.SerializerMethodField()

    def get_emails(self,obj):
        result = {}
        result["count"] = obj.emails().count()
        result["data"] = []
        for e in obj.emails():
            dic = {}
            if not self.values or 'emails__data' in self.values or 'emails' in self.values:
                dic["id"] = e.id
            if not self.values or 'emails__email' in self.values or 'emails' in self.values:
                dic["email"] = e.email
            if not self.values or 'emails__target' in self.values or 'emails' in self.values:
                dic["target"] = e.target
            result["data"].append(dic)
        return result

    def get_persons(self,obj):
        result = {}
        result["count"] = obj.persons().count()
        result["data"] = PersonSerializer(instance=obj.persons(),many=True,read_only=True).data
        return result

    def get_telephones(self,obj):
        result = {}
        result["count"] = obj.telephones().count()
        result["data"] = []
        for tn in obj.telephones():
            dic = {}
            if not self.values or 'telephones__data' in self.values or 'telephones' in self.values:
                dic["id"] = tn.id
            if not self.values or 'telephones__type' in self.values or 'telephones' in self.values:
                dic["type"] = Telephone.Types(tn.type).label
            if not self.values or 'telephones__number' in self.values or 'telephones' in self.values:
                dic["number"] = tn.number
            if not self.values or 'telephones__target' in self.values or 'telephones' in self.values:
                dic["target"] = tn.target
            result["data"].append(dic)
        return result

    def get_url(self,obj):
        result = {}
        if not self.values or 'url__delete' in self.values or 'url' in self.values:
            result['delete'] = obj.url_delete()
        if not self.values or 'url__detail' in self.values or 'url' in self.values:
            result['detail'] = obj.url_detail()
        if not self.values or 'url__update' in self.values or 'url' in self.values:
            result['update'] = obj.url_update()
        return result

    def get_wares(self,obj):
        if obj.supplier_information():
            result = {}
            result["count"] = obj.supplier_information().wares().count()
            result["data"] = WareSerializer(instance=obj.supplier_information().wares(),many=True,read_only=True).data
        else:
            result=None
        return result

    class Meta:
        model = Company
        exclude = [
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------