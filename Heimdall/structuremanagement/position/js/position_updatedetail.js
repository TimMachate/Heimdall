function position_updatedetail(api_data_url) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.picture && document.getElementById("id_image_file_url")){
                        document.getElementById("id_image_file_url").setAttribute("src",dataset.picture.url_file);
                    };
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.short_form && document.getElementById("id_short_form")){
                        document.getElementById("id_short_form").setAttribute("value",dataset.short_form);
                    };
                    if(dataset.section){
                        if(dataset.section.name && dataset.section.reference_number && document.getElementById("id_section_id")){
                            document.getElementById("id_section_id").setAttribute("value",dataset.section.name+" ("+dataset.section.reference_number+")");
                        };
                        if(dataset.section.url_detail && document.getElementById("id_section_id_url_detail")){
                            document.getElementById("id_section_id_url_detail").setAttribute("href",dataset.section.url_detail);
                        };
                    };
                    if(dataset.department){
                        if(dataset.department.name && dataset.department.reference_number && document.getElementById("id_department_id")){
                            document.getElementById("id_department_id").setAttribute("value",dataset.department.name+" ("+dataset.department.reference_number+")");
                        };
                        if(dataset.department.url_detail && document.getElementById("id_department_id_url_detail")){
                            document.getElementById("id_department_id_url_detail").setAttribute("href",dataset.department.url_detail);
                        };
                    };
                    if(dataset.create){
                        if(dataset.create.date && dataset.create.time && document.getElementById('id_create_datetime')){
                            document.getElementById('id_create_datetime').setAttribute('value',dataset.create.date+' '+dataset.create.time);
                        };
                        if(dataset.create.username && document.getElementById('id_create_username')){
                            document.getElementById('id_create_username').setAttribute('value',dataset.create.username);
                        };
                    };
                    if(dataset.update){
                        if(dataset.update.date && dataset.create.time && document.getElementById('id_update_datetime')){
                            document.getElementById('id_update_datetime').setAttribute('value',dataset.update.date+' '+dataset.create.time);
                        };
                        if(dataset.update.username && document.getElementById('id_update_username')){
                            document.getElementById('id_update_username').setAttribute('value',dataset.update.username);
                        };
                    };
                    if(dataset.picture){
                        if(dataset.picture.url_file && document.getElementById('id_picture_id_url_file')){
                            document.getElementById('id_picture_id_url_file').setAttribute('href',dataset.picture.url_file);
                        };
                        if(dataset.picture.name && dataset.picture.url_detail && document.getElementById('id_picture_id_url_detail')){
                            document.getElementById('id_picture_id_url_detail').setAttribute('href',dataset.picture.url_detail);
                            document.getElementById('id_picture_id_url_detail').innerHTML = dataset.picture.name;
                        };
                    };
                    if(dataset.working_description && document.getElementById('id_working_description_id_url_file')){
                        if(dataset.working_description.url_file){
                            document.getElementById('id_working_description_id_url_file').setAttribute('href',dataset.working_description.url_file);
                        };
                        if(dataset.working_description.name && dataset.working_description.url_detail && document.getElementById('id_working_description_id_url_detail')){
                            document.getElementById('id_working_description_id_url_detail').setAttribute('href',dataset.working_description.url_detail);
                            document.getElementById('id_working_description_id_url_detail').innerHTML = dataset.working_description.name;
                        };
                    };
                    if(dataset.responsible){
                        if(dataset.responsible.name && document.getElementById('id_responsible_employee_id')){
                            document.getElementById('id_responsible_employee_id').setAttribute('value',dataset.responsible.name);
                        };
                        if(dataset.responsible.email && document.getElementById('id_responsible_email')){
                            document.getElementById('id_responsible_email').innerHTML = dataset.responsible.email;
                        };
                        if(dataset.responsible.telephone && document.getElementById('id_responsible_telephone')){
                            document.getElementById('id_responsible_telephone').innerHTML = dataset.responsible.telephone;
                        };
                    };
                    if(dataset.substitute){
                        if(dataset.substitute.name && document.getElementById('id_substitute_employee_id')){
                            document.getElementById('id_substitute_employee_id').setAttribute('value',dataset.substitute.name);
                        };
                        if(dataset.substitute.email && document.getElementById('id_substitute_email')){
                            document.getElementById('id_substitute_email').innerHTML = dataset.substitute.email;
                        };
                        if(dataset.substitute.telephone && document.getElementById('id_substitute_telephone')){
                            document.getElementById('id_substitute_telephone').innerHTML = dataset.substitute.telephone;
                        };
                    };
                    if(dataset.description && document.getElementById('id_description')){
                        document.getElementById('id_description').innerHTML = dataset.description;
                    };
                    if(dataset.employees && document.getElementById('id_employees_count')){
                        document.getElementById('id_employees_count').innerHTML = dataset.employees.count;
                    };
                    if(dataset.directions){
                        if(dataset.directions.data){
                            dataset.directions.data.forEach(element => {
                                if(element.url_file && document.getElementById('id_directions_url_file-'+element.id)){
                                    document.getElementById('id_directions_url_file-'+element.id).setAttribute('href',element.url_file);
                                };
                                if(element.name && element.url_detail && document.getElementById('id_directions_url_detail-'+element.id)){
                                    document.getElementById('id_directions_url_detail-'+element.id).setAttribute('href',element.url_detail);
                                    document.getElementById('id_directions_url_detail-'+element.id).innerHTML = element.name;
                                };
                            });
                        };
                    };
                    if(dataset.documents){
                        if(dataset.documents.data){
                            dataset.documents.data.forEach(element => {
                                if(element.url_file && document.getElementById('id_documents_url_file-'+element.id)){
                                    document.getElementById('id_documents_url_file-'+element.id).setAttribute('href',element.url_file);
                                };
                                if(element.name && element.url_detail && document.getElementById('id_documents_url_detail-'+element.id)){
                                    document.getElementById('id_documents_url_detail-'+element.id).setAttribute('href',element.url_detail);
                                    document.getElementById('id_documents_url_detail-'+element.id).innerHTML = element.name;
                                };
                            });
                        };
                    };
                    if(dataset.safety_data_sheets){
                        if(dataset.safety_data_sheets.data){
                            dataset.safety_data_sheets.data.forEach(element => {
                                if(element.url_file && document.getElementById('id_safety_data_sheets_url_file-'+element.id)){
                                    document.getElementById('id_safety_data_sheets_url_file-'+element.id).setAttribute('href',element.url_file);
                                };
                                if(element.name && element.url_detail && document.getElementById('id_safety_data_sheets_url_detail-'+element.id)){
                                    document.getElementById('id_safety_data_sheets_url_detail-'+element.id).setAttribute('href',element.url_detail);
                                    document.getElementById('id_safety_data_sheets_url_detail-'+element.id).innerHTML = element.name;
                                };
                            });
                        };
                    };
                    if(dataset.working_instructions){
                        if(dataset.working_instructions.data){
                            dataset.working_instructions.data.forEach(element => {
                                if(element.url_file && document.getElementById('id_working_instructions_url_file-'+element.id)){
                                    document.getElementById('id_working_instructions_url_file-'+element.id).setAttribute('href',element.url_file);
                                };
                                if(element.name && element.url_detail && document.getElementById('id_working_instructions_url_detail-'+element.id)){
                                    document.getElementById('id_working_instructions_url_detail-'+element.id).setAttribute('href',element.url_detail);
                                    document.getElementById('id_working_instructions_url_detail-'+element.id).innerHTML = element.name;
                                };
                            });
                        };
                    };
                    if(dataset.employees.data){
                        let col_employees = [
                            {
                                "name":"id",
                                "data":"",
                                "defaultContent": "",
                                "width":"10px",
                                "className":"",
                                "visible":true,
                            },
                            {
                                "name":"reference_number",
                                "data":"reference_number",
                                "defaultContent": "",
                                "className":"",
                                "visible": "reference_number" in dataset.employees.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        return '<a class="link-dark" href="'+ row.url_detail +'">'+row.reference_number+'</a>'
                                    } else {
                                        return row.reference_number
                                    }
                                }
                            },
                            {
                                "name":"name",
                                "data":"name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "name" in dataset.employees.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        return '<a class="link-dark" href="'+ row.url_detail +'">'+row.name+'</a>'
                                    } else {
                                        return row.name
                                    }
                                }
                            },
                            {
                                "name":"url",
                                "data":"url",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url" in dataset.employees.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url){
                                        if (row.url.detail){
                                            detail = '<a class="btn btn-primary" href="'+ row.url.detail +'"><i class="fas fa-search"></i></a>'
                                        } else {detail = ""};
                                        if (row.url.update){
                                            update = '<a class="btn btn-primary" href="'+ row.url.update +'"><i class="fas fa-pen"></i></a>'
                                        } else {update = ""};
                                        if (row.url.delete){
                                            del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                        } else {del = ""};
                                        return '<div class="btn-group">'+detail+update+del+'</div>'
                                    };
                                }
                            },
                        ];
                        transformTable("employees",dataset.employees.data,col_employees,[[2,"asc"]]);
                    };
                };
            },
        });
        
    });
}