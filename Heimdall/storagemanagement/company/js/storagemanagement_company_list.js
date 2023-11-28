function company_list(api_url,model) {
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
                            "name":"companycontact_count",
                            "data":"companycontact_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "companycontact_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.companycontact_count){return row.companycontact_count};}
                        },
                        {
                            "name":"companyitem_count",
                            "data":"companyitem_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "companyitem_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.companyitem_count){return row.companyitem_count};}
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
