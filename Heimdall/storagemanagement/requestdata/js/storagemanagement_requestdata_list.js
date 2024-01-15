function requestdata_list(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset.length > 0){
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
                            "name":"authorized",
                            "data":"authorized",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.authorized == true){
                                    return '<span class="btn btn-success disabled"><i class="fas fa-check"></i></span>'
                                } else if (row.authorized == false) {
                                    return '<span class="btn btn-danger disabled"><i class="fas fa-times"></i></span>'
                                } else {
                                    return ''
                                };
                            }
                        },
                        {
                            "name":"authorized_date",
                            "data":"authorized_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.authorized_date){return row.authorized_date};}
                        },
                        {
                            "name":"authorized_time",
                            "data":"authorized_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.authorized_time){return row.authorized_time};}
                        },
                        {
                            "name":"authorized_username",
                            "data":"authorized_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.authorized_username && row.authorized_url_detail){
                                    return '<a class="link-dark" href="'+ row.authorized_url_detail +'">'+row.authorized_username+'</a>'
                                } else {
                                    return row.authorized_username
                                };
                            }
                        },
                        {
                            "name":"done",
                            "data":"done",
                            "defaultContent": "",
                            "className":"",
                            "visible": "done" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.done == true){
                                    return '<span class="btn btn-success disabled"><i class="fas fa-check"></i></span>'
                                } else if (row.done == false){
                                    return '<span class="btn btn-danger disabled"><i class="fas fa-times"></i></span>'
                                } else {
                                    return ''
                                };
                            }
                        },
                        {
                            "name":"create_date",
                            "data":"create_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.create_date){return row.create_date};}
                        },
                        {
                            "name":"create_time",
                            "data":"create_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.create_time){return row.create_time};}
                        },
                        {
                            "name":"create_username",
                            "data":"create_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.create_username && row.create_url_detail){
                                    return '<a class="link-dark" href="'+ row.create_url_detail +'">'+row.create_username+'</a>'
                                } else {
                                    return row.create_username
                                };
                            }
                        },
                        {
                            "name":"update_date",
                            "data":"update_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.update_date){return row.update_date};}
                        },
                        {
                            "name":"update_time",
                            "data":"update_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.update_time){return row.update_time}}
                        },
                        {
                            "name":"update_username",
                            "data":"update_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.update_username && row.update_url_detail){
                                    return '<a class="link-dark" href="'+ row.update_url_detail +'">'+row.update_username+'</a>'
                                } else {
                                    return row.update_username
                                };
                            }
                        },
                        {
                            "name":"reference_number",
                            "data":"reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "reference_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.reference_number){return row.reference_number}}
                        },
                        {
                            "name":"storageitem_name",
                            "data":"storageitem_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "storageitem_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.storageitem_name && row.storageitem_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.storageitem_url_detail+'">'+row.storageitem_name+'</a>'
                                }else{
                                    return row.storageitem_name
                                };
                            }
                        },
                        {
                            "name":"storageitem_reference_number",
                            "data":"storageitem_reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "storageitem_reference_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.storageitem_reference_number && row.storageitem_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.storageitem_url_detail+'">'+row.storageitem_reference_number+'</a>'
                                }else{
                                    return row.storageitem_reference_number
                                };
                            }
                        },
                        {
                            "name":"supplieritem_name",
                            "data":"supplieritem_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "supplieritem_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.supplieritem_name && row.supplieritem_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.supplieritem_url_detail+'">'+row.supplieritem_name+'</a>'
                                }else{
                                    return row.supplieritem_name
                                };
                            }
                        },
                        {
                            "name":"supplieritem_reference_number",
                            "data":"supplieritem_reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "supplieritem_reference_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.supplieritem_reference_number && row.storageitem_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.storageitem_url_detail+'">'+row.supplieritem_reference_number+'</a>'
                                }else{
                                    return row.supplieritem_reference_number
                                };
                            }
                        },
                        {
                            "name":"supplieritem_item_number",
                            "data":"supplieritem_item_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "supplieritem_item_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.supplieritem_item_number && row.storageitem_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.storageitem_url_detail+'">'+row.supplieritem_item_number+'</a>'
                                }else{
                                    return row.supplieritem_item_number
                                };
                            }
                        },
                        {
                            "name":"supplier_name",
                            "data":"supplier_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "supplier_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.supplier_name && row.supplier_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.supplier_url_detail+'">'+row.supplier_name+'</a>'
                                }else{
                                    return row.supplier_name
                                };
                            }
                        },
                        {
                            "name":"amount",
                            "data":"amount",
                            "defaultContent": "",
                            "className":"",
                            "visible": "amount" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.amount){return row.amount}}
                        },
                        {
                            "name":"unit",
                            "data":"unit",
                            "defaultContent": "",
                            "className":"",
                            "visible": "unit" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.unit){return row.unit};}
                        },
                        {
                            "name":"price",
                            "data":"price",
                            "defaultContent": "",
                            "className":"",
                            "visible": "price" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.price){return row.price+" €"};}
                        },
                        {
                            "name":"value",
                            "data":"value",
                            "defaultContent": "",
                            "className":"",
                            "visible": "value" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.value){return row.value+" €"};}
                        },
                        {
                            "name":"notice",
                            "data":"notice",
                            "defaultContent": "",
                            "className":"",
                            "visible": "notice" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.notice){return '<i class="fas fa-exclamation-triangle"></i>'};}
                        },
                        {
                            "name":"url_authorize_true",
                            "data":"url_authorize_true",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_authorize_true" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_authorize_true){
                                    return '<a class="btn btn-success" href="'+row.url_authorize_true+'"><i class="fas fa-check"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_authorize_false",
                            "data":"url_authorize_false",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_authorize_false" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_authorize_false){
                                    return '<a class="btn btn-danger" href="'+row.url_authorize_false+'?next="><i class="fas fa-times"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_authorize",
                            "data":"url_authorize",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_authorize" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_authorize){
                                    if (row.url_authorize.url_authorize_true){
                                        yes = '<a class="btn btn-primary" href="'+ row.url_authorize.url_authorize_true +'"><i class="fas fa-search"></i></a>'
                                    } else {yes = ""};
                                    if (row.url_authorize.url_authorize_false){
                                        no = '<a class="btn btn-primary" href="'+ row.url_authorize.url_authorize_false +'"><i class="fas fa-pen"></i></a>'
                                    } else {no = ""};
                                    return '<div class="btn-group">'+yes+no+'</div>'
                                }
                            }
                        },
                        {
                            "name":"url_detail",
                            "data":"url_detail",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_detail" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                    };
                            }
                        },
                        {
                            "name":"url_update",
                            "data":"url_update",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_update){
                                    return '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_delete",
                            "data":"url_delete",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_delete" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_delete){
                                    return '<a class="btn btn-danger" href="'+ row.url_delete + "?next=" + dataset.url_detail +'"><i class="fas fa-trash"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_block",
                            "data":"url_block",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_block" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_block){
                                    if (row.url_block.url_detail){
                                        detail = '<a class="btn btn-primary" href="'+ row.url_block.url_detail +'"><i class="fas fa-search"></i></a>'
                                    } else {detail = ""};
                                    if (row.url_block.url_update){
                                        update = '<a class="btn btn-primary" href="'+ row.url_block.url_update +'"><i class="fas fa-pen"></i></a>'
                                    } else {update = ""};
                                    if (row.url_block.url_delete){
                                        del = '<a class="btn btn-danger" href="'+ row.url_block.url_delete +'"><i class="fas fa-trash"></i></a>'
                                    } else {del = ""};
                                    return '<div class="btn-group">'+detail+update+del+'</div>'
                                }
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createList('id_requestdata',dataset,col,[[6,'desc'],[7,'desc']],print);
                };
            },
        });
        
    });
}
