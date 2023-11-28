function company_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        // Logo
                        if(element.logo_url && document.getElementById("id_logo-"+element.id)){
                            document.getElementById("id_logo-"+element.id).setAttribute("source",element.logo_url);
                        };
                        // Company Item
                        if(element.name && document.getElementById("id_company-"+element.id)){
                            document.getElementById("id_company-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_company-"+element.id)){
                            document.getElementById("id_company-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Telephone
                        if(element.telephone && document.getElementById("id_telephone-"+element.id)){
                            document.getElementById("id_telephone-"+element.id).innerHTML = element.telephone;
                        };
                        // Email
                        if(element.email && document.getElementById("id_email-"+element.id)){
                            document.getElementById("id_email-"+element.id).innerHTML = element.email;
                        };
                        // Company Contact Count
                        if(element.companycontact_count && document.getElementById("id_companycontact_count-"+element.id)){
                            document.getElementById("id_companycontact_count-"+element.id).innerHTML = element.companycontact_count;
                        };
                        // Company Item Count
                        if(element.companyitem_count && document.getElementById("id_companyitem_count-"+element.id)){
                            document.getElementById("id_companyitem_count-"+element.id).innerHTML = element.companyitem_count;
                        };
                    });
                };
            },
        });
        
    });
}
