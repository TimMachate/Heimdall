function status_updatedetail(api_data_url){
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
                if(dataset.name && document.getElementById("id_name")){
                    document.getElementById("id_name").setAttribute("value",dataset.name);
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
                if(dataset.background_color){
                    if(document.getElementById("id_color")){
                        document.getElementById("id_color").setAttribute("style","background-color:rgba("+dataset.background_color.red+","+dataset.background_color.green+","+dataset.background_color.blue+","+dataset.background_color.alpha+")");
                    };
                    if(dataset.background_color.red && document.getElementById("id_red")){
                        document.getElementById("id_red").setAttribute("value",dataset.background_color.red);
                    };
                    if(dataset.background_color.green && document.getElementById("id_green")){
                        document.getElementById("id_green").setAttribute("value",dataset.background_color.green);
                    };
                    if(dataset.background_color.blue && document.getElementById("id_blue")){
                        document.getElementById("id_blue").setAttribute("value",dataset.background_color.blue);
                    };
                    if(dataset.background_color.alpha && document.getElementById("id_alpha")){
                        document.getElementById("id_alpha").setAttribute("value",dataset.background_color.alpha);
                    };
                };
                if(dataset.description && document.getElementById("id_description")){
                    document.getElementById("id_description").innerHTML = dataset.description;
                };
                if(dataset.stati_count){
                    document.getElementById("id_stati_count").innerHTML = dataset.stati_count
                };
                if(dataset.url){
                    if(dataset.url.data_create){
                        document.getElementById("id_url_data_create").setAttribute("href",dataset.url.data_create)
                    };
                    if(dataset.url.data_list){
                        document.getElementById("id_url_data_list").setAttribute("href",dataset.url.data_list)
                    };
                    if(dataset.url.data_table){
                        document.getElementById("id_url_data_table").setAttribute("href",dataset.url.data_table)
                    };
                };
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
                        "visible": "create" in dataset.stati[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.create){return row.create.date}}
                    },
                    {
                        "name":"create_time",
                        "data":"create_time",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset.stati[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.create){return row.create.time}}
                    },
                    {
                        "name":"device",
                        "data":"device",
                        "defaultContent": "",
                        "className":"",
                        "visible": "device" in dataset.stati[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.device){
                                return row.device.name
                            };
                        }
                    },
                    {
                        "name":"url",
                        "data":"url",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "url" in dataset.stati[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url){
                                if (row.url.detail){
                                    detail = '<a class="btn btn-primary" href="'+ row.url.detail +'"><i class="fas fa-search"></i></a>'
                                } else {detail = ""};
                                if (row.url.update){
                                    update = '<a class="btn btn-primary" href="'+ row.url.update +'"><i class="fas fa-pen"></i></a>'
                                } else {update = ""};
                                if (row.url.data_create){
                                    data_create = '<a class="btn btn-success" href="'+ row.url.data_create +'"><i class="fas fa-plus"></i></a>'
                                } else {data_create = ""};
                                if (row.url.delete){
                                    del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                } else {del = ""};
                                return '<div class="btn-group">'+detail+update+data_create+del+'</div>'
                            };
                        }
                    },
                ];
                let print = [];
                for (let i = 0; i < col.length; i++){
                    if (col[i]["visible"] === true) {print.push(i)};
                };
                transformTable("stati",dataset.stati,col,[[1,'desc']],print);
            },
        });
        
    });
}