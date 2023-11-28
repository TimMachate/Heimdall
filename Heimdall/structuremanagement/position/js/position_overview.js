function position_overview(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        if (element.name && document.getElementById('id_name-'+element.id)) {
                            document.getElementById('id_name-'+element.id).innerHTML = element.name
                        };
                        if (element.reference_number && document.getElementById('id_reference_number-'+element.id)) {
                            document.getElementById('id_reference_number-'+element.id).innerHTML = element.reference_number
                        };
                        if (element.url) {
                            if(element.url.detail && document.getElementById('id_url_detail-'+element.id)){
                                document.getElementById('id_url_detail-'+element.id).setAttribute('href',element.url.detail);
                            };
                        };
                        if(element.responsible){
                            if(element.responsible.name && document.getElementById('id_responsible_employee_id-'+element.id)){
                                document.getElementById('id_responsible_employee_id-'+element.id).innerHTML = element.responsible.name
                            };
                            if(element.responsible.email && document.getElementById('id_responsible_email-'+element.id)){
                                document.getElementById('id_responsible_email-'+element.id).innerHTML = element.responsible.email
                            };
                            if(element.responsible.telephone && document.getElementById('id_responsible_telephone-'+element.id)){
                                document.getElementById('id_responsible_telephone-'+element.id).innerHTML = element.responsible.telephone
                            };
                        };
                        if(element.substitute){
                            if(element.substitute.name && document.getElementById('id_substitute_employee_id-'+element.id)){
                                document.getElementById('id_substitute_employee_id-'+element.id).innerHTML = element.substitute.name
                            };
                            if(element.substitute.email && document.getElementById('id_substitute_email-'+element.id)){
                                document.getElementById('id_substitute_email-'+element.id).innerHTML = element.substitute.email
                            };
                            if(element.substitute.telephone && document.getElementById('id_substitute_telephone-'+element.id)){
                                document.getElementById('id_substitute_telephone-'+element.id).innerHTML = element.substitute.telephone
                            };
                        };
                        if(element.picture){
                            if(element.picture.url_file && document.getElementById('id_picture_id-'+element.id)){
                                document.getElementById('id_picture_id-'+element.id).setAttribute('src',element.picture.url_file);
                            };
                        }
                    });
                };
            },
        });
    });
}