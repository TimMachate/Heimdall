function statusdata_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset.url){
                    if(dataset.url.detail && document.getElementById("id_url_detail")){
                        document.getElementById("id_url_detail").setAttribute("href",dataset.url.detail);
                    };
                };
                if(dataset.reference_number && document.getElementById("id_reference_number")){
                    document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                };
                if(dataset.status){
                    if(dataset.status.name && document.getElementById("id_status")){
                        document.getElementById("id_status").setAttribute("value",dataset.status.name);
                    };
                    if(dataset.status.url_detail && document.getElementById("id_status_url_detail")){
                        document.getElementById("id_status_url_detail").setAttribute("href",dataset.status.name);
                    };
                };
                if(dataset.device){
                    if(dataset.device.name && document.getElementById("id_device")){
                        document.getElementById("id_device").setAttribute("value",dataset.device.name);
                    };
                    if(dataset.device.url_detail && document.getElementById("id_device_url_detail")){
                        document.getElementById("id_device_url_detail").setAttribute("href",dataset.device.url_detail);
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
            },
        });
        
    });
}