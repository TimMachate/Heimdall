function requestdata_overview(api_url,model) {
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
                            "name":"storageitem_name",
                            "data":"storageitem_name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "storageitem_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.storageitem_name && row.storageitem_url_detail && row.storageitem_reference_number){
                                    return '<a class="link-dark text-decoration-none" href="'+row.storageitem_url_detail+'">'+row.storageitem_name+'<br>'+row.storageitem_reference_number+'</a>'
                                }else{
                                    return row.storageitem_name
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
                                if(row.companyitem_name && row.companyitem_url_detail && row.companyitem_item_number){
                                    return '<a class="link-dark text-decoration-none" href="'+row.companyitem_url_detail+'">'+row.companyitem_name+'<br>'+row.companyitem_item_number+'</a>'
                                }else{
                                    return row.companyitem_name
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
                            "name":"amount",
                            "data":"amount",
                            "defaultContent": "",
                            "className":"",
                            "visible": "amount" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.amount && row.unit){
                                    return row.amount+ ' '+ row.unit
                                } else {
                                    return row.amount
                                };
                            }
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
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createList('id_requestdata',dataset,col,[[1,'desc'],[2,'desc']],print);
                };
            },
        });
        
    });
}
