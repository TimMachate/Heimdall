function process_overview(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url,
            success: function(dataset){
                dataset.forEach(element => {
                    if(element.url_detail){
                        document.getElementById("id_name_"+element.id).setAttribute('href',element.url_detail);
                    };
                    if(element.name){
                        document.getElementById("id_name_"+element.id).innerHTML = element.name;
                    };
                    if(element.reference_number){
                        document.getElementById("id_reference_number_"+element.id).innerHTML = element.reference_number;
                    };
                    if(element.url_data_add){
                        document.getElementById("id_url_processes_create_"+element.id).setAttribute('href',element.url.data_create);
                    };
                    if(element.processes.last){
                        document.getElementById("id_processes_last_"+element.id).setAttribute('href',element.processes.last.url_detail);
                        document.getElementById("id_processes_last_"+element.id).innerHTML = element.processes.last.begin.date + ' ' + element.processes.last.begin.time;
                    };
                    if(element.processes){
                        if(element.processes.status == "closed"){
                            document.getElementById("id_processes_last_status_"+element.id).setAttribute('class',"btn btn-danger");
                        } else if (element.processes.status == "running") {
                            document.getElementById("id_processes_last_status_"+element.id).setAttribute('class',"btn btn-warning");
                        } else {
                            document.getElementById("id_processes_last_status_"+element.id).setAttribute('class',"btn btn-success");
                        };
                    };
                    if(element.picture){
                        document.getElementById("id_image_"+element.id).setAttribute('src',element.picture.url_file);
                    };
                });
            },
        });
    });
}