function order_table(api_url,model) {
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
                            "name":"done",
                            "data":"done",
                            "defaultContent": "",
                            "className":"",
                            "visible": "done" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.done == true){
                                    return 'true'
                                } else if (row.done == false) {
                                    return 'false'
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
                                    return 'true'
                                } else if (row.authorized == false) {
                                    return 'false'
                                } else {
                                    return ''
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
                                    return 'true'
                                } else if (row.booked == false) {
                                    return 'false'
                                } else {
                                    return ''
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
                                    return 'true'
                                } else if (row.sent == false) {
                                    return 'false'
                                } else {
                                    return ''
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
                                if (row.sent_username){
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
                                    return 'true'
                                } else if (row.recived == false) {
                                    return 'false'
                                } else {
                                    return ''
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
                                if (row.recived_username){
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
                            "render":function(data,type,row,meta){if (row.notice){return 'true'}else{return 'false'};}
                        },
                        {
                            "name":"url_detail",
                            "data":"url_detail",
                            "defaultContent": "",
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
                            "name":"url_sent",
                            "data":"url_sent",
                            "defaultContent": "",
                            "className":"",
                            "visible": "url_sent" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.url_sent){
                                    return row.url_sent
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
                                    return row.url_recived
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
                    createTable('id_order',dataset,col,[[12,'desc'],[13,'desc']],print);
                };
            },
        });
        
    });
}
