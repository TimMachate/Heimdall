#--------------------------------------------------------------------------------
# serializers File from App Storagemanagement API
# 27.10.2023
# Tim Machate
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.apps import apps
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
if 'tools' in [app.name for app in apps.get_app_configs()]:
    from tools.api.serializers import (
        BaseSerializer,
        CreateSerializer,
        UpdateSerializer
        )
else:
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
        create_date = serializers.ReadOnlyField()
        create_time = serializers.ReadOnlyField()
        create_username = serializers.ReadOnlyField()
    #--------------------------------------------------------------------------------
    class UpdateSerializer(serializers.ModelSerializer):
        update_date = serializers.ReadOnlyField()
        update_time = serializers.ReadOnlyField()
        update_username = serializers.ReadOnlyField()
    #--------------------------------------------------------------------------------