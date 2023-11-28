function maintenance_overview(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url,
            success: function(dataset){
                dataset.forEach(element => {
                    if (element.name && document.getElementById('id_name-'+element.id)) {
                        document.getElementById('id_name-'+element.id).innerHTML = element.name;
                    };
                    if (element.reference_number && document.getElementById('id_reference_number-'+element.id)) {
                        document.getElementById('id_reference_number-'+element.id).innerHTML = element.reference_number;
                    };
                    if (element.url) {
                        if (element.url.detail && document.getElementById('id_url_detail-'+element.id)){
                            document.getElementById('id_url_detail-'+element.id).setAttribute('href',element.url.detail);
                        };
                    };
                    if(element.device){
                        if(element.device.name && document.getElementById('id_device-'+element.id)){
                            document.getElementById('id_device-'+element.id).innerHTML = element.device.name;
                        };
                        if(element.device.url_detail && document.getElementById('id_device_url_detail-'+element.id)){
                            document.getElementById('id_device_url_detail-'+element.id).setAttribute('href',element.device.url_detail);
                        };
                    };
                    if(element.maintenance_next && document.getElementById('id_maintenance_next-'+element.id)){
                        document.getElementById('id_maintenance_next-'+element.id).innerHTML = element.maintenance_next.datetime_formated
                    };
                    if(element.status && document.getElementById('id_maintenance_next-'+element.id)){
                        if(element.status == 'alarm'){
                            document.getElementById('id_maintenance_next-'+element.id).setAttribute("class","btn btn-danger form-control")
                        } else if (element.status == 'warning'){
                            document.getElementById('id_maintenance_next-'+element.id).setAttribute("class","btn btn-warning form-control")
                        } else if (element.status == 'OK'){
                            document.getElementById('id_maintenance_next-'+element.id).setAttribute("class","btn btn-secondary form-control")
                        } else {
                            document.getElementById('id_maintenance_next-'+element.id).setAttribute("class","btn btn-secondary form-control")
                        };
                    };
                    if(element.url.data_create){
                        if(element.url.data_create && document.getElementById('id_maintenance_next_data_create-'+element.id)){
                            document.getElementById('id_maintenance_next_data_create-'+element.id).setAttribute("href",element.url.data_create)
                        };
                    };
                    if(element.maintenance_last){
                        if(element.maintenance_last.create.date && element.maintenance_last.create.time && document.getElementById('id_maintenance_last-'+element.id)){
                            document.getElementById('id_maintenance_last-'+element.id).innerHTML = element.maintenance_last.create.date + " " + element.maintenance_last.create.time
                        };
                        if(element.maintenance_last.url_detail && document.getElementById('id_maintenance_last_data_create-'+element.id)){
                            document.getElementById('id_maintenance_last_data_create-'+element.id).setAttribute("href",element.maintenance_last.url_detail)
                        };
                    };
                });
            }
        });
    });
}