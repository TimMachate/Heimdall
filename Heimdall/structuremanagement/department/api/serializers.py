#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import PictureProxy
from personalmanagement.employee.models import Employee
from structuremanagement.department.models import Department
from structuremanagement.position.models import Position
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class EmployeeSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = Employee
        fields = ['id','reference_number','name','telephone','email','url']

class PictureSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = PictureProxy
        fields = ['id','reference_number','name','url_detail','url_file']

class PositionSerializer(serializers.ModelSerializer):

    section = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_section(self,obj):
        result = {}
        result["id"] = obj.section_id.id
        result["name"] = obj.section_id.name
        result["url_detail"] = obj.section_id.url_detail()
        return result
    
    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = Position
        fields = ['id','reference_number','name','section','url']

class ProcessInstructionSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = PictureProxy
        fields = ['id','reference_number','name','url_detail','url_file']

class SectionSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    class Meta:
        model = Section
        fields = ['id','reference_number','name','url_detail','url']
#--------------------------------------------------------------------------------
class DepartmentListSerializer(serializers.ModelSerializer):

    color = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    employee_count = serializers.SerializerMethodField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    position_count = serializers.SerializerMethodField()

    process_instruction = ProcessInstructionSerializer(source="process_instruction_id", many=False , read_only=True)

    responsible = EmployeeSerializer(source="responsible_employee_id",many=False,read_only=True)

    section_count = serializers.SerializerMethodField()

    substitute = EmployeeSerializer(source="substitute_employee_id",many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    def get_color(self,obj):
        result = {}
        result["value"] = obj.rgba_value()
        result["style"] = obj.rgba_style()
        result["red"] = obj.rgba_red
        result["green"] = obj.rgba_green
        result["blue"] = obj.rgba_blue
        result["alpha"] = obj.rgba_alpha
        return result

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result
    
    def get_employee_count(self,obj):
        result = obj.employees().count()
        return result

    def get_position_count(self,obj):
        result = obj.positions().count()
        return result

    def get_section_count(self,obj):
        result = obj.sections().count()
        return result

    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username()
        return result
    
    def get_url(self,obj):
        result = {}
        result['delete'] = obj.url_delete()
        result['detail'] = obj.url_detail()
        result['update'] = obj.url_update()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DepartmentListSerializer, self).__init__(*args, **kwargs)
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
        exclude = [
            'create_datetime',
            'create_user_id',
            'picture_id',
            'process_instruction_id',
            'responsible_employee_id',
            'rgba_alpha',
            'rgba_blue',
            'rgba_green',
            'rgba_red',
            'substitute_employee_id',
            'update_datetime',
            'update_user_id',
        ]
#--------------------------------------------------------------------------------
class DepartmentDetailSerializer(serializers.ModelSerializer):

    color = serializers.SerializerMethodField()

    create = serializers.SerializerMethodField()

    employees = serializers.SerializerMethodField()

    order = serializers.ReadOnlyField()

    picture = PictureSerializer(source="picture_id", many=False, read_only=True)

    positions = serializers.SerializerMethodField()

    process_instructions = ProcessInstructionSerializer(source="process_instruction_id", many=False , read_only=True)

    responsible = EmployeeSerializer(source="responsible_employee_id",many=False,read_only=True)

    sections = serializers.SerializerMethodField()

    substitute = EmployeeSerializer(source="substitute_employee_id",many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url_detail = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()
    url_delete = serializers.ReadOnlyField()

    def get_color(self,obj):
        result = {}
        result["value"] = obj.rgba_value()
        result["style"] = obj.rgba_style()
        result["red"] = obj.rgba_red
        result["green"] = obj.rgba_green
        result["blue"] = obj.rgba_blue
        result["alpha"] = obj.rgba_alpha
        return result

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result

    def get_employees(self,obj):
        result = {}
        result["data"] = EmployeeSerializer(instance=obj.employees(),many=True,read_only=True).data if obj.employees() else None
        result["count"] = obj.employees().count()
        return result

    def get_positions(self,obj):
        result = {}
        result["data"] = PositionSerializer(instance=obj.positions(),many=True,read_only=True).data if obj.positions() else None
        result["count"] = obj.positions().count()
        return result

    def get_sections(self,obj):
        result = {}
        result["data"] = SectionSerializer(instance=obj.sections(),many=True,read_only=True).data if obj.sections() else None
        result["count"] = obj.sections().count()
        return result
    
    def get_update(self,obj):
        result = {}
        result["id"] = obj.update_user_id.id
        result["date"] = obj.update_date()
        result["datetime"] = obj.update_datetime
        result["datetime_formated"] = obj.update_datetime_formated()
        result["time"] = obj.update_time()
        result["username"] = obj.update_username()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DepartmentDetailSerializer, self).__init__(*args, **kwargs)
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
        exclude = [
            'create_user_id',
            'create_datetime',
            'picture_id',
            'process_instruction_id',
            'responsible_employee_id',
            'rgba_red',
            'rgba_green',
            'rgba_blue',
            'rgba_alpha',
            'substitute_employee_id',
            'update_user_id',
            'update_datetime',
            ]
#--------------------------------------------------------------------------------