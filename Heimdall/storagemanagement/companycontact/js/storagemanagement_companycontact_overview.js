function companycontact_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        // Company Item
                        if(element.name && document.getElementById("id_companycontact-"+element.id)){
                            document.getElementById("id_companycontact-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_companycontact-"+element.id)){
                            document.getElementById("id_companycontact-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Company
                        if(element.company_name && document.getElementById("id_company-"+element.id)){
                            document.getElementById("id_company-"+element.id).innerHTML = element.company_name;
                        };
                        if(element.company_url_detail && document.getElementById("id_company-"+element.id)){
                            document.getElementById("id_company-"+element.id).setAttribute("href",element.company_url_detail);
                        };
                        // Emails
                        if(element.email_data){
                            element.email_data.forEach(email => {
                                if(email.email && document.getElementById("id_email-"+element.id+"-"+email.id)){
                                    document.getElementById("id_email-"+element.id+"-"+email.id).innerHTML = email.email
                                };
                            });
                        };
                        // Telephones
                        if(element.telephone_data){
                            element.telephone_data.forEach(phone => {
                                if(phone.types){
                                    if (phone.types == "Telefon"){
                                        document.getElementById("id_telephone_type-"+element.id+"-"+phone.id).setAttribute('class','fas fa-phone');
                                    } else if(phone.types == "Handy"){
                                        document.getElementById("id_telephone_type-"+element.id+"-"+phone.id).setAttribute('class','fas fa-mobile');
                                    } else if(phone.types == "Fax"){
                                        document.getElementById("id_telephone_type-"+element.id+"-"+phone.id).setAttribute('class','fas fa-fax');
                                    };
                                };
                                if(phone.number && document.getElementById("id_telephone-"+element.id+"-"+phone.id)){
                                    document.getElementById("id_telephone-"+element.id+"-"+phone.id).innerHTML = phone.number
                                };
                            });
                        };
                    });
                };
            },
        });
        
    });
}
