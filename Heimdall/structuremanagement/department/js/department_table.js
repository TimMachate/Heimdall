function department_table(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replace("=&amp;", '=&').replace("&amp;", '&'),
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
                            "name":"rgba_value",
                            "data":"rgba_value",
                            "defaultContent": "",
                            "className":"",
                            "visible": "color" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.color){
                                    return '<div class="btn" '+row.color.style+'>&nbsp;</div>'
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"rgba_red",
                            "data":"rgba_red",
                            "defaultContent": "",
                            "className":"",
                            "visible": "color" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.color){
                                    return row.color.red
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"rgba_green",
                            "data":"rgba_green",
                            "defaultContent": "",
                            "className":"",
                            "visible": "color" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.color){
                                    return row.color.green
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"rgba_blue",
                            "data":"rgba_blue",
                            "defaultContent": "",
                            "className":"",
                            "visible": "color" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.color){
                                    return row.color.blue
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"rgba_alpha",
                            "data":"rgba_alpha",
                            "defaultContent": "",
                            "className":"",
                            "visible": "color" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.color){
                                    return row.color.alpha
                                }else{
                                    return '-'
                                };
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
                            "name":"section_count",
                            "data":"section_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "section_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){return row.section_count}
                        },
                        {
                            "name":"position_count",
                            "data":"position_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "position_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){return row.position_count}
                        },
                        {
                            "name":"employee_count",
                            "data":"employee_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "employee_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){return row.employee_count}
                        },
                        {
                            "name":"process_instruction_file_url",
                            "data":"process_instruction_file_url",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "process_instruction" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.process_instruction){
                                    if (row.process_instruction.url_file){
                                        return '<a class="btn btn-primary" href="'+ row.process_instruction.url_file +'" target="_blank"><i class="fas fa-file-pdf"></i></a>'
                                    } else {
                                        return '-'
                                    }
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"image_file_url",
                            "data":"image_file_url",
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
