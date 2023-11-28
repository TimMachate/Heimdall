function protocol_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.url){
                        if(dataset.url.file && document.getElementById("id_url_file")){
                            console.log(dataset.url.file)
                            document.getElementById("id_url_file").setAttribute("href",dataset.url.file);
                        };
                    };
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.file){
                        if(dataset.file.name && document.getElementById("id_name")){
                            document.getElementById("id_name").setAttribute("value",dataset.file.name);
                        };
                        if(dataset.file.url && document.getElementById("id_url_detail")){
                            document.getElementById("id_url_detail").setAttribute("href",dataset.file.url.detail);
                        };
                    };
                    if(dataset.type && document.getElementById("id_type")){
                        document.getElementById("id_type").setAttribute("value",dataset.type);
                    };
                    if(dataset.version && document.getElementById("id_version")){
                        document.getElementById("id_version").setAttribute("value",dataset.version);
                    };
                    if(dataset.version_suffix && document.getElementById("id_version_suffix")){
                        document.getElementById("id_version_suffix").innerHTML = "-"+dataset.version_suffix;
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
                    if(dataset.keywords && document.getElementById("id_keywords")){
                        document.getElementById("id_keywords").innerHTML = dataset.keywords;
                    };
                    if(dataset.topic && document.getElementById("id_topic")){
                        document.getElementById("id_topic").innerHTML = dataset.topic;
                    };
                    if(dataset.procedure && document.getElementById("id_procedure")){
                        document.getElementById("id_procedure").innerHTML = dataset.procedure;
                    };
                    if(dataset.protocol && document.getElementById("id_protocol")){
                        document.getElementById("id_protocol").checked = true;
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
                                    if(v.unit && document.getElementById("id_unit-"+element.id+'-'+v.id)){
                                        document.getElementById("id_unit-"+element.id+'-'+v.id).innerHTML = v.unit
                                    };
                                });
                            };
                        });
                    };
                    if(dataset.data && document.getElementById("protocoldata")){
                        let col = [
                            {
                                "name":"id",
                                "data":"",
                                "defaultContent": "",
                                "width":"10px",
                                "className":"",
                                "visible":true,
                            },
                            {
                                "name":"create_date",
                                "data":"create_date",
                                "defaultContent": "",
                                "className":"",
                                "visible": "create" in dataset.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if(row.create){
                                        return row.create.date
                                    }else{
                                        return '-'
                                    };
                                }
                            },
                            {
                                "name":"create_time",
                                "data":"create_time",
                                "defaultContent": "",
                                "className":"",
                                "visible": "create" in dataset.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if(row.create){
                                        return row.create.time
                                    }else{
                                        return '-'
                                    };
                                }
                            },

                            {
                                "name":"version",
                                "data":"version",
                                "defaultContent": "",
                                "className":"",
                                "visible": "version" in dataset.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if(row.version){
                                        return row.version
                                    }else{
                                        return '-'
                                    };
                                }
                            },
                            {
                                "name":"file",
                                "data":"file",
                                "defaultContent": "",
                                "className":"",
                                "visible": "file" in dataset.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if(row.file){
                                        return '<a class="btn btn-primary" href="'+ row.file +'" target="_blank"><i class="fas fa-file-pdf"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url",
                                "data":"url",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url" in dataset.data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url){
                                        if (row.url.detail){
                                            detail = '<a class="btn btn-primary" href="'+ row.url.detail +'"><i class="fas fa-search"></i></a>'
                                        } else {detail = ""};
                                        if (row.url.update){
                                            update = '<a class="btn btn-primary" href="'+ row.url.update +'"><i class="fas fa-pen"></i></a>'
                                        } else {update = ""};
                                        if (row.url.delete){
                                            del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                        } else {del = ""};
                                        return '<div class="btn-group">'+detail+update+del+'</div>'
                                    };
                                }
                            },
                        ];
                        let print = [];
                        for (let i = 0; i < col.length; i++){
                            if (col[i]["visible"] === true) {print.push(i)};
                        };
                        createList("protocoldata",dataset.data,col,[[1,'desc']],print);
                    };
                };
            },
        });
        
    });
}