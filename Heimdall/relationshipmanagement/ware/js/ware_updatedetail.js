function ware_updatedetail(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.ware_number && document.getElementById("id_ware_number")){
                        document.getElementById("id_ware_number").setAttribute("value",dataset.ware_number);
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
                    if(dataset.unit_package && document.getElementById("id_unit_package")){
                        document.getElementById("id_unit_package").setAttribute("value",dataset.unit_package);
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
