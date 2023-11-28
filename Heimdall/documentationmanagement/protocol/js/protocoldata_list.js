function protocoldata_list(api_url,model) {
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
                                    return row.reference_number
                            }
                        },
                        {
                            "name":"protocol",
                            "data":"protocol",
                            "defaultContent": "",
                            "className":"",
                            "visible": "protocol" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.protocol){
                                    if (row.protocol.name && row.protocol.url_detail){
                                        return '<a class="link-dark" href="'+ row.protocol.url_detail +'">'+row.protocol.name+'</a>'
                                    } else if (row.protocol.name){
                                        return row.protocol.name
                                    };
                                    
                                };
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
                            "name":"data",
                            "data":"data",
                            "defaultContent": "",
                            "className":"",
                            "visible": "data" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.data){
                                    return row.data
                                };
                            }
                        },
                        {
                            "name":"protocol_id",
                            "data":"protocol_id",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "protocol_id" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.protocol_id){
                                    if (row.protocol_id){
                                        return '<a class="btn btn-primary" href="'+ row.protocol_id +'" target="_blank"><i class="fas fa-file-pdf"></i></a>'
                                    };
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
                                    if (row.url.url_detail){
                                        detail = '<a class="btn btn-primary" href="'+ row.url.url_detail +'"><i class="fas fa-search"></i></a>'
                                    } else {detail = ""};
                                    if (row.url.url_update){
                                        update = '<a class="btn btn-primary" href="'+ row.url.url_update +'"><i class="fas fa-pen"></i></a>'
                                    } else {update = ""};
                                    if (row.url.url_delete){
                                        del = '<a class="btn btn-danger" href="'+ row.url.url_delete +'"><i class="fas fa-trash"></i></a>'
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
                    createList(model,dataset,col,[[1,'desc']],print);
                };
            },
        });
        
    });
}
