function supplier_table(api_url,model) {
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
                            "render":function(data,type,row,meta){if(row.reference_number){return row.reference_number}}
                        },
                        {
                            "name":"name",
                            "data":"name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.name){return row.name};}
                        },
                        {
                            "name":"street",
                            "data":"street",
                            "defaultContent": "",
                            "className":"",
                            "visible": "street" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.street){return row.street};}
                        },
                        {
                            "name":"house_number",
                            "data":"house_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "house_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.house_number){return row.house_number};}
                        },
                        {
                            "name":"post_code",
                            "data":"post_code",
                            "defaultContent": "",
                            "className":"",
                            "visible": "post_code" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.post_code){return row.post_code};}
                        },
                        {
                            "name":"city",
                            "data":"city",
                            "defaultContent": "",
                            "className":"",
                            "visible": "city" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.city){return row.city};}
                        },
                        {
                            "name":"country",
                            "data":"country",
                            "defaultContent": "",
                            "className":"",
                            "visible": "country" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.country){return row.country};}
                        },
                        {
                            "name":"telephone",
                            "data":"telephone",
                            "defaultContent": "",
                            "className":"",
                            "visible": "telephone" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.telephone){return row.telephone};}
                        },
                        {
                            "name":"email",
                            "data":"email",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email){return row.email};}
                        },
                        {
                            "name":"email_address_offer",
                            "data":"email_address_offer",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_address_offer" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_address_offer){return row.email_address_offer};}
                        },
                        {
                            "name":"email_address_cc_offer",
                            "data":"email_address_cc_offer",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_address_cc_offer" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_address_cc_offer){return row.email_address_cc_offer};}
                        },
                        {
                            "name":"email_body_offer",
                            "data":"email_body_offer",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_body_offer" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_body_offer){return row.email_body_offer};}
                        },
                        {
                            "name":"email_subject_offer",
                            "data":"email_subject_offer",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_subject_offer" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_subject_offer){return row.email_subject_offer};}
                        },
                        {
                            "name":"email_address_order",
                            "data":"email_address_order",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_address_order" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_address_order){return row.email_address_order};}
                        },
                        {
                            "name":"email_address_cc_order",
                            "data":"email_address_cc_order",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_address_cc_order" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_address_cc_order){return row.email_address_cc_order};}
                        },
                        {
                            "name":"email_body_order",
                            "data":"email_body_order",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_body_order" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_body_order){return row.email_body_order};}
                        },
                        {
                            "name":"email_subject_order",
                            "data":"email_subject_order",
                            "defaultContent": "",
                            "className":"",
                            "visible": "email_subject_order" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.email_subject_order){return row.email_subject_order};}
                        },
                        {
                            "name":"suppliercontact_count",
                            "data":"suppliercontact_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "suppliercontact_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.suppliercontact_count){return row.suppliercontact_count};}
                        },
                        {
                            "name":"supplieritem_count",
                            "data":"supplieritem_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "supplieritem_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.supplieritem_count){return row.supplieritem_count};}
                        },
                        {
                            "name":"storageitem_count",
                            "data":"storageitem_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "storageitem_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.storageitem_count){return row.storageitem_count};}
                        },
                        {
                            "name":"stock_count",
                            "data":"stock_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "stock_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.stock_count){return row.stock_count};}
                        },
                        {
                            "name":"stock_value",
                            "data":"stock_value",
                            "defaultContent": "",
                            "className":"",
                            "visible": "stock_value" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.stock_value){return row.stock_value};}
                        },
                        {
                            "name":"booking_count",
                            "data":"booking_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booking_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.booking_count){return row.booking_count};}
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
                            "name":"notice",
                            "data":"notice",
                            "defaultContent": "",
                            "className":"",
                            "visible": "notice" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.notice){return '<i class="fas fa-exclamation-triangle"></i>'};}
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
                    createTable(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}
