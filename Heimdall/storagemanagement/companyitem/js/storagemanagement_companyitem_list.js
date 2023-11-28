function companyitem_list(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
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
                            "name":"item_number",
                            "data":"item_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.item_number){
                                    return row.item_number
                                }
                            }
                        },
                        {
                            "name":"company",
                            "data":"company",
                            "defaultContent": "",
                            "className":"",
                            "visible": "company_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.company_name && row.company_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.company_url_detail+'">'+row.company_name+'</a>'
                                }else{
                                    return row.company_name
                                };
                            }
                        },
                        {
                            "name":"storageitem",
                            "data":"storageitem",
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
                            "name":"unit",
                            "data":"unit",
                            "defaultContent": "",
                            "className":"",
                            "visible": "unit" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.unit){return row.unit}}
                        },
                        {
                            "name":"price",
                            "data":"price",
                            "defaultContent": "",
                            "className":"",
                            "visible": "price" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.price){return row.price+" €"}}
                        },
                        {
                            "name":"stock_count",
                            "data":"price",
                            "defaultContent": "",
                            "className":"",
                            "visible": "stock_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.stock_count){return row.stock_count}}
                        },
                        {
                            "name":"stock_value",
                            "data":"stock_value",
                            "defaultContent": "",
                            "className":"",
                            "visible": "stock_value" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.stock_value){return row.stock_value+" €"}}
                        },
                        {
                            "name":"booking_count",
                            "data":"booking_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.booking_count){return row.booking_count}}
                        },
                        {
                            "name":"booking_last",
                            "data":"booking_last",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking_last" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.booking_last){
                                    if(row.booking_last.create_date && row.booking_last.create_time && row.booking_last.url_detail){
                                        return row.booking_last.create_date + " " + row.booking_last.create_time
                                    } else if(row.booking_last.create_date && row.booking_last.create_time){
                                        return row.booking_last.create_date + " " + row.booking_last.create_time
                                    };
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
                                    return '<a class="btn btn-danger" href="'+ row.url_booking_remove +'?next=storagemanagement:storageitem_list"><i class="fas fa-minus"></i></a>'
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
                                    return '<a class="btn btn-success" href="'+ row.url_booking_add +'?next=storagemanagement:storageitem_list"><i class="fas fa-plus"></i></a>'
                                };
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
                                    detail = '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                } else {detail = ""};
                                if (row.url_update){
                                    update = '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                } else {update = ""};
                                if (row.url_delete){
                                    del = '<a class="btn btn-danger" href="'+ row.url_delete +'"><i class="fas fa-trash"></i></a>'
                                } else {del = ""};
                                return '<div class="btn-group">'+detail+update+del+'</div>'
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
