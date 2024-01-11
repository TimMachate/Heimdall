function companyitem_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        // Company Item
                        if(element.name && document.getElementById("id_companyitem-"+element.id)){
                            document.getElementById("id_companyitem-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_companyitem-"+element.id)){
                            document.getElementById("id_companyitem-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Company
                        if(element.company_name && document.getElementById("id_company-"+element.id)){
                            document.getElementById("id_company-"+element.id).innerHTML = element.company_name;
                        };
                        if(element.company_url_detail && document.getElementById("id_company-"+element.id)){
                            document.getElementById("id_company-"+element.id).setAttribute("href",element.company_url_detail);
                        };
                        // Storage Item
                        if(element.storageitem_name && document.getElementById("id_storageitem-"+element.id)){
                            document.getElementById("id_storageitem-"+element.id).innerHTML = element.storageitem_name;
                        };
                        if(element.storageitem_url_detail && document.getElementById("id_storageitem-"+element.id)){
                            document.getElementById("id_storageitem-"+element.id).setAttribute("href",element.storageitem_url_detail);
                        };
                    });
                };
            },
        });
        
    });
}
