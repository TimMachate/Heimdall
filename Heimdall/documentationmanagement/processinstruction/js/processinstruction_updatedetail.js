function processinstruction_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.url_file_qrcode){
                        document.getElementById("id_image_file_url").setAttribute("src",dataset.url_file_qrcode);
                    };
                    if(dataset.url_file){
                        document.getElementById("id_url_file").setAttribute("href",dataset.url_file);
                    };
                    if(dataset.reference_number){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.url_detail && document.getElementById("id_url_detail")){
                        document.getElementById("id_url_detail").setAttribute("href",dataset.url_detail);
                    };
                    if(dataset.url_update && document.getElementById("id_url_update")){
                        document.getElementById("id_url_update").setAttribute("href",dataset.url_update);
                    };
                    if(dataset.url_delete){
                        document.getElementById("id_url_delete").setAttribute("href",dataset.url_delete);
                    };
                    if(dataset.name){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.type){
                        document.getElementById("id_type").setAttribute("value",dataset.type);
                    };
                    if(dataset.version && document.getElementById("id_version")){
                        document.getElementById("id_version").setAttribute("value",dataset.version);
                    };
                    if(dataset.version_suffix && document.getElementById("id_version_suffix")){
                        document.getElementById("id_version_suffix").innerHTML = "-"+dataset.version_suffix;
                    };
                    if(dataset.create){
                        if(dataset.create.date && dataset.create.time){
                            document.getElementById('id_create_datetime').setAttribute('value',dataset.create.date+' '+dataset.create.time);
                        };
                        if(dataset.create.username){
                            document.getElementById('id_create_username').setAttribute('value',dataset.create.username);
                        };
                    };
                    if(dataset.update){
                        if(dataset.update.date && dataset.create.time){
                            document.getElementById('id_update_datetime').setAttribute('value',dataset.update.date+' '+dataset.create.time);
                        };
                        if(dataset.update.username){
                            document.getElementById('id_update_username').setAttribute('value',dataset.update.username);
                        };
                    };
                    if(dataset.keywords && document.getElementById("id_keywords")){
                        document.getElementById("id_keywords").innerHTML = dataset.keywords;
                    };
                    if(dataset.content && document.getElementById("id_content")){
                        document.getElementById("id_content").innerHTML = dataset.content.content;
                    };
                };
            },
        });
        
    });
}