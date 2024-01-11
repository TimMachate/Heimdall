function supplier_overview(api_url,model) {
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
                        if(element.name && document.getElementById("id_supplier-"+element.id)){
                            document.getElementById("id_supplier-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_supplier-"+element.id)){
                            document.getElementById("id_supplier-"+element.id).setAttribute("href",element.url_detail);
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
                        if(element.suppliercontact_count && document.getElementById("id_suppliercontact_count-"+element.id)){
                            document.getElementById("id_suppliercontact_count-"+element.id).innerHTML = element.suppliercontact_count;
                        };
                        // Company Item Count
                        if(element.supplieritem_count && document.getElementById("id_supplieritem_count-"+element.id)){
                            document.getElementById("id_supplieritem_count-"+element.id).innerHTML = element.supplieritem_count;
                        };
                    });
                };
            },
        });
        
    });
}
