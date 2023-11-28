#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class BaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(BaseSerializer, self).__init__(*args, **kwargs)
        self.values = None
        fields = self.context['request'].query_params.get('values')
        if fields:
            self.values = fields.split(',')
            fields = fields.split(',')
            n = 0
            for field in fields:
                fields[n] = field.split('__')[0]
                n+=1
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
#--------------------------------------------------------------------------------
class CreateSerializer(BaseSerializer):

    create = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        if not self.values or 'create__id' in self.values or 'create' in self.values:
            result["id"] = obj.create_user_id.id
        if not self.values or 'create__date' in self.values or 'create' in self.values:
            result["date"] = obj.create_date()
        if not self.values or 'create__datetime' in self.values or 'create' in self.values:
            result["datetime"] = obj.create_datetime
        if not self.values or 'create__datetime_formated' in self.values or 'create' in self.values:
            result["datetime_formated"] = obj.create_datetime_formated()
        if not self.values or 'create__time' in self.values or 'create' in self.values:
            result["time"] = obj.create_time()
        if not self.values or 'create__username' in self.values or 'create' in self.values:
            result["username"] = obj.create_username()
        return result
#--------------------------------------------------------------------------------
class UpdateSerializer(BaseSerializer):

    update = serializers.SerializerMethodField()

    def get_update(self,obj):
        result = {}
        if not self.values or 'update__id' in self.values or 'update' in self.values:
            result["id"] = obj.update_user_id.id
        if not self.values or 'update__date' in self.values or 'update' in self.values:
            result["date"] = obj.update_date()
        if not self.values or 'update__datetime' in self.values or 'update' in self.values:
            result["datetime"] = obj.update_datetime
        if not self.values or 'update__datetime_formated' in self.values or 'update' in self.values:
            result["datetime_formated"] = obj.update_datetime_formated()
        if not self.values or 'update__time' in self.values or 'update' in self.values:
            result["time"] = obj.update_time()
        if not self.values or 'update__username' in self.values or 'update' in self.values:
            result["username"] = obj.update_username()
        return result
#--------------------------------------------------------------------------------