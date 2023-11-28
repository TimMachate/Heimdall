function section_updatedetail(api_data_url){
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
                    if(dataset.department){
                        if(dataset.department.name && dataset.department.reference_number){
                            document.getElementById("id_department_id").setAttribute("value",dataset.department.name+" ("+dataset.department.reference_number+")");
                        };
                        if(dataset.department.url_detail && document.getElementById("id_department_id_url_detail")){
                            document.getElementById("id_department_id_url_detail").setAttribute("href",dataset.department.url_detail);
                        };
                    };
                    if(dataset.color){
                        if(dataset.color.value && document.getElementById("id_color")){
                            document.getElementById("id_color").setAttribute("style",'background-color:rgba('+dataset.color.value+')');
                        };
                        if(dataset.color.red && document.getElementById("id_rgba_red")){
                            document.getElementById("id_rgba_red").setAttribute("value",dataset.color.red);
                        };
                        if(dataset.color.green && document.getElementById("id_rgba_green")){
                            document.getElementById("id_rgba_green").setAttribute("value",dataset.color.green);
                        };
                        if(dataset.color.blue && document.getElementById("id_rgba_blue")){
                            document.getElementById("id_rgba_blue").setAttribute("value",dataset.color.blue);
                        };
                        if(dataset.color.alpha && document.getElementById("id_rgba_alpha")){
                            document.getElementById("id_rgba_alpha").setAttribute("value",dataset.color.alpha);
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
                            document.getElementById('id_picture_id_url_detail').innerHTML = dataset.picture.name
                        };
                    };
                    if(dataset.process_instruction){
                        if(dataset.process_instruction.url_file && document.getElementById('id_process_instruction_id_url_file')){
                            document.getElementById('id_process_instruction_id_url_file').setAttribute('href',dataset.process_instruction.url_file);
                        };
                        if(dataset.process_instruction.name && dataset.process_instruction.url_detail && document.getElementById('id_process_instruction_id_url_detail')){
                            document.getElementById('id_process_instruction_id_url_detail').setAttribute('href',dataset.process_instruction.url_detail);
                            document.getElementById('id_process_instruction_id_url_detail').innerHTML = dataset.process_instruction.name
                        };
                    };
                    if(dataset.responsible){
                        if(dataset.responsible.name && document.getElementById('id_responsible_employee_id')){
                            document.getElementById('id_responsible_employee_id').setAttribute('value',dataset.responsible.name);
                        };
                        if(dataset.responsible.email && document.getElementById('id_responsible_email')){
                            document.getElementById('id_responsible_email').innerHTML = dataset.responsible.email
                        };
                        if(dataset.responsible.telephone && document.getElementById('id_responsible_telephone')){
                            document.getElementById('id_responsible_telephone').innerHTML = dataset.responsible.telephone
                        };
                    };
                    if(dataset.substitute){
                        if(dataset.substitute.name && document.getElementById('id_substitute_employee_id')){
                            document.getElementById('id_substitute_employee_id').setAttribute('value',dataset.substitute.name);
                        };
                        if(dataset.substitute.email && document.getElementById('id_substitute_email')){
                            document.getElementById('id_substitute_email').innerHTML = dataset.substitute.email
                        };
                        if(dataset.substitute.telephone && document.getElementById('id_substitute_telephone')){
                            document.getElementById('id_substitute_telephone').innerHTML = dataset.substitute.telephone
                        };
                    };
                    if (dataset.positions){
                        if (dataset.positions.count && document.getElementById('id_positions_count')){
                            document.getElementById('id_positions_count').innerHTML = dataset.positions.count
                        };
                    };
                    if (dataset.employees){
                        if (dataset.employees.count && document.getElementById('id_employees_count')){
                            document.getElementById('id_employees_count').innerHTML = dataset.employees.count
                        };
                    };
                    if(dataset.positions.data){
                        let col_positions = [
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
                                "visible": "reference_number" in dataset.positions.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                        return row.reference_number
                                }
                            },
                            {
                                "name":"name",
                                "data":"name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "name" in dataset.positions.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                        return row.name
                                }
                            },
                            {
                                "name":"url",
                                "data":"url",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url" in dataset.positions.data[0] ? true : false,
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
                        transformTable("positions",dataset.positions.data,col_positions,[[2,"asc"]]);
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
                                        return row.reference_number
                                }
                            },
                            {
                                "name":"name",
                                "data":"name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "name" in dataset.employees.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                        return row.name
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