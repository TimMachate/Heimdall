#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from relationshipmanagement.company.models import Company
from relationshipmanagement.person.models import Person,EmailPerson,TelephonePerson
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
from main.api.serializers import CreateSerializer,UpdateSerializer
#--------------------------------------------------------------------------------
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','reference_number','url_detail']
#--------------------------------------------------------------------------------
class PersonListSerializer(CreateSerializer,UpdateSerializer):

    company = CompanySerializer(source='company_id',many=False,read_only=True)

    emails = serializers.SerializerMethodField()

    telephones = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

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
            if dic:
                if "data" in result:
                    result["data"].append(dic)
                else:
                    result["data"] = []
                    result["data"].append(dic)
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
                dic["type"] = TelephonePerson.Types(tn.type).label
            if not self.values or 'telephones__data__number' in self.values or 'telephones__data' in self.values or 'telephones' in self.values:
                dic["number"] = tn.number
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

    class Meta:
        model = Person
        exclude = [
            'company_id',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------
class PersonDetailSerializer(CreateSerializer,UpdateSerializer):

    company = CompanySerializer(source='company_id',many=False,read_only=True)

    emails = serializers.SerializerMethodField()

    telephones = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

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
            result["data"].append(dic)
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
                dic["type"] = TelephonePerson.Types(tn.type).label
            if not self.values or 'telephones__number' in self.values or 'telephones' in self.values:
                dic["number"] = tn.number
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

    class Meta:
        model = Person
        exclude = [
            'company_id',
            'create_user_id',
            'create_datetime',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------