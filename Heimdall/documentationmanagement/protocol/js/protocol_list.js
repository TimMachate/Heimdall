function protocol_list(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    let col = [
                        {
                            "name":"id",
                            "data":"keywords",
                            "defaultContent": "",
                            "width":"10px",
                            "className":"",
                            "visible":true,
                            "render":function(data,type,row,meta){
                                return '<div class="d-none">'+row.keywords+'</div>'
                            }
                        },
                        {
                            "name":"reference_number",
                            "data":"reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "reference_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                return row.reference_number
                            }
                        },
                        {
                            "name":"name",
                            "data":"name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                return row.name
                            }
                        },
                        {
                            "name":"version",
                            "data":"version",
                            "defaultContent": "",
                            "className":"",
                            "visible": "version" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.version){
                                    return row.version
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"type",
                            "data":"type",
                            "defaultContent": "",
                            "className":"",
                            "visible": "type" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.type){
                                    return row.type
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"url_file",
                            "data":"url_file",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url){
                                    if (row.url.file){
                                        return '<a class="btn btn-primary" href="'+ row.url.file +'" target="_blank"><i class="fas fa-file-pdf"></i></a>'
                                    } else {
                                        return '-'
                                    }
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"url_file_qrcode",
                            "data":"url_file_qrcode",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible":"url_file_qrcode" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_file_qrcode){
                                    if (row.url_file_qrcode){
                                        return '<a class="btn btn-primary" href="'+ row.url_file_qrcode +'" target="_blank"><i class="fas fa-image"></i></a>'
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
                                    if (row.url.data_create){
                                        data_create = '<a class="btn btn-success" href="'+ row.url.data_create +'"><i class="fas fa-plus"></i></a>'
                                    } else {data_create = ""};
                                    if (row.url.delete){
                                        del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                    } else {del = ""};
                                    return '<div class="btn-group">'+detail+update+data_create+del+'</div>'
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
