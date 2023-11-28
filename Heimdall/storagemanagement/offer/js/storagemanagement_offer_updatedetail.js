function offer_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    // Company
                    if(dataset.company_name && document.getElementById('id_company')){
                        document.getElementById('id_company').setAttribute('value',dataset.company_name);
                    };
                    if(dataset.company_url_detail && document.getElementById('id_company_url_detail')){
                        document.getElementById('id_company_url_detail').setAttribute('href',dataset.company_url_detail);
                    };
                    // Offer File
                    if(dataset.offer_file_url && document.getElementById("id_offer_file_url")){
                        document.getElementById("id_offer_file_url").setAttribute('href',dataset.offer_file_url);
                    };
                    if(dataset.offer_file_name && document.getElementById("id_offer_file_name")){
                        document.getElementById("id_offer_file_name").innerHTML = dataset.offer_file_name;
                    };
                    // Create
                    if(dataset.create_date && dataset.create_time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create_date+' '+dataset.create_time);
                    };
                    if(dataset.create_username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create_username);
                    };
                    // Update
                    if(dataset.update_date && dataset.create_time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update_date+' '+dataset.update_time);
                    };
                    if(dataset.update_username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update_username);
                    };
                    // Sent
                    if(dataset.sent == true && document.getElementById('id_sent_icon')){
                        document.getElementById('id_sent_icon').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_sent_icon').innerHTML='<i class="fas fa-check"></i>';
                    } else if (dataset.sent == false && document.getElementById('id_sent_icon')){
                        document.getElementById('id_sent_icon').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_sent_icon').innerHTML='<i class="fas fa-times"></i>';
                    };
                    if(dataset.url_sent && document.getElementById('id_url_sent')){
                        document.getElementById('id_url_sent').setAttribute("href",dataset.url_sent);
                    };
                    if(dataset.sent_date && dataset.sent_time && document.getElementById('id_sent_datetime')){
                        document.getElementById('id_sent_datetime').setAttribute('value',dataset.sent_date+' '+dataset.sent_time);
                    };
                    if(dataset.sent_username && document.getElementById('id_sent_username')){
                        document.getElementById('id_sent_username').setAttribute('value',dataset.sent_username);
                    };
                    // Recived
                    if(dataset.recived == true && document.getElementById('id_recived_icon')){
                        document.getElementById('id_recived_icon').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_recived_icon').innerHTML='<i class="fas fa-check"></i>';
                    } else if (dataset.recived == false && document.getElementById('id_recived_icon')){
                        document.getElementById('id_recived_icon').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_recived_icon').innerHTML='<i class="fas fa-times"></i>';
                    };
                    if(dataset.url_recived && document.getElementById('id_url_recived')){
                        document.getElementById('id_url_recived').setAttribute("href",dataset.url_recived);
                    };
                    if(dataset.recived_date && dataset.recived_time && document.getElementById('id_recived_datetime')){
                        document.getElementById('id_recived_datetime').setAttribute('value',dataset.recived_date+' '+dataset.recived_time);
                    };
                    if(dataset.recived_username && document.getElementById('id_recived_username')){
                        document.getElementById('id_recived_username').setAttribute('value',dataset.recived_username);
                    };
                    // Ordered
                    if(dataset.ordered == true && document.getElementById('id_ordered_icon')){
                        document.getElementById('id_ordered_icon').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_ordered_icon').innerHTML='<i class="fas fa-check"></i>';
                    } else if (dataset.ordered == false && document.getElementById('id_ordered_icon')){
                        document.getElementById('id_ordered_icon').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_ordered_icon').innerHTML='<i class="fas fa-times"></i>';
                    };
                    if(dataset.url_order_true && document.getElementById('id_url_order_true')){
                        document.getElementById('id_url_order_true').setAttribute("href",dataset.url_order_true);
                    };
                    if(dataset.url_order_false && document.getElementById('id_url_order_false')){
                        document.getElementById('id_url_order_false').setAttribute("href",dataset.url_order_false);
                    };
                    if(dataset.ordered_date && dataset.ordered_time && document.getElementById('id_ordered_datetime')){
                        document.getElementById('id_ordered_datetime').setAttribute('value',dataset.ordered_date+' '+dataset.ordered_time);
                    };
                    if(dataset.ordered_username && document.getElementById('id_ordered_username')){
                        document.getElementById('id_ordered_username').setAttribute('value',dataset.ordered_username);
                    };
                    // Authorized
                    if(dataset.authorized == true && document.getElementById('id_authorize')){
                        document.getElementById('id_authorize').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_authorize').innerHTML='<i class="fas fa-check"></i>';
                    } else if (dataset.authorized == false && document.getElementById('id_authorize')){
                        document.getElementById('id_authorize').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_authorize').innerHTML='<i class="fas fa-times"></i>';
                    };
                    if(dataset.url_authorize_true && document.getElementById('id_url_authorize_true')){
                        document.getElementById('id_url_authorize_true').setAttribute("href",dataset.url_authorize_true);
                    };
                    if(dataset.url_authorize_false && document.getElementById('id_url_authorize_false')){
                        document.getElementById('id_url_authorize_false').setAttribute("href",dataset.url_authorize_false);
                    };
                    if(dataset.item_data.length != 0){
                        let items = [
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
                                "visible": "authorized" in dataset.item_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if(row.authorized){
                                        return '<span class="btn btn-success disabled" ><i class="fas fa-check"></i></span>'
                                    }else{
                                        return '<span class="btn btn-danger disabled" ><i class="fas fa-times"></i></span>'
                                    };
                                }
                            },
                            {
                                "name":"companyitem_name",
                                "data":"companyitem_name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "companyitem_name" in dataset.item_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if(row.companyitem_name){
                                        return row.companyitem_name + '<br>' + row.companyitem_item_number
                                    };
                                }
                            },
                            {
                                "name":"amount",
                                "data":"amount",
                                "defaultContent": "",
                                "className":"",
                                "visible": "amount" in dataset.item_data[0] ? true : false,
                                "render":function(data,type,row,meta){if(row.amount && row.unit){return row.amount+' '+row.unit};}
                            },
                            {
                                "name":"price",
                                "data":"price",
                                "defaultContent": "",
                                "className":"",
                                "visible": "price" in dataset.item_data[0] ? true : false,
                                "render":function(data,type,row,meta){if(row.price && row.unit){return row.price+" € / "+row.unit};}
                            },
                            {
                                "name":"value",
                                "data":"value",
                                "defaultContent": "",
                                "className":"",
                                "visible": "value" in dataset.item_data[0] ? true : false,
                                "render":function(data,type,row,meta){if(row.value){return row.value+" €"};}
                            },
                            {
                                "name":"url_detail",
                                "data":"url_detail",
                                "defaultContent": "",
                                "className":"",
                                "visible": "url_detail" in dataset.item_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        det = '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                    }else{det=""};
                                    if (row.url_update){
                                        up = '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                    }else{up=""};
                                    if (row.url_delete){
                                        de = '<a class="btn btn-danger" href="'+ row.url_delete +'"><i class="fas fa-trash"></i></a>'
                                    }else{de=""};
                                    if (row.url_authorize_true){
                                        at = '<a class="btn btn-success" href="'+ row.url_authorize_true +'"><i class="fas fa-check"></i></a>'
                                    }else{at=""};
                                    if (row.url_authorize_false){
                                        af = '<a class="btn btn-danger" href="'+ row.url_authorize_false +'"><i class="fas fa-times"></i></a>'
                                    }else{af=""};
                                    return '<div class="btn-group">'+det+up+de+at+af+'</div>'
                                }
                            },
                        ];
                        let print = [];
                        for (let i = 0; i < items.length; i++){
                            if (items[i]["visible"] === true) {print.push(i)};
                        };
                        transformTable("id_items",dataset.item_data,items,[[1,'asc']],print);
                    };
                };
            },
        });
        
    });
}
