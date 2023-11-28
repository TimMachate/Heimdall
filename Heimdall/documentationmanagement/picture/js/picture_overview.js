function picture_overview(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        if (element.name) {
                            document.getElementById('id_name-'+element.id).innerHTML = element.name
                        };
                        if (element.reference_number) {
                            document.getElementById('id_reference_number-'+element.id).innerHTML = element.reference_number
                        };
                        if (element.url_detail) {
                            document.getElementById('id_url_detail-'+element.id).setAttribute('href',element.url_detail);
                        };
                        if(element.url_file){
                            document.getElementById('id_picture-'+element.id).setAttribute('src',element.url_file);
                        };
                        if(element.url_file){
                            document.getElementById('id_picture_url_detail-'+element.id).setAttribute('href',element.url_file);
                        };
                    });
                };
            },
        });
    });
}