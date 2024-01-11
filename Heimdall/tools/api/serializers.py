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
class CreateSerializer(serializers.ModelSerializer):
    """ CreateSerializer contains all fields for info who create a object"""
    create_date = serializers.ReadOnlyField()
    create_time = serializers.ReadOnlyField()
    create_username = serializers.ReadOnlyField()
#--------------------------------------------------------------------------------
class UpdateSerializer(serializers.ModelSerializer):
    """ UpdateSerializer contains all fields for info who update a object"""
    update_date = serializers.ReadOnlyField()
    update_time = serializers.ReadOnlyField()
    update_username = serializers.ReadOnlyField()
