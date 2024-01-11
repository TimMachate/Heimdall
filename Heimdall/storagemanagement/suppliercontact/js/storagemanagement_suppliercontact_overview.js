function suppliercontact_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        // Supplier Item
                        if(element.name && document.getElementById("id_suppliercontact-"+element.id)){
                            document.getElementById("id_suppliercontact-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_suppliercontact-"+element.id)){
                            document.getElementById("id_suppliercontact-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Supplier
                        if(element.supplier_name && document.getElementById("id_supplier-"+element.id)){
                            document.getElementById("id_supplier-"+element.id).innerHTML = element.supplier_name;
                        };
                        if(element.supplier_url_detail && document.getElementById("id_supplier-"+element.id)){
                            document.getElementById("id_supplier-"+element.id).setAttribute("href",element.supplier_url_detail);
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
