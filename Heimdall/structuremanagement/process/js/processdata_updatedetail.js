function processdata_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset.url){
                    if(dataset.url.detail && document.getElementById("id_url_detail")){
                        document.getElementById("id_url_detail").setAttribute("href",dataset.url.detail);
                    };
                };
                if(dataset.reference_number && document.getElementById("id_reference_number")){
                    document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                };
                if(dataset.process){
                    if(dataset.process.name && dataset.process.reference_number && document.getElementById("id_process")){
                        document.getElementById("id_process").setAttribute("value",dataset.process.name + ' (' + dataset.process.reference_number + ')')
                    };
                    if(dataset.process.url_detail && document.getElementById("id_process_url_detail")){
                        document.getElementById("id_process_url_detail").setAttribute("href",dataset.process.url_detail)
                    };
                };
                if(dataset.device){
                    if(dataset.device.name && dataset.device.reference_number && document.getElementById("id_device")){
                        document.getElementById("id_device").setAttribute("value",dataset.device.name + ' (' + dataset.device.reference_number + ')')
                    };
                    if(dataset.device.url_detail && document.getElementById("id_device_url_detail")){
                        document.getElementById("id_device_url_detail").setAttribute("href",dataset.device.url_detail)
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
                if(dataset.duration_formated && document.getElementById('id_duration')){
                    document.getElementById('id_duration').setAttribute('value',dataset.duration_formated)
                };
                if(dataset.count && document.getElementById('id_count')){
                    document.getElementById('id_count').setAttribute('value',dataset.count)
                };
                if(dataset.utilization){
                    if(dataset.utilization.percentage && document.getElementById("id_utilization")){
                        document.getElementById("id_utilization").setAttribute('value',dataset.utilization.percentage)
                    };
                };
                if(dataset.begin){
                    if(dataset.begin.date && dataset.begin.time && document.getElementById('id_begin_datetime')){
                        document.getElementById('id_begin_datetime').setAttribute('value',dataset.begin.date+' '+dataset.begin.time);
                    };
                    if(dataset.begin.username && document.getElementById('id_begin_username')){
                        document.getElementById('id_begin_username').setAttribute('value',dataset.begin.username);
                    };
                };
                if(dataset.end){
                    if(dataset.end.date && dataset.end.time && document.getElementById('id_end_datetime')){
                        document.getElementById('id_end_datetime').setAttribute('value',dataset.end.date+' '+dataset.end.time);
                    };
                    if(dataset.end.username && document.getElementById('id_end_username')){
                        document.getElementById('id_end_username').setAttribute('value',dataset.end.username);
                    };
                };
                if(dataset.notice && document.getElementById("id_notice")){
                    document.getElementById("id_notice").innerHTML = dataset.notice;
                };
            },
        });
        
    });
}