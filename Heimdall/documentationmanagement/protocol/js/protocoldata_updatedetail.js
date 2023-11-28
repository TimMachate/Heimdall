function protocoldata_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.file && document.getElementById("id_url_file")){
                        document.getElementById("id_url_file").setAttribute("href",dataset.file);
                    };
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.protocol){
                        if(dataset.protocol.name && document.getElementById("id_protocol_id")){
                            document.getElementById("id_protocol_id").setAttribute("value",dataset.protocol.name);
                        };
                        if(dataset.protocol.url_detail && document.getElementById("id_protocol_id_url_detail")){
                            document.getElementById("id_protocol_id_url_detail").setAttribute("href",dataset.protocol.url_detail);
                        };
                    };
                    if(dataset.topic && document.getElementById("id_topic")){
                        document.getElementById("id_topic").innerHTML = dataset.topic;
                    };
                    if(dataset.procedure && document.getElementById("id_procedure")){
                        document.getElementById("id_procedure").innerHTML = dataset.procedure;
                    };
                    if(dataset.steps){
                        dataset.steps.forEach(element => {
                            if(element.order && document.getElementById("id_order-"+element.id)){
                                document.getElementById("id_order-"+element.id).innerHTML = element.order
                            };
                            if(element.name && document.getElementById("id_name-"+element.id)){
                                document.getElementById("id_name-"+element.id).innerHTML = element.name
                            };
                            if(element.text && document.getElementById("id_text-"+element.id)){
                                document.getElementById("id_text-"+element.id).innerHTML = element.text
                            };
                            if(element.variables){
                                element.variables.forEach(v =>{
                                    if(v.name && document.getElementById("id_name-"+element.id+'-'+v.id)){
                                        document.getElementById("id_name-"+element.id+'-'+v.id).innerHTML = v.name
                                    };
                                    if(v.symbol && document.getElementById("id_symbol-"+element.id+'-'+v.id)){
                                        document.getElementById("id_symbol-"+element.id+'-'+v.id).innerHTML = v.symbol
                                    };
                                    if(v.value && document.getElementById("id_value-"+element.id+'-'+v.id)){
                                        if(document.getElementById("id_value-"+element.id+'-'+v.id).type == 'checkbox'){
                                            document.getElementById("id_value-"+element.id+'-'+v.id).setAttribute('checked',true);
                                        } else {
                                            document.getElementById("id_value-"+element.id+'-'+v.id).setAttribute('value',v.value);
                                        };
                                    };
                                    if(v.unit && document.getElementById("id_unit-"+element.id+'-'+v.id)){
                                        document.getElementById("id_unit-"+element.id+'-'+v.id).innerHTML = v.unit
                                    };
                                });
                            };
                        });
                    };
                    if(dataset.version && document.getElementById("id_version")){
                        document.getElementById("id_version").setAttribute("value",dataset.version);
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
                        if(dataset.update.date && dataset.update.time && document.getElementById('id_update_datetime')){
                            document.getElementById('id_update_datetime').setAttribute('value',dataset.update.date+' '+dataset.update.time);
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