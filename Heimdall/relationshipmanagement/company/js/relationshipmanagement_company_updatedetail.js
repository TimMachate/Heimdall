function company_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
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
                    if(dataset.logo && document.getElementById("id_logo_url")){
                        document.getElementById("id_logo_url").setAttribute("href",dataset.logo);
                    };
                    if(dataset.logo && document.getElementById("id_logo")){
                        document.getElementById("id_logo").innerHTML=dataset.logo;
                    };
                    if(dataset.street && document.getElementById("id_street")){
                        document.getElementById("id_street").setAttribute("value",dataset.street);
                    };
                    if(dataset.house_number && document.getElementById("id_house_number")){
                        document.getElementById("id_house_number").setAttribute("value",dataset.house_number);
                    };
                    if(dataset.post_code && document.getElementById("id_post_code")){
                        document.getElementById("id_post_code").setAttribute("value",dataset.post_code);
                    };
                    if(dataset.city && document.getElementById("id_city")){
                        document.getElementById("id_city").setAttribute("value",dataset.city);
                    };
                    if(dataset.country && document.getElementById("id_country")){
                        document.getElementById("id_country").setAttribute("value",dataset.country);
                    };
                    if(dataset.telephone){
                        if(dataset.telephone && document.getElementById("id_telephone")){
                            document.getElementById("id_telephone").setAttribute('value',dataset.telephone);
                        };
                    };
                    if(dataset.email){
                        if(dataset.email && document.getElementById("id_email")){
                            document.getElementById("id_email").setAttribute('value',dataset.email);
                        };
                    };
                    if(dataset.supplier && document.getElementById("id_supplier")){
                        document.getElementById("id_supplier").setAttribute("checked",true)
                    };
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML=dataset.notice;
                    };
                    // Company Contact
                    if(dataset.companycontact_count && document.getElementById("id_companycontact_count")){
                        document.getElementById("id_companycontact_count").setAttribute("value",dataset.companycontact_count);
                    };
                    // Company Item
                    if(dataset.companyitem_count && document.getElementById("id_companyitem_count")){
                        document.getElementById("id_companyitem_count").setAttribute("value",dataset.companyitem_count);
                    };
                };
            },
        });
        
    });
}
