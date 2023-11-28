function position_table(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
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
                            "name":"reference_number",
                            "data":"reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "reference_number" in dataset[0] ? true : false,
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
                            "visible": "name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_detail){
                                    return '<a class="link-dark" href="'+ row.url_detail +'">'+row.name+'</a>'
                                } else {
                                    return row.name
                                }
                            }
                        },
                        {
                            "name":"department",
                            "data":"department",
                            "defaultContent": "",
                            "className":"",
                            "visible": "department" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.department){
                                    return '<a class="link-dark" href="'+ row.department.url_detail +'">'+row.department.name+'</a>'
                                } else {
                                    return '-'
                                }
                            }
                        },
                        {
                            "name":"section",
                            "data":"section",
                            "defaultContent": "",
                            "className":"",
                            "visible": "section" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.section){
                                    return '<a class="link-dark" href="'+ row.section.url_detail +'">'+row.section.name+'</a>'
                                } else {
                                    return '-'
                                }
                            }
                        },
                        {
                            "name":"responsible_name",
                            "data":"responsible_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "responsible" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.responsible){
                                    if (row.responsible.url_detail){
                                        return '<a class="link-dark" href="'+ row.responsible.url_detail +'">'+row.responsible.name+'</a>'
                                    } else {
                                        return row.responsible.name
                                    }
                                } else {
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"responsible_email",
                            "data":"responsible_email",
                            "defaultContent": "",
                            "className":"",
                            "visible": "responsible" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.responsible){
                                    return row.responsible.email
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"responsible_telephone",
                            "data":"responsible_telephone",
                            "defaultContent": "",
                            "className":"",
                            "visible": "responsible" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.responsible){
                                    return row.responsible.telephone
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"substitute_name",
                            "data":"substitute_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "substitute" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.substitute){
                                    if (row.substitute.url_detail){
                                        return '<a class="link-dark" href="'+ row.substitute.url_detail +'">'+row.substitute.name+'</a>'
                                    } else {
                                        return row.substitute.name
                                    }
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"substitute_email",
                            "data":"substitute_email",
                            "defaultContent": "",
                            "className":"",
                            "visible": "substitute" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.substitute){
                                    return row.substitute.email
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"substitute_telephone",
                            "data":"substitute_telephone",
                            "defaultContent": "",
                            "className":"",
                            "visible": "substitute" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.substitute){
                                    return row.substitute.telephone
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"employee_count",
                            "data":"employee_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "employees" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.employees){
                                    return row.employees.count
                                };
                            }
                        },
                        {
                            "name":"directions_count",
                            "data":"directions_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "directions" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.directions){
                                    return row.directions.count
                                };
                            }
                        },
                        {
                            "name":"documents_count",
                            "data":"documents_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "documents" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.documents){
                                    return row.documents.count
                                };
                            }
                        },
                        {
                            "name":"safety_data_sheets_count",
                            "data":"safety_data_sheets_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "safety_data_sheets" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.safety_data_sheets){
                                    return row.safety_data_sheets.count
                                };
                            }
                        },
                        {
                            "name":"working_instructions_count",
                            "data":"working_instructions_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "working_instructions" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.working_instructions){
                                    return row.working_instructions.count
                                };
                            }
                        },
                        {
                            "name":"description",
                            "data":"description",
                            "defaultContent": "",
                            "className":"",
                            "visible": "description" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.description){
                                    return row.description
                                };
                            }
                        },
                        {
                            "name":"working_description_id_url_file",
                            "data":"working_description_id_url_file",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "working_description" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.working_description){
                                    if (row.working_description.url_file){
                                        return '<a class="btn btn-primary" href="'+ row.working_description.url_file +'" target="_blank"><i class="fas fa-file-pdf"></i></a>'
                                    } else {
                                        return '-'
                                    }
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"picture_id_url_file",
                            "data":"picture_id_url_file",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible":"picture" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.picture){
                                    if (row.picture.url_file){
                                        return '<a class="btn btn-primary" href="'+ row.picture.url_file +'" target="_blank"><i class="fas fa-image"></i></a>'
                                    } else {
                                        return '-'
                                    }   
                                }else{
                                    return '-'
                                };                     
                            }
                        },
                        {
                            "name":"create_date",
                            "data":"create_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.create){
                                    return row.create.date
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"create_time",
                            "data":"create_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.create){
                                    return row.create.time
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"create_username",
                            "data":"create_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.create){
                                    if (row.create.url_detail){
                                        return '<a class="link-dark" href="'+ row.create.url_detail +'">'+row.create.username+'</a>'
                                    } else {
                                        return row.create.username
                                    }
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"update_date",
                            "data":"update_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.update){
                                    return row.update.date
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"update_time",
                            "data":"update_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.update){
                                    return row.update.time
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"update_username",
                            "data":"update_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.update){
                                    if (row.update.url_detail){
                                        return '<a class="link-dark" href="'+ row.update.url_detail +'">'+row.update.username+'</a>'
                                    } else {
                                        return row.update.username
                                    }
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"url",
                            "data":"url",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url" in dataset[0] ? true : false,
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
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createTable(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}
