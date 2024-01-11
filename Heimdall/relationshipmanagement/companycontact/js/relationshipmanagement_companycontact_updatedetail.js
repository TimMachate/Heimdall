function companycontact_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.last_name && document.getElementById("id_last_name")){
                        document.getElementById("id_last_name").setAttribute("value",dataset.last_name);
                    };
                    if(dataset.first_name && document.getElementById("id_first_name")){
                        document.getElementById("id_first_name").setAttribute("value",dataset.first_name);
                    };
                    if(dataset.company_name && document.getElementById("id_company")){
                        document.getElementById("id_company").setAttribute("value",dataset.company_name);
                    };
                    if(dataset.company_url_detail && document.getElementById("id_company_url_detail")){
                        document.getElementById("id_company_url_detail").setAttribute("href",dataset.company_url_detail);
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
                    if(dataset.telephone_count && document.getElementById("id_telephone_count")){
                        document.getElementById("id_telephone_count").innerHTML=dataset.telephone_count;
                    };
                    if (dataset.telephone_data){
                        dataset.telephone_data.forEach(element => {
                            if(element.types && document.getElementById("id_telephone_type-"+element.id)){
                                if (element.types == "Telefon"){
                                    document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-phone"></i>';
                                } else if(element.types == "Handy"){
                                    document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-mobile"></i>';
                                } else if(element.types == "Fax"){
                                    document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-fax"></i>';
                                };
                            };
                            if(element.number && document.getElementById("id_telephone_number-"+element.id)){
                                document.getElementById("id_telephone_number-"+element.id).setAttribute("value",element.number);
                            };
                            if(element.target && document.getElementById("id_telephone_target-"+element.id)){
                                document.getElementById("id_telephone_target-"+element.id).setAttribute("value",element.target);
                            };
                        });
                    };
                    if(dataset.email_count && document.getElementById("id_email_count")){
                        document.getElementById("id_email_count").innerHTML=dataset.email_count;
                    };
                    if (dataset.email_data){
                        dataset.email_data.forEach(element => {
                            if(element.email && document.getElementById("id_email_email-"+element.id)){
                                document.getElementById("id_email_email-"+element.id).setAttribute("value",element.email);
                            };
                            if(element.target && document.getElementById("id_email_target-"+element.id)){
                                document.getElementById("id_email_target-"+element.id).setAttribute("value",element.target);
                            };
                        });             
                    };
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML=dataset.notice;
                    };
                };
            },
        });
        
    });
}
