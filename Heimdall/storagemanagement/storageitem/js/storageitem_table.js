function storageitem_table(api_url,model) {
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
                            "name":"companyitem_name",
                            "data":"companyitem_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "companyitem_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.companyitem_name && row.companyitem_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.companyitem_url_detail+'">'+row.companyitem_name+'</a>'
                                }else{
                                    return row.companyitem_name
                                };
                            }
                        },
                        {
                            "name":"companyitem_item_number",
                            "data":"companyitem_item_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "companyitem_item_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.companyitem_item_number){return row.companyitem_item_number};}
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
                                    return '<a class="btn btn-success" href="'+ row.url_request_create +'?next='+row.url_detail+'"><i class="fas fa-cart-plus"></i></a>'
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
