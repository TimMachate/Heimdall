function offer_overview(api_url,model) {
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
                            "name":"create_date",
                            "data":"create_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.create_date && row.create_time && row.create_username){
                                    return row.create_date + ' ' + row.create_time + '<br>' + row.create_username
                                } else {
                                    return row.create_date + ' ' + row.create_time
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
                                if(row.company_name && row.company_url_detail && row.company_reference_number){
                                    return '<a class="link-dark text-decoration-none" href="'+row.company_url_detail+'">'+row.company_name+'<br>'+row.company_reference_number+'</a>'
                                }else{
                                    return row.company_name
                                };
                            }
                        },
                        {
                            "name":"item_data",
                            "data":"item_data",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_data" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.item_data){
                                    result = ''
                                    row.item_data.forEach(element => {
                                        result += element.companyitem_name
                                        result += '<br>'+element.companyitem_item_number
                                        result += '<br>'
                                    });
                                    return result
                                };
                            }
                        },
                        {
                            "name":"item_data",
                            "data":"item_data",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_data" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.item_data){
                                    result = ''
                                    row.item_data.forEach(element => {
                                        result += element.amount + ' ' + element.unit
                                        result += '<br>'
                                        result += '<br>'   
                                    });
                                    return result
                                };
                            }
                        },
                        {
                            "name":"item_data",
                            "data":"item_data",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_data" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.item_data){
                                    result = ''
                                    row.item_data.forEach(element => {
                                        result += element.price+" € / "+element.unit
                                        result += '<br>'
                                        result += '<br>'   
                                    });
                                    return result
                                };
                            }
                        },
                        {
                            "name":"item_data",
                            "data":"item_data",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_data" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.item_data){
                                    result = ''
                                    row.item_data.forEach(element => {
                                        result += element.value+" €"
                                        result += '<br>'
                                        result += '<br>'   
                                    });
                                    return result
                                };
                            }
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
                    createList('id_offer',dataset,col,[[1,'desc'],[2,'desc']],print);
                };
            },
        });
        
    });
}