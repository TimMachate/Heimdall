function storage_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.storageitem_name && document.getElementById("id_storageitem")){
                        document.getElementById("id_storageitem").setAttribute("value",dataset.storageitem_name);
                    };
                    if(dataset.storageitem_url_detail && document.getElementById("id_storageitem_url_detail")){
                        document.getElementById("id_storageitem_url_detail").setAttribute("href",dataset.storageitem_url_detail);
                    };
                    if(dataset.booking_reference_number && document.getElementById("id_booking")){
                        document.getElementById("id_booking").setAttribute("value",dataset.booking_reference_number);
                    };
                    if(dataset.booking_url_detail && document.getElementById("id_booking_url_detail")){
                        document.getElementById("id_booking_url_detail").setAttribute("href",dataset.booking_url_detail);
                    };
                    if(dataset.create_date && dataset.create_time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create_date+' '+dataset.create_time);
                    };
                    if(dataset.create_username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create_username);
                    };
                    if(dataset.update_date && dataset.create_time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update_date+' '+dataset.update_time);
                    };
                    if(dataset.update_username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update_username);
                    };
                    if(dataset.companyitem_name && document.getElementById("id_companyitem")){
                        document.getElementById("id_companyitem").setAttribute("value",dataset.companyitem_name);
                    };
                    if(dataset.companyitem_url_detail && document.getElementById("id_companyitem_url_detail")){
                        document.getElementById("id_companyitem_url_detail").setAttribute("href",dataset.companyitem_url_detail);
                    };
                    if(dataset.company_name && document.getElementById("id_company")){
                        document.getElementById("id_company").setAttribute("value",dataset.company_name);
                    };
                    if(dataset.company_url_detail && document.getElementById("id_company_url_detail")){
                        document.getElementById("id_company_url_detail").setAttribute("href",dataset.company_url_detail);
                    };
                    if(dataset.unit && document.getElementById("id_unit")){
                        document.getElementById("id_unit").setAttribute("value",dataset.unit);
                    };
                    if(dataset.value && document.getElementById("id_value")){
                        document.getElementById("id_value").setAttribute('value',dataset.value);
                    };
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML=dataset.notice;
                    };
                };
            },
        });
        
    });
}
