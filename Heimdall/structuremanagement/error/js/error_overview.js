function error_overview(api_data_url){
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
                        if (element.url.detail && document.getElementById('id_name-'+element.id)){
                            document.getElementById('id_name-'+element.id).setAttribute('href',element.url.detail);
                        };
                    };
                    if (element.url) {
                        if (element.url.data_create && document.getElementById('id_error_url_data_create-'+element.id)){
                            document.getElementById('id_error_url_data_create-'+element.id).setAttribute('href',element.url.data_create);
                        };
                    };
                    if(element.error_last){
                        if(element.error_last.create.date && element.error_last.create.time && document.getElementById('id_error_last-'+element.id)){
                            document.getElementById('id_error_last-'+element.id).innerHTML = element.error_last.create.date + " " + element.error_last.create.time;
                        };
                        if(element.error_last.url_detail && document.getElementById('id_error_last-'+element.id)){
                            document.getElementById('id_error_last-'+element.id).setAttribute('href',element.error_last.url_detail);
                        };
                    };
                    if(element.error_last){
                        if(element.error_last.device){
                            if(element.error_last.device.name && document.getElementById('id_device-'+element.id)){
                                document.getElementById('id_device-'+element.id).innerHTML = element.error_last.device.name;
                            };
                            if(element.error_last.device.url_detail && document.getElementById('id_device-'+element.id)){
                                document.getElementById('id_device-'+element.id).setAttribute('href',element.error_last.device.url_detail);
                            };
                        };
                    };
                });
            },
        });
    });
}