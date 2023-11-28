function offer_list(api_url,model) {
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
                            "name":"authorized",
                            "data":"authorized",
                            "defaultContent": "",
                            "className":"",
                            "visible": "authorized" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.authorized){
                                    return '<span class="btn btn-success disabled" ><i class="fas fa-check"></i></span>'
                                }else{
                                    return '<span class="btn btn-danger disabled" ><i class="fas fa-times"></i></span>'
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
                                if(row.sent){
                                    return '<span class="btn btn-success disabled" ><i class="fas fa-check"></i></span>'
                                }else{
                                    return '<span class="btn btn-danger disabled" ><i class="fas fa-times"></i></span>'
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
                                if(row.recived){
                                    return '<span class="btn btn-success disabled" ><i class="fas fa-check"></i></span>'
                                }else{
                                    return '<span class="btn btn-danger disabled" ><i class="fas fa-times"></i></span>'
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
                            "name":"ordered",
                            "data":"ordered",
                            "defaultContent": "",
                            "className":"",
                            "visible": "ordered" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.ordered){
                                    return '<span class="btn btn-success disabled" ><i class="fas fa-check"></i></span>'
                                }else{
                                    return '<span class="btn btn-danger disabled" ><i class="fas fa-times"></i></span>'
                                };
                            }
                        },
                        {
                            "name":"ordered_date",
                            "data":"ordered_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "ordered_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.ordered_date){return row.ordered_date};}
                        },
                        {
                            "name":"ordered_time",
                            "data":"ordered_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "ordered_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.ordered_time){return row.ordered_time};}
                        },
                        {
                            "name":"ordered_username",
                            "data":"ordered_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "ordered_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.ordered_username && row.ordered_url_detail){
                                    return '<a class="link-dark" href="'+ row.ordered_url_detail +'">'+row.ordered_username+'</a>'
                                } else {
                                    return row.ordered_username
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
                            "name":"url_sent",
                            "data":"url_sent",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_sent" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_sent){
                                        return '<a class="btn btn-primary" href="'+ row.url_sent +'"><i class="fas fa-question"></i></a>'
                                    };
                            }
                        },
                        {
                            "name":"url_recived",
                            "data":"url_recived",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_recived" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_recived){
                                        return '<a class="btn btn-primary" href="'+ row.url_recived +'"><i class="fas fa-file"></i></a>'
                                    };
                            }
                        },
                        {
                            "name":"url_order_true",
                            "data":"url_order_true",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_order_true" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_order_true){
                                        return '<a class="btn btn-primary" href="'+ row.url_order_true +'"><i class="fas fa-truck"></i></a>'
                                    };
                            }
                        },
                        {
                            "name":"url_order_false",
                            "data":"url_order_false",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_order_false" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_order_false){
                                        return '<a class="btn btn-danger" href="'+ row.url_order_false +'"><i class="fas fa-truck"></i></a>'
                                    };
                            }
                        }
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createList('id_offer',dataset,col,[[3,'desc'],[4,'desc']],print);
                };
            },
        });
        
    });
}
