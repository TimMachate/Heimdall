#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from rest_framework import serializers
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.file.models import DirectionProxy, DocumentProxy, PictureProxy, SafetyDataSheetProxy, WorkingDescriptionProxy, WorkingInstructionProxy
from personalmanagement.employee.models import Employee
from structuremanagement.department.models import Department
from structuremanagement.position.models import Position
from structuremanagement.section.models import Section
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Serializer
#--------------------------------------------------------------------------------
class DirectionSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = DirectionProxy
        fields = ['id','reference_number','name','url_detail','url_file']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','reference_number','name','url_detail']

class DocumentSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = DirectionProxy
        fields = ['id','reference_number','name','url_detail','url_file']

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

class ResponsibleSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ['id','reference_number','name','telephone','email','url_detail']

class SafetyDataSheetSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = SafetyDataSheetProxy
        fields = ['id','reference_number','name','url_detail','url_file']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id','reference_number','name','url_detail']

class SubstituteSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ['id','reference_number','name','telephone','email','url_detail']

class WorkingDescriptionSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = WorkingDescriptionProxy
        fields = ['id','reference_number','name','url_detail','url_file']

class WorkingInstructionSerializer(serializers.ModelSerializer):

    url_file = serializers.SerializerMethodField()

    def get_url_file(self,obj):
        result = obj.file.url
        return result

    class Meta:
        model = WorkingInstructionProxy
        fields = ['id','reference_number','name','url_detail','url_file']

class PositionListSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    department = DepartmentSerializer(many=False,read_only=True)

    directions = serializers.SerializerMethodField()

    documents = serializers.SerializerMethodField()

    employee_count = serializers.SerializerMethodField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    responsible = EmployeeSerializer(source="responsible_employee_id",many=False,read_only=True)

    safety_data_sheets = serializers.SerializerMethodField()

    section = SectionSerializer(source="section_id",many=False,read_only=True)

    substitute = EmployeeSerializer(source="substitute_employee_id",many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    working_description = WorkingDescriptionSerializer(source="working_description_id", many=False , read_only=True)

    working_instructions = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result

    def get_directions(self,obj):
        result = {}
        result["data"] = DirectionSerializer(instance=obj.directions,many=True , read_only=True).data if obj.directions else None
        result["count"] = obj.directions.count()
        return result

    def get_documents(self,obj):
        result = {}
        result["data"] = DocumentSerializer(instance=obj.documents,many=True , read_only=True).data if obj.documents else None
        result["count"] = obj.documents.count()
        return result

    def get_employee_count(self,obj):
        result = obj.employees.count()
        return result

    def get_safety_data_sheets(self,obj):
        result = {}
        result["data"] = SafetyDataSheetSerializer(instance=obj.safety_data_sheets,many=True,read_only=True).data if obj.safety_data_sheets else None
        result["count"] = obj.safety_data_sheets.count()
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

    def get_working_instructions(self,obj):
        result = {}
        result["data"] = WorkingInstructionSerializer(instance=obj.working_instructions,many=True,read_only=True).data if obj.working_instructions else None
        result["count"] = obj.working_instructions.count()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(PositionListSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Position
        exclude = [
            'create_user_id',
            'create_datetime',
            'employees',
            'picture_id',
            'responsible_employee_id',
            'section_id',
            'substitute_employee_id',
            'update_user_id',
            'update_datetime',
            'working_description_id'
            ]
#--------------------------------------------------------------------------------
class PositionDetailSerializer(serializers.ModelSerializer):

    create = serializers.SerializerMethodField()

    department = DepartmentSerializer(many=False,read_only=True)

    directions = serializers.SerializerMethodField()

    documents = serializers.SerializerMethodField()

    employees = serializers.SerializerMethodField()

    picture = PictureSerializer(source="picture_id",many=False,read_only=True)

    responsible = EmployeeSerializer(source="responsible_employee_id",many=False,read_only=True)

    safety_data_sheets = serializers.SerializerMethodField()

    section = SectionSerializer(source="section_id",many=False,read_only=True)

    substitute = EmployeeSerializer(source="substitute_employee_id",many=False,read_only=True)

    update = serializers.SerializerMethodField()

    url_detail = serializers.ReadOnlyField()
    url_update = serializers.ReadOnlyField()
    url_delete = serializers.ReadOnlyField()

    working_description = WorkingDescriptionSerializer(source="working_description_id", many=False , read_only=True)

    working_instructions = serializers.SerializerMethodField()

    def get_create(self,obj):
        result = {}
        result["id"] = obj.create_user_id.id
        result["date"] = obj.create_date()
        result["datetime"] = obj.create_datetime
        result["datetime_formated"] = obj.create_datetime_formated()
        result["time"] = obj.create_time()
        result["username"] = obj.create_username()
        return result

    def get_directions(self,obj):
        result = {}
        result["data"] = DirectionSerializer(instance=obj.directions,many=True , read_only=True).data if obj.directions else None
        result["count"] = obj.directions.count()
        return result

    def get_documents(self,obj):
        result = {}
        result["data"] = DocumentSerializer(instance=obj.documents,many=True , read_only=True).data if obj.documents else None
        result["count"] = obj.documents.count()
        return result

    def get_employees(self,obj):
        result = {}
        result["data"] = EmployeeSerializer(instance=obj.employees,many=True,read_only=True).data if obj.employees else None
        result["count"] = obj.employees.count()
        return result

    def get_safety_data_sheets(self,obj):
        result = {}
        result["data"] = SafetyDataSheetSerializer(instance=obj.safety_data_sheets,many=True,read_only=True).data if obj.safety_data_sheets else None
        result["count"] = obj.safety_data_sheets.count()
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

    def get_working_instructions(self,obj):
        result = {}
        result["data"] = WorkingInstructionSerializer(instance=obj.working_instructions,many=True,read_only=True).data if obj.working_instructions else None
        result["count"] = obj.working_instructions.count()
        return result

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(PositionDetailSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('values')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Position
        exclude = [
            'create_user_id',
            'create_datetime',
            'picture_id',
            'responsible_employee_id',
            'section_id',
            'substitute_employee_id',
            'update_user_id',
            'update_datetime',
            'working_description_id'
            ]
#--------------------------------------------------------------------------------