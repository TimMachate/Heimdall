function variable_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.url_detail && document.getElementById("id_url_detail")){
                        document.getElementById("id_url_detail").setAttribute("href",dataset.url_detail);
                    };
                    if(dataset.url_update && document.getElementById("id_url_update")){
                        document.getElementById("id_url_update").setAttribute("href",dataset.url_update);
                    };
                    if(dataset.url_delete && document.getElementById("id_url_delete")){
                        document.getElementById("id_url_delete").setAttribute("href",dataset.url_delete);
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.symbol && document.getElementById("id_symbol")){
                        document.getElementById("id_symbol").setAttribute("value",dataset.symbol);
                    };
                    if(dataset.unit && document.getElementById("id_unit")){
                        document.getElementById("id_unit").setAttribute("value",dataset.unit);
                    };
                    if(dataset.input_type && document.getElementById("id_input_type")){
                        document.getElementById("id_input_type").setAttribute("value",dataset.input_type);
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
                };
            },
        });
        
    });
}