function companyitem_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.url_request_create && document.getElementById("id_url_request_create")){
                        document.getElementById("id_url_request_create").setAttribute("href",dataset.url_request_create);
                    };
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.item_number && document.getElementById("id_item_number")){
                        document.getElementById("id_item_number").setAttribute("value",dataset.item_number);
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
                    if(dataset.image && document.getElementById("id_image_url")){
                        document.getElementById("id_image_url").setAttribute("href",dataset.image);
                    };
                    if(dataset.image && document.getElementById("id_image")){
                        document.getElementById("id_image").innerHTML=dataset.image;
                    };
                    if(dataset.unit && document.getElementById("id_unit")){
                        document.getElementById("id_unit").setAttribute("value",dataset.unit);
                    };
                    if(dataset.price && document.getElementById("id_price")){
                        document.getElementById("id_price").setAttribute("value",dataset.price);
                    };
                };
            },
        });
        
    });
}
