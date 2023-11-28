function person_list(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
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
                                if (row.reference_number){
                                    return row.reference_number
                                }
                            }
                        },
                        {
                            "name":"last_name",
                            "data":"last_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "last_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.last_name){
                                    return row.last_name
                                }
                            }
                        },
                        {
                            "name":"first_name",
                            "data":"first_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "first_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.first_name){
                                    return row.first_name
                                }
                            }
                        },
                        {
                            "name":"company",
                            "data":"company",
                            "defaultContent": "",
                            "className":"",
                            "visible": "company" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.company){
                                    if(row.company.name && row.company.url_detail){
                                        return '<a class="link-dark text-decoration-none" href="'+row.company.url_detail+'">'+row.company.name+'</a>'
                                    }else if(row.company.name){
                                        return row.company.name
                                    }else if(row.company.url_detail){
                                        return '<a class="link-dark text-decoration-none" href="'+row.company.url_detail+'"><i class="fas fa-info"></i></a>'
                                    };
                                };
                            }
                        },
                        {
                            "name":"telephones",
                            "data":"telephones",
                            "defaultContent": "",
                            "className":"",
                            "visible": "telephones" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.telephones){
                                    if(row.telephones.data){
                                        string = ""
                                        row.telephones.data.forEach(element => {
                                            string+='<div>'+element.number+'</div>'
                                        });
                                        return string
                                    };
                                }
                            }
                        },
                        {
                            "name":"emails",
                            "data":"emails",
                            "defaultContent": "",
                            "className":"",
                            "visible": "emails" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.emails){
                                    if(row.emails.data){
                                        string = ""
                                        row.emails.data.forEach(element => {
                                            string+='<div>'+element.email+'</div>'
                                        });
                                        return string
                                    };
                                }
                            }
                        },
                        {
                            "name":"notice",
                            "data":"notice",
                            "defaultContent": "",
                            "className":"",
                            "visible": "notice" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.notice){
                                    return row.notice
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
                                    if(row.create.date){
                                        return row.create.date
                                    };
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
                                    if(row.create.time){return row.create.time};
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
                            }}
                        },
                        {
                            "name":"update_date",
                            "data":"update_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.update){
                                    if(row.update.date){return row.update.date};
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
                                    if(row.update.time){return row.update.time}
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
                            }}
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
                    createList(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}
