#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from structuremanagement.department.models import Department
from structuremanagement.position.models import Position
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'reference_number', 'name', 'url_detail']

class SectionSerializer(serializers.ModelSerializer):
    positions = PositionSerializer(many=True, read_only=True)
    class Meta:
        model = Section
        fields = ['id', 'reference_number', 'name', 'url_detail','positions']

class CompanyStructureSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(CompanyStructureSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Department
        fields = ['id', 'reference_number', 'name', 'url_detail','sections']
#--------------------------------------------------------------------------------