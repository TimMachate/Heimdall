function orderdata_table(api_url,model) {
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
                            "name":"authorized",
                            "data":"authorized",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.authorized == true){
                                    return 'true'
                                } else if (row.authorized == false) {
                                    return 'false'
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
                                if (row.authorized_username){
                                    return row.authorized_username
                                };
                            }
                        },
                        {
                            "name":"booking",
                            "data":"booking",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.booking == true){
                                    return 'true'
                                } else if (row.booking == false) {
                                    return 'false'
                                } else {
                                    return ''
                                };
                            }
                        },
                        {
                            "name":"booking_date",
                            "data":"booking_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.booking_date){return row.booking_date};}
                        },
                        {
                            "name":"booking_time",
                            "data":"booking_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.booking_time){return row.booking_time};}
                        },
                        {
                            "name":"booking_username",
                            "data":"booking_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.booking_username){
                                    return row.booking_username
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
                                if (row.create_username){
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
                                if (row.update_username){
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
                            "name":"order_reference_number",
                            "data":"order_reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "order_reference_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.order_reference_number){return row.order_reference_number}}
                        },
                        {
                            "name":"storageitem_name",
                            "data":"storageitem_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "storageitem_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.storageitem_name){
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
                                if(row.storageitem_reference_number){
                                    return row.storageitem_reference_number
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
                                if(row.companyitem_name){
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
                            "render":function(data,type,row,meta){
                                if(row.companyitem_item_number){
                                    return row.companyitem_item_number
                                };
                            }
                        },
                        {
                            "name":"company_name",
                            "data":"company_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "company_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.company_name){
                                    return row.company_name
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
                            "name":"amount_recived",
                            "data":"amount_recived",
                            "defaultContent": "",
                            "className":"",
                            "visible": "amount_recived" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.amount_recived){return row.amount_recived}}
                        },
                        {
                            "name":"notice",
                            "data":"notice",
                            "defaultContent": "",
                            "className":"",
                            "visible": "notice" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.notice){return 'true'}else{return 'false'}}
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
                                        return row.url_detail
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
                                    return row.url_update
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
                                    return row.url_delete
                                };
                            }
                        },
                        {
                            "name":"url_authorize_true",
                            "data":"url_authorize_true",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_authorize_true" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_authorize_true){
                                    return row.url_authorize_true
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
                                    return row.url_authorize_false
                                };
                            }
                        },
                        {
                            "name":"url_booking_true",
                            "data":"url_booking_true",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_booking_true" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_booking_true){
                                    return row.url_booking_true
                                };
                            }
                        },
                        {
                            "name":"url_booking_false",
                            "data":"url_booking_false",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_booking_false" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_booking_false){
                                    return row.url_booking_false
                                };
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createTable('id_orderdata',dataset,col,[[9,'desc'],[10,'desc']],print);
                };
            },
        });
        
    });
}