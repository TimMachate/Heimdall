function storageitem_list(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset.length != 0){
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
                            "name":"status",
                            "data":"status",
                            "defaultContent": "",
                            "className":"",
                            "visible": "status" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.status){
                                    if (row.status == 'overload'){
                                        result = '<span class="btn btn-secondary">&nbsp;&nbsp;</span>'
                                    }
                                    if (row.status == 'ok'){
                                        result = '<span class="btn btn-success">&nbsp;&nbsp;</span>'
                                    }
                                    if (row.status == 'warning'){
                                        result = '<span class="btn btn-warning">&nbsp;&nbsp;</span>'
                                    }
                                    if (row.status == 'alarm'){
                                        result = '<span class="btn btn-danger">&nbsp;&nbsp;</span>'
                                    }
                                    return result
                                }
                            }
                        },
                        {
                            "name":"name",
                            "data":"name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.name){return row.name};}
                        },
                        {
                            "name":"reference_number",
                            "data":"reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "reference_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.reference_number){return row.reference_number};}
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
                            "name":"supplieritem_item_number",
                            "data":"supplieritem_item_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "supplieritem_item_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.supplieritem_item_number){return row.supplieritem_item_number};}
                        },
                        {
                            "name":"stock_count",
                            "data":"stock_count",
                            "defaultContent": "0",
                            "className":"",
                            "visible": "stock_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.stock_count){return row.stock_count};}
                        },
                        {
                            "name":"stock_percentage",
                            "data":"stock_percentage",
                            "defaultContent": "0 %",
                            "className":"",
                            "visible": "stock_percentage" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.stock_percentage){return row.stock_percentage + " %"};}
                        },
                        {
                            "name":"stock_value",
                            "data":"stock_value",
                            "defaultContent": "0 €",
                            "className":"",
                            "visible": "stock_value" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.stock_value){return row.stock_value + ' €'};}
                        },
                        {
                            "name":"minimum",
                            "data":"minimum",
                            "defaultContent": "0",
                            "className":"",
                            "visible": "minimum" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.minimum){return row.minimum};}
                        },
                        {
                            "name":"warning",
                            "data":"warning",
                            "defaultContent": "0",
                            "className":"",
                            "visible": "warning" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.warning){return row.warning};}
                        },
                        {
                            "name":"maximum",
                            "data":"maximum",
                            "defaultContent": "0",
                            "className":"",
                            "visible": "maximum" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.maximum){return row.maximum};}
                        },
                        {
                            "name":"booking_count",
                            "data":"booking_count",
                            "defaultContent": "0",
                            "className":"",
                            "visible": "booking_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.booking_count){return row.booking_count};}
                        },
                        {
                            "name":"booking_last",
                            "data":"booking_last",
                            "defaultContent": "-",
                            "className":"",
                            "visible": "booking_last" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.booking_last){
                                    if (row.booking_last.create_date && row.booking_last.create_time && row.booking_last.url_detail){
                                        return '<a class="link-dark text-decoration-none" href="'+ row.booking_last.url_detail +'">'+row.booking_last.create_date + ' ' + row.booking_last.create_time+'</a>'
                                    }
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
                                if (row.create_username && row.create_username_url_detail){
                                    return '<a class="link-dark" href="'+ row.create_username_url_detail +'">'+row.create_username+'</a>'
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
                            "render":function(data,type,row,meta){if(row.update_time){return row.update_time};}
                        },
                        {
                            "name":"update_username",
                            "data":"update_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.update_username && row.update_username_url_detail){
                                    return '<a class="link-dark" href="'+ row.update_username_url_detail +'">'+row.update_username+'</a>'
                                } else {
                                    return row.update_username
                                }
                            }
                        },
                        {
                            "name":"url_request_create",
                            "data":"url_request_create",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_request_create" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_request_create){
                                    return '<a class="btn btn-success" href="'+ row.url_request_create +'?next=storagemanagement:storageitem_list"><i class="fas fa-cart-plus"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_booking_remove",
                            "data":"url_booking_remove",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_booking_remove" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_booking_remove){
                                    return '<a class="btn btn-danger" href="'+ row.url_booking_remove +'?next='+row.url_detail+'"><i class="fas fa-minus"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_booking_add",
                            "data":"url_booking_add",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_booking_add" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_booking_add){
                                    return '<a class="btn btn-success" href="'+ row.url_booking_add +'?next='+row.url_detail+'"><i class="fas fa-plus"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_booking",
                            "data":"url_booking",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_booking" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_booking){
                                    if (row.url_booking.url_booking_remove){
                                        minus = '<a class="btn btn-danger" href="'+ row.url_booking.url_booking_remove +'"><i class="fas fa-minus"></i></a>'
                                    } else {minus = ""};
                                    if (row.url_booking.url_booking_add){
                                        plus = '<a class="btn btn-success" href="'+ row.url_booking.url_booking_add +'"><i class="fas fa-plus"></i></a>'
                                    } else {plus = ""};
                                    return '<div class="btn-group">'+minus+plus+'</div>'
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
                                    return '<a class="btn btn-danger" href="'+ row.url_delete +'?next='+row.url_detail+'"><i class="fas fa-trash"></i></a>'
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
                    createList(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}
