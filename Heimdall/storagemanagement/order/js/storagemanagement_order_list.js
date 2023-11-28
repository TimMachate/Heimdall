function order_list(api_url,model) {
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
                            "name":"done",
                            "data":"done",
                            "defaultContent": "",
                            "className":"",
                            "visible": "done" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.done == true){
                                    return '<span class="btn btn-success disabled" style="width:3rem;">&nbsp;&nbsp;&nbsp;&nbsp;</span>'
                                } else if (row.done == false) {
                                    return '<span class="btn btn-danger disabled" style="width:3rem;">&nbsp;&nbsp;&nbsp;&nbsp;</span>'
                                } else {
                                    return ''
                                };
                            }
                        },
                        {
                            "name":"authorized",
                            "data":"authorized",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.authorized == true){
                                    return '<span class="btn btn-success disabled" style="width:3rem;"><i class="fas fa-certificate"></i></span>'
                                } else if (row.authorized == false) {
                                    return '<span class="btn btn-danger disabled" style="width:3rem;"><i class="fas fa-certificate"></i></span>'
                                } else {
                                    return '<span class="btn btn-secondary disabled" style="width:3rem;"><i class="fas fa-certificate"></i></span>'
                                };
                            }
                        },
                        {
                            "name":"booked",
                            "data":"booked",
                            "defaultContent": "",
                            "className":"",
                            "visible": "booked" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.booked == true){
                                    return '<span class="btn btn-success disabled" style="width:3rem;"><i class="fas fa-warehouse"></i></span>'
                                } else if (row.booked == false) {
                                    return '<span class="btn btn-danger disabled" style="width:3rem;"><i class="fas fa-warehouse"></i></span>'
                                } else {
                                    return '<span class="btn btn-secondary disabled" style="width:3rem;"><i class="fas fa-warehouse"></i></span>'
                                };
                            }
                        },
                        {
                            "name":"sent",
                            "data":"sent",
                            "defaultContent": "",
                            "className":"",
                            "visible": "sent" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.sent == true){
                                    return '<span class="btn btn-success disabled" style="width:3rem;"><i class="fas fa-truck"></i></span>'
                                } else if (row.sent == false) {
                                    return '<span class="btn btn-danger disabled" style="width:3rem;"><i class="fas fa-truck"></i></span>'
                                } else {
                                    return '<span class="btn btn-secondary disabled" style="width:3rem;"></span>'
                                };
                            }
                        },
                        {
                            "name":"sent_date",
                            "data":"sent_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "sent_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.sent_date){return row.sent_date};}
                        },
                        {
                            "name":"sent_time",
                            "data":"sent_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "sent_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.sent_time){return row.sent_time};}
                        },
                        {
                            "name":"sent_username",
                            "data":"sent_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "sent_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.sent_username && row.sent_url_detail){
                                    return '<a class="link-dark" href="'+ row.sent_url_detail +'">'+row.sent_username+'</a>'
                                } else {
                                    return row.sent_username
                                };
                            }
                        },
                        {
                            "name":"recived",
                            "data":"recived",
                            "defaultContent": "",
                            "className":"",
                            "visible": "recived" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.recived == true){
                                    return '<span class="btn btn-success disabled" style="width:3rem;"><i class="fas fa-truck-loading"></i></span>'
                                } else if (row.recived == false) {
                                    return '<span class="btn btn-danger disabled" style="width:3rem;"><i class="fas fa-truck-loading"></i></span>'
                                } else {
                                    return '<span class="btn btn-secondary disabled" style="width:3rem;"></span>'
                                };
                            }
                        },
                        {
                            "name":"recived_date",
                            "data":"recived_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "recived_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.recived_date){return row.recived_date};}
                        },
                        {
                            "name":"recived_time",
                            "data":"recived_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "recived_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.recived_time){return row.recived_time};}
                        },
                        {
                            "name":"recived_username",
                            "data":"recived_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "recived_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.recived_username && row.recived_url_detail){
                                    return '<a class="link-dark" href="'+ row.recived_url_detail +'">'+row.recived_username+'</a>'
                                } else {
                                    return row.recived_username
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
                            "name":"company_name",
                            "data":"company_name",
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
                            "name":"item_count",
                            "data":"item_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.item_count){return row.item_count};}
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
                            "render":function(data,type,row,meta){if (row.notice){return '<span class="btn btn-danger disabled" style="width:3rem;"><i class="fas fa-exclamation-triangle"></i></span>'};}
                        },
                        {
                            "name":"url_detail",
                            "data":"url_detail",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_detail" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        return '<a class="btn btn-primary" href="'+ row.url_detail +'" style="width:3rem;"><i class="fas fa-search"></i></a>'
                                    };
                            }
                        },
                        {
                            "name":"url_update",
                            "data":"url_update",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_update){
                                    return '<a class="btn btn-primary" href="'+ row.url_update +'" style="width:3rem;"><i class="fas fa-pen"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_delete",
                            "data":"url_delete",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_delete" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_delete){
                                    return '<a class="btn btn-danger" href="'+ row.url_delete +'" style="width:3rem;"><i class="fas fa-trash"></i></a>'
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
                                    return '<a class="btn btn-success" href="'+row.url_authorize_true +'" style="width:3rem;"><i class="fas fa-certificate"></i></a>'
                                }else{
                                    return ''
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
                                    return '<a class="btn btn-danger" href="'+row.url_authorize_false +'" style="width:3rem;"><i class="fas fa-certificate"></i></a>'
                                }else{
                                    return ''
                                };
                            }
                        },
                        {
                            "name":"url_sent",
                            "data":"url_sent",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_sent" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_sent){
                                    return '<a class="btn btn-danger" href="'+row.url_sent +'" style="width:3rem;"><i class="fas fa-truck"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_recived",
                            "data":"url_recived",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_recived" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_recived){
                                    return '<a class="btn btn-danger" href="'+row.url_recived +'" style="width:3rem;"><i class="fas fa-truck-loading"></i></a>'
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
                                    return '<a class="btn btn-success" href="'+row.url_booking_true +'" style="width:3rem;"><i class="fas fa-warehouse"></i></a>'
                                }else{
                                    return ''
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
                                    return '<a class="btn btn-danger" href="'+row.url_booking_false +'" style="width:3rem;"><i class="fas fa-warehouse"></i></a>'
                                }else{
                                    return ''
                                };
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createList('id_order',dataset,col,[[12,'desc'],[13,'desc']],print);
                };
            },
        });
        
    });
}
