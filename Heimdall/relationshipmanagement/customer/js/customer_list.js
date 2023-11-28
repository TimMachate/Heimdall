function customer_list(api_data_url,model) {
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
                            "name":"name",
                            "data":"name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.name){
                                    return row.name
                                }
                            }
                        },
                        {
                            "name":"street",
                            "data":"street",
                            "defaultContent": "",
                            "className":"",
                            "visible": "street" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.street){
                                    return row.street
                                }
                            }
                        },
                        {
                            "name":"house_number",
                            "data":"house_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "house_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.house_number){
                                    return row.house_number
                                }
                            }
                        },
                        {
                            "name":"post_code",
                            "data":"post_code",
                            "defaultContent": "",
                            "className":"",
                            "visible": "post_code" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.post_code){
                                    return row.post_code
                                }
                            }
                        },
                        {
                            "name":"city",
                            "data":"city",
                            "defaultContent": "",
                            "className":"",
                            "visible": "city" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.city){
                                    return row.city
                                }
                            }
                        },
                        {
                            "name":"country",
                            "data":"country",
                            "defaultContent": "",
                            "className":"",
                            "visible": "country" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.country){
                                    return row.country
                                }
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
