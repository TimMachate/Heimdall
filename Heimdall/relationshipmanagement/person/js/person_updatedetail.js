function person_updatedetail(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
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
                    if(dataset.company){
                        if(dataset.company.name && document.getElementById("id_company_id")){
                            document.getElementById("id_company_id").setAttribute("value",dataset.company.name);
                        };
                        if(dataset.company.url_detail && document.getElementById("id_company_url_detail")){
                            document.getElementById("id_company_url_detail").setAttribute("href",dataset.company.url_detail);
                        };
                    };
                    if(dataset.create){
                        if(dataset.create.date && dataset.create.time && document.getElementById('id_create_datetime')){
                            document.getElementById('id_create_datetime').setAttribute('value',dataset.create.date+' '+dataset.create.time);
                        };
                        if(dataset.create.username && document.getElementById('id_create_username')){
                            document.getElementById('id_create_username').setAttribute('value',dataset.create.username);
                        };
                    };
                    if(dataset.update){
                        if(dataset.update.date && dataset.create.time && document.getElementById('id_update_datetime')){
                            document.getElementById('id_update_datetime').setAttribute('value',dataset.update.date+' '+dataset.create.time);
                        };
                        if(dataset.update.username && document.getElementById('id_update_username')){
                            document.getElementById('id_update_username').setAttribute('value',dataset.update.username);
                        };
                    };
                    if(dataset.telephones){
                        if(dataset.telephones.count && document.getElementById("id_telephone_count")){
                            document.getElementById("id_telephone_count").innerHTML=dataset.telephones.count;
                        };
                    };
                    if (dataset.telephones){
                        if (dataset.telephones.data){
                            dataset.telephones.data.forEach(element => {
                                if(element.type && document.getElementById("id_telephone_type-"+element.id)){
                                    if (element.type == "Telefon"){
                                        document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-phone"></i>';
                                    } else if(element.type == "Handy"){
                                        document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-mobile"></i>';
                                    } else if(element.type == "Fax"){
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
                    };
                    if(dataset.emails){
                        if(dataset.emails.count && document.getElementById("id_email_count")){
                            document.getElementById("id_email_count").innerHTML=dataset.emails.count;
                        };
                    };
                    if (dataset.emails){
                        if (dataset.emails.data){
                            dataset.emails.data.forEach(element => {
                                if(element.email && document.getElementById("id_email_email-"+element.id)){
                                    document.getElementById("id_email_email-"+element.id).setAttribute("value",element.email);
                                };
                                if(element.target && document.getElementById("id_email_target-"+element.id)){
                                    document.getElementById("id_email_target-"+element.id).setAttribute("value",element.target);
                                };
                            });
                        };                     
                    };
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML=dataset.notice;
                    };
                };
            },
        });
        
    });
}
