function order_updatedetail(api_url,model) {
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
                        document.getElementById('id_company_url_detail').setAttribute('class','input-group-text btn btn-primary');
                    };
                    // Order File
                    if(dataset.order_file_url && document.getElementById("id_order_file_url")){
                        document.getElementById("id_order_file_url").setAttribute('href',dataset.order_file_url);
                        document.getElementById("id_order_file_url").setAttribute('class','input-group-text btn btn-primary');
                    };
                    if(dataset.order_file_name && document.getElementById("id_order_file_name")){
                        document.getElementById("id_order_file_name").setAttribute('value',dataset.order_file_name);
                    };
                    // Delivery Note
                    if(dataset.delivery_note_url && document.getElementById("id_delivery_note_url")){
                        document.getElementById("id_delivery_note_url").setAttribute('href',dataset.delivery_note_url);
                        document.getElementById("id_delivery_note_url").setAttribute('class','input-group-text btn btn-primary');
                    };
                    if(dataset.delivery_note_name && document.getElementById("id_delivery_note_name")){
                        document.getElementById("id_delivery_note_name").innerHTML = dataset.delivery_note_name;
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
                    // Item Count
                    if(dataset.item_count && document.getElementById("id_item_count")){
                        document.getElementById("id_item_count").setAttribute('value',dataset.item_count);
                    };
                    // Value
                    if(dataset.value && document.getElementById("id_value")){
                        document.getElementById("id_value").setAttribute('value',dataset.value);
                    };
                    // Sent
                    if(dataset.sent == true && document.getElementById('id_sent_icon')){
                        document.getElementById('id_sent_icon').setAttribute("class","input-group-text btn btn-success disabled");
                    } else if (dataset.sent == false && document.getElementById('id_sent_icon')){
                        document.getElementById('id_sent_icon').setAttribute("class","input-group-text btn btn-danger disabled");
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
                    } else if (dataset.recived == false && document.getElementById('id_recived_icon')){
                        document.getElementById('id_recived_icon').setAttribute("class","input-group-text btn btn-danger disabled");
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
                    // Notice
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML = dataset.notice;
                    };
                    // Authorized
                    if(dataset.authorized == true && document.getElementById('id_authorize')){
                        document.getElementById('id_authorize').setAttribute("class","input-group-text btn btn-success disabled");
                    } else if (dataset.authorized == false && document.getElementById('id_authorize')){
                        document.getElementById('id_authorize').setAttribute("class","input-group-text btn btn-danger disabled");
                    };
                    if(dataset.url_authorize_true && document.getElementById('id_url_authorize_true')){
                        document.getElementById('id_url_authorize_true').setAttribute("href",dataset.url_authorize_true);
                        document.getElementById('id_url_authorize_true').setAttribute("class",'btn btn-success');
                    };
                    if(dataset.url_authorize_false && document.getElementById('id_url_authorize_false')){
                        document.getElementById('id_url_authorize_false').setAttribute("href",dataset.url_authorize_false);
                        document.getElementById('id_url_authorize_false').setAttribute("class",'btn btn-danger');
                    };
                    // Order Data
                    if(dataset.item_data.length != 0){
                        for(let i = 0; i < dataset.item_data.length; i++){
                            if(dataset.item_data[i].url_detail && document.getElementById('id_orderdata_order-'+i+'-offer')){
                                document.getElementById('id_orderdata_order-'+i+'-offer').setAttribute('href',dataset.item_data[i].offer_url_detail);
                                document.getElementById('id_orderdata_order-'+i+'-offer').setAttribute('class','btn btn-primary mt-1');
                            };
                            if(dataset.item_data[i].companyitem_name && document.getElementById('id_orderdata_order-'+i+'-companyitem')){
                                document.getElementById('id_orderdata_order-'+i+'-companyitem').setAttribute('value',dataset.item_data[i].companyitem_name)
                            };
                            if(dataset.item_data[i].companyitem_item_number && document.getElementById('id_orderdata_order-'+i+'-companyitem_item_number')){
                                document.getElementById('id_orderdata_order-'+i+'-companyitem_item_number').setAttribute('value',dataset.item_data[i].companyitem_item_number)
                            };
                            if(dataset.item_data[i].amount && document.getElementById('id_orderdata_order-'+i+'-amount')){
                                document.getElementById('id_orderdata_order-'+i+'-amount').setAttribute('value',dataset.item_data[i].amount)
                            };
                            if(dataset.item_data[i].unit && document.getElementById('id_orderdata_order-'+i+'-unit')){
                                document.getElementById('id_orderdata_order-'+i+'-unit').innerHTML = dataset.item_data[i].unit
                            };
                            if(dataset.item_data[i].unit && document.getElementById('id_orderdata_order-'+i+'-unit2')){
                                document.getElementById('id_orderdata_order-'+i+'-unit2').innerHTML = '€ / '+dataset.item_data[i].unit
                            };
                            if(dataset.item_data[i].unit && document.getElementById('id_orderdata_order-'+i+'-unit3')){
                                document.getElementById('id_orderdata_order-'+i+'-unit3').innerHTML = dataset.item_data[i].unit
                            };
                            if(dataset.item_data[i].price && document.getElementById('id_orderdata_order-'+i+'-price')){
                                document.getElementById('id_orderdata_order-'+i+'-price').setAttribute('value',dataset.item_data[i].price)
                            };
                            if(dataset.item_data[i].amount_recived && document.getElementById('id_orderdata_order-'+i+'-amount_recived')){
                                document.getElementById('id_orderdata_order-'+i+'-amount_recived').setAttribute('value',dataset.item_data[i].amount_recived)
                            }else{
                                document.getElementById('id_orderdata_order-'+i+'-amount_recived').setAttribute('value',0)
                            };
                            if(dataset.item_data[i].value && document.getElementById('id_orderdata_order-'+i+'-value')){
                                document.getElementById('id_orderdata_order-'+i+'-value').setAttribute('value',dataset.item_data[i].value)
                            };
                            if(dataset.item_data[i].authorized && document.getElementById('id_orderdata_order-'+i+'-authorized')){
                                if(dataset.item_data[i].authorized == true){
                                    document.getElementById('id_orderdata_order-'+i+'-authorized').setAttribute('class','btn btn-success disabled mt-1');
                                }else if(dataset.item_data[i].authorized == false){
                                    document.getElementById('id_orderdata_order-'+i+'-authorized').setAttribute('class','btn btn-danger disabled mt-1');
                                }else{
                                    document.getElementById('id_orderdata_order-'+i+'-authorized').setAttribute('class','btn btn-secondary disabled mt-1');
                                };
                            };
                            if(dataset.item_data[i].booked && document.getElementById('id_orderdata_order-'+i+'-booked')){
                                if(dataset.item_data[i].booking == true){
                                    document.getElementById('id_orderdata_order-'+i+'-booked').setAttribute('class','btn btn-success disabled mt-1');
                                }else if(dataset.item_data[i].booking == false){
                                    document.getElementById('id_orderdata_order-'+i+'-booked').setAttribute('class','btn btn-danger disabled mt-1');
                                }else{
                                    document.getElementById('id_orderdata_order-'+i+'-booked').setAttribute('class','btn btn-secondary disabled mt-1');
                                };
                            };
                            if(dataset.item_data[i].notice && document.getElementById('id_orderdata_order-'+i+'-notice-icon')){
                                if(dataset.item_data[i].notice){
                                    document.getElementById('id_orderdata_order-'+i+'-notice-icon').setAttribute('class','btn btn-success disabled mt-1');
                                }else{
                                    document.getElementById('id_orderdata_order-'+i+'-notice-icon').setAttribute('class','btn btn-secondary disabled mt-1');
                                };
                            };
                            if(dataset.item_data[i].url_detail && document.getElementById('id_orderdata_order-'+i+'-url_detail')){
                                document.getElementById('id_orderdata_order-'+i+'-url_detail').setAttribute('class','btn btn-primary mt-1');
                                document.getElementById('id_orderdata_order-'+i+'-url_detail').setAttribute('href',dataset.item_data[i].url_detail);
                            };
                            if(dataset.item_data[i].url_update && document.getElementById('id_orderdata_order-'+i+'-url_update')){
                                document.getElementById('id_orderdata_order-'+i+'-url_update').setAttribute('class','btn btn-primary mt-1');
                                document.getElementById('id_orderdata_order-'+i+'-url_update').setAttribute('href',dataset.item_data[i].url_update);
                            };
                            if(dataset.item_data[i].url_authorize_true && document.getElementById('id_orderdata_order-'+i+'-url_authorize_true')){
                                document.getElementById('id_orderdata_order-'+i+'-url_authorize_true').setAttribute('class','btn btn-success mt-1');
                                document.getElementById('id_orderdata_order-'+i+'-url_authorize_true').setAttribute('href',dataset.item_data[i].url_authorize_true);
                            };
                            if(dataset.item_data[i].url_authorize_false && document.getElementById('id_orderdata_order-'+i+'-url_authorize_false')){
                                document.getElementById('id_orderdata_order-'+i+'-url_authorize_false').setAttribute('class','btn btn-danger mt-1');
                                document.getElementById('id_orderdata_order-'+i+'-url_authorize_false').setAttribute('href',dataset.item_data[i].url_authorize_false);
                            };
                            if(dataset.item_data[i].url_booking_true && document.getElementById('id_orderdata_order-'+i+'-url_booking_true')){
                                document.getElementById('id_orderdata_order-'+i+'-url_booking_true').setAttribute('class','btn btn-success mt-1');
                                document.getElementById('id_orderdata_order-'+i+'-url_booking_true').setAttribute('href',dataset.item_data[i].url_booking_true);
                            };
                            if(dataset.item_data[i].url_booking_false && document.getElementById('id_orderdata_order-'+i+'-url_booking_false')){
                                document.getElementById('id_orderdata_order-'+i+'-url_booking_false').setAttribute('class','btn btn-danger mt-1');
                                document.getElementById('id_orderdata_order-'+i+'-url_booking_false').setAttribute('href',dataset.item_data[i].url_booking_false);
                            };
                        };
                    };
                };
            },
        });
        
    });
}