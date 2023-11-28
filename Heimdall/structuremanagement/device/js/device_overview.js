function device_overview(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url,
            success: function(dataset){
                dataset.forEach(element => {
                    if(element.url_detail){
                        document.getElementById("id_url_detail_"+element.id).setAttribute('href',element.url_detail);
                        document.getElementById("id_picture_url_detail_"+element.id).setAttribute('href',element.url_detail);
                    };
                    if(element.name){
                        document.getElementById("id_name_"+element.id).innerHTML = element.name;
                    };
                    if(element.reference_number){
                        document.getElementById("id_reference_number_"+element.id).innerHTML = element.reference_number;
                    };
                    if(element.picture){
                        document.getElementById("id_image_"+element.id).setAttribute('src',element.picture.url_file);
                    };
                    if(element.processdata){
                        if(element.processdata.next){
                            if(element.processdata.next.url_detail){
                                document.getElementById("id_processdata_last_"+element.id).setAttribute('href',element.processdata.next.url_detail);
                            };
                            if(element.processdata.next.begin.date){
                                document.getElementById("id_processdata_last_datetime_"+element.id).innerHTML = element.processdata.next.begin.date+' '+element.processdata.next.begin.time;
                            };
                            if(element.processdata.next.reference_number){
                                document.getElementById("id_processdata_last_reference_number_"+element.id).innerHTML = element.processdata.next.reference_number;
                            };
                        };
                        if(element.processdata.status == "closed"){
                            document.getElementById("id_processdata_status_"+element.id).setAttribute('class',"input-group-text link-dark text-decoration-none w-25 bg-danger");
                        } else if (element.processdata.status == "running") {
                            document.getElementById("id_processdata_status_"+element.id).setAttribute('class',"input-group-text link-dark text-decoration-none w-25 bg-warning");
                        } else {
                            document.getElementById("id_processdata_status_"+element.id).setAttribute('class',"input-group-text link-dark text-decoration-none w-25 bg-success");
                        };
                    };
                    if(element.url_processdata_add){
                        document.getElementById("id_processdata_add_"+element.id).setAttribute('href',element.url_processdata_add+"?next=/structuremanagement/device/");
                    };
                    if(element.statusdata){
                        if(element.statusdata.last){
                            if(element.statusdata.last.status){
                                document.getElementById("id_statusdata_status_"+element.id).setAttribute('style','background-color:rgba('+element.statusdata.last.status.rgba_value+')');
                            };
                            if(element.statusdata.last.url_detail){
                                document.getElementById("id_statusdata_last_"+element.id).setAttribute('href',element.statusdata.last.url_detail);
                            };
                            if(element.statusdata.last.create.date){
                                document.getElementById("id_statusdata_last_datetime_"+element.id).innerHTML = element.statusdata.last.create.date+' '+element.statusdata.last.create.time;
                            };
                            if(element.statusdata.last.status.name){
                                document.getElementById("id_statusdata_last_name_"+element.id).innerHTML = element.statusdata.last.status.name;
                            };
                        };
                    };
                    if(element.url_statusdata_add){
                        document.getElementById("id_statusdata_add_"+element.id).setAttribute('href',element.url_statusdata_add+"?next=/structuremanagement/device/");
                    };
                    if(element.errordata){
                        if(element.errordata.last){
                            if(element.errordata.last.url_detail){
                                document.getElementById("id_errordata_last_"+element.id).setAttribute('href',element.errordata.last.url_detail);
                            };
                            if(element.errordata.last.create){
                                document.getElementById("id_errordata_last_datetime_"+element.id).innerHTML = element.errordata.last.create.date+' '+element.errordata.last.create.time;
                            };
                            if(element.errordata.last.error){
                                document.getElementById("id_errordata_last_name_"+element.id).innerHTML = element.errordata.last.error.name;
                            };
                        };
                    };
                    if(element.url_errordata_add){
                        document.getElementById("id_errordata_add_"+element.id).setAttribute('href',element.url_errordata_add+"?next=/structuremanagement/device/");
                    };
                    if(element.maintenance){
                        document.getElementById("id_maintenance_open_"+element.id).innerHTML = element.maintenance.open;
                        if(element.maintenance.open == 0){
                            document.getElementById("id_maintenance_status_"+element.id).setAttribute('class',"form-control link-dark text-decoration-none text-center bg-success");
                        } else {
                            document.getElementById("id_maintenance_status_"+element.id).setAttribute('class',"form-control link-dark text-decoration-none text-center bg-danger");
                        };
                    };
                });
            },
        });
    });
}