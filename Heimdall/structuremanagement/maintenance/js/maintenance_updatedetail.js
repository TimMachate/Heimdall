function maintenance_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset.reference_number && document.getElementById("id_reference_number")){
                    document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                };
                if(dataset.name && document.getElementById("id_name")){
                    document.getElementById("id_name").setAttribute("value",dataset.name);
                };
                if(dataset.device){
                    if(dataset.device.name && dataset.device.reference_number && document.getElementById("id_device_id")){
                        document.getElementById("id_device_id").setAttribute("value",dataset.device.name+' ('+dataset.device.reference_number+')');
                    };
                    if(dataset.device.url_detail && document.getElementById("id_device_url_detail")){
                        document.getElementById("id_device_url_detail").setAttribute("href",dataset.device.url_detail);
                    };
                };
                if(dataset.protocol){
                    if(dataset.protocol.name && dataset.protocol.reference_number && document.getElementById("id_protocol_id")){
                        document.getElementById("id_protocol_id").setAttribute("value",dataset.protocol.name+' ('+dataset.protocol.reference_number+')');
                    };
                    if(dataset.protocol.url_detail && document.getElementById("id_protocol_url_detail")){
                        document.getElementById("id_protocol_url_detail").setAttribute("href",dataset.protocol.url_detail);
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
                if(dataset.warning){
                    if(dataset.warning.formated && document.getElementById("id_warning_formated")){
                        document.getElementById("id_warning_formated").innerHTML = dataset.warning.formated;
                    };
                };
                if(dataset.repetition){
                    if(dataset.repetition.formated && document.getElementById("id_repetition_formated")){
                        document.getElementById("id_repetition_formated").innerHTML = dataset.repetition.formated;
                    };
                };
                if(dataset.maintenance_next){
                    if(dataset.maintenance_next.date && dataset.maintenance_next.time && document.getElementById("id_maintenance_next")){
                        document.getElementById("id_maintenance_next").innerHTML = dataset.maintenance_next.date + " " + dataset.maintenance_next.time;
                    };
                };
                if(dataset.status && document.getElementById("id_maintenance_next")){
                    if(dataset.status == "alarm"){
                        document.getElementById("id_maintenance_next").setAttribute("class","btn btn-danger btn-lg form-control");
                    } else if(dataset.status == "warning"){
                        document.getElementById("id_maintenance_next").setAttribute("class","btn btn-warning btn-lg form-control");
                    } else if(dataset.status == "OK"){
                        document.getElementById("id_maintenance_next").setAttribute("class","btn btn-secondary btn-lg form-control");
                    } else {
                        document.getElementById("id_maintenance_next").setAttribute("class","btn btn-secondary btn-lg form-control");
                    };
                };
                if(dataset.url){
                    if(dataset.url.data_create && document.getElementById("id_maintenance_url_data_create")){
                        document.getElementById("id_maintenance_url_data_create").setAttribute("href",dataset.url.data_create);
                    };
                };
                if(dataset.maintenance_count){
                    document.getElementById("id_maintenance_count").innerHTML = dataset.maintenance_count;
                };
                let col = [
                    {
                        "name":"id",
                        "data":"",
                        "defaultContent": "",
                        "width":"10px",
                        "className":"",
                        "visible":true,
                    },
                    {
                        "name":"create",
                        "data":"create",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset.maintenance_data[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.create){
                                if(row.create.date){
                                    return row.create.date
                                };
                            };
                        }
                    },
                    {
                        "name":"create",
                        "data":"create",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset.maintenance_data[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.create){
                                if(row.create.time){
                                    return row.create.time
                                };
                            };
                        }
                    },
                    {
                        "name":"reference_number",
                        "data":"reference_number",
                        "defaultContent": "",
                        "className":"",
                        "visible": "reference_number" in dataset.maintenance_data[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.reference_number){
                                return row.reference_number
                            }
                        }
                    },
                    {
                        "name":"version",
                        "data":"version",
                        "defaultContent": "",
                        "className":"",
                        "visible": "version" in dataset.maintenance_data[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.version){
                                return row.version
                            }
                        }
                    },
                    {
                        "name":"file",
                        "data":"file",
                        "defaultContent": "",
                        "className":"",
                        "visible": "file" in dataset.maintenance_data[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.file){
                                return '<a class="btn btn-primary" href="'+ row.file +'"><i class="fas fa-file-pdf"></i></a>'
                            }
                        }
                    },
                    {
                        "name":"url",
                        "data":"url",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "url" in dataset.maintenance_data[0] ? true : false,
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
                transformTable("maintenances",dataset.maintenance_data,col,[[2,"desc"]]);
            },
        });
        
    });
}