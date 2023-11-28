function orderdata_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    // Create
                    if(dataset.create_date && dataset.create_time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create_date+' '+dataset.create_time);
                    };
                    if(dataset.create_username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create_username);
                    };
                    // Update
                    if(dataset.update_date && dataset.update_time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update_date+' '+dataset.update_time);
                    };
                    if(dataset.update_username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update_username);
                    };
                    // Company
                    if(dataset.company_name && document.getElementById('id_company')){
                        document.getElementById('id_company').setAttribute('value',dataset.company_name);
                    };
                    if(dataset.company_url_detail && document.getElementById('id_company_url_detail')){
                        document.getElementById('id_company_url_detail').setAttribute('href',dataset.company_url_detail);
                    };
                    // Company Item
                    if(dataset.companyitem_name && document.getElementById('id_companyitem')){
                        document.getElementById('id_companyitem').setAttribute('value',dataset.companyitem_name);
                    };
                    if(dataset.companyitem_url_detail && document.getElementById('id_companyitem_url_detail')){
                        document.getElementById('id_companyitem_url_detail').setAttribute('href',dataset.companyitem_url_detail);
                    };
                    // Order
                    if(dataset.order_reference_number && document.getElementById('id_order_reference_number')){
                        document.getElementById('id_order_reference_number').setAttribute('value',dataset.order_reference_number);
                    };
                    if(dataset.order_url_detail && document.getElementById('id_order_url_detail')){
                        document.getElementById('id_order_url_detail').setAttribute('href',dataset.order_url_detail);
                    };
                    // Amount
                    if(dataset.amount && document.getElementById("id_amount")){
                        document.getElementById("id_amount").setAttribute('value',dataset.amount);
                    };
                    if(dataset.unit && document.getElementById("id_unit2")){
                        document.getElementById("id_unit").innerHTML=dataset.unit;
                    };
                    if(dataset.price && document.getElementById("id_price")){
                        document.getElementById("id_price").setAttribute('value',dataset.price);
                    };
                    if(dataset.value && document.getElementById("id_value")){
                        document.getElementById("id_value").setAttribute('value',dataset.value + " €");
                    };
                    // Authorized
                    if(dataset.authorized == true && document.getElementById('id_authorize_icon')){
                        document.getElementById('id_authorize_icon').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_authorize_icon').innerHTML='<i class="fas fa-check"></i>';
                    } else if (dataset.authorized == false && document.getElementById('id_authorize_icon')){
                        document.getElementById('id_authorize_icon').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_authorize_icon').innerHTML='<i class="fas fa-times"></i>';
                    };
                    if(dataset.authorized_date && dataset.authorized_time && document.getElementById('id_authorized_datetime')){
                        document.getElementById('id_authorized_datetime').setAttribute('value',dataset.authorized_date+' '+dataset.authorized_time);
                    };
                    if(dataset.authorized_username && document.getElementById('id_authorized_username')){
                        document.getElementById('id_authorized_username').setAttribute('value',dataset.authorized_username);
                    };
                    if(dataset.url_authorize_true && document.getElementById('id_url_authorize_true')){
                        document.getElementById('id_url_authorize_true').setAttribute("href",dataset.url_authorize_true);
                    };
                    if(dataset.url_authorize_false && document.getElementById('id_url_authorize_false')){
                        document.getElementById('id_url_authorize_false').setAttribute("href",dataset.url_authorize_false);
                    };
                    // Booking
                    if(dataset.booking == true && document.getElementById('id_booking_icon')){
                        document.getElementById('id_booking_icon').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_booking_icon').innerHTML='<i class="fas fa-warehouse"></i>';
                    } else if (dataset.booking == false && document.getElementById('id_booking_icon')){
                        document.getElementById('id_booking_icon').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_booking_icon').innerHTML='<i class="fas fa-warehouse"></i>';
                    };
                    if(dataset.booking_date && dataset.booking_time && document.getElementById('id_booking_datetime')){
                        document.getElementById('id_booking_datetime').setAttribute('value',dataset.booking_date+' '+dataset.booking_time);
                    };
                    if(dataset.booking_username && document.getElementById('id_booking_username')){
                        document.getElementById('id_booking_username').setAttribute('value',dataset.booking_username);
                    };
                    if(dataset.url_booking_true && document.getElementById('id_url_booking_true')){
                        document.getElementById('id_url_booking_true').setAttribute("href",dataset.url_booking_true);
                    };
                    if(dataset.url_booking_false && document.getElementById('id_url_booking_false')){
                        document.getElementById('id_url_booking_false').setAttribute("href",dataset.url_booking_false);
                    };
                };
            },
        });
        
    });
}
