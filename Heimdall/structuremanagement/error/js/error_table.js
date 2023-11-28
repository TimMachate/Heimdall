function error_table(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
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
                        "name":"reference_number",
                        "data":"reference_number",
                        "defaultContent": "",
                        "className":"",
                        "visible": "reference_number" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url_detail){
                                return '<a class="link-dark" href="'+ row.url_detail +'">'+row.reference_number+'</a>'
                            } else {
                                return row.reference_number
                            }
                        }
                    },
                    {
                        "name":"name",
                        "data":"name",
                        "defaultContent": "",
                        "className":"",
                        "visible": "name" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url_detail){
                                return '<a class="link-dark" href="'+ row.url_detail +'">'+row.name+'</a>'
                            } else {
                                return row.name
                            }
                        }
                    },
                    {
                        "name":"description",
                        "data":"description",
                        "defaultContent": "",
                        "className":"",
                        "visible": "description" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.description}
                    },
                    {
                        "name":"error_last",
                        "data":"error_last",
                        "defaultContent": "",
                        "className":"",
                        "visible": "error_last" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.error_last){
                                if(row.error_last.create){
                                    if(row.error_last.create.date && row.error_last.create.time && row.error_last.url_detail){
                                        return '<a class="link-dark text-decoration-none" href="'+row.error_last.url_detail+'">'+row.error_last.create.date + " " + row.error_last.create.time+'</a>'
                                    } else if(row.error_last.create.date && row.error_last.create.time){
                                        return row.error_last.create.date + " " + row.error_last.create.time
                                    };
                                };
                            };
                        }
                    },
                    {
                        "name":"error_last",
                        "data":"error_last",
                        "defaultContent": "",
                        "className":"",
                        "visible": "error_last" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.error_last){
                                if(row.error_last.device){
                                    if(row.error_last.device.name && row.error_last.device.url_detail){
                                        return '<a class="link-dark text-decoration-none" href="'+row.error_last.device.url_detail+'">'+row.error_last.device.name+'</a>'
                                    } else if(row.error_last.device.name){
                                        return row.error_last.device.name
                                    };
                                };
                            };
                        }
                    },
                    {
                        "name":"errors_count",
                        "data":"errors_count",
                        "defaultContent": "",
                        "className":"",
                        "visible": "errors_count" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.errors_count}
                    },
                    {
                        "name":"create_date",
                        "data":"create_date",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.create){return row.create.date}}
                    },
                    {
                        "name":"create_time",
                        "data":"create_time",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.create){return row.create.time}}
                    },
                    {
                        "name":"create_username",
                        "data":"create_username",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.create){
                            if (row.create.url_detail){
                                return '<a class="link-dark" href="'+ row.create.url_detail +'">'+row.create.username+'</a>'
                            } else {
                                return row.create.username
                            }
                        }}
                    },
                    {
                        "name":"update_date",
                        "data":"update_date",
                        "defaultContent": "",
                        "className":"",
                        "visible": "update" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.update){return row.update.date}}
                    },
                    {
                        "name":"update_time",
                        "data":"update_time",
                        "defaultContent": "",
                        "className":"",
                        "visible": "update" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.update){return row.update.time}}
                    },
                    {
                        "name":"update_username",
                        "data":"update_username",
                        "defaultContent": "",
                        "className":"",
                        "visible": "update" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.update){
                            if (row.update.url_detail){
                                return '<a class="link-dark" href="'+ row.update.url_detail +'">'+row.update.username+'</a>'
                            } else {
                                return row.update.username
                            }
                        }}
                    },
                    {
                        "name":"url",
                        "data":"url",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "url" in dataset[0] ? true : false,
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
                createTable(model,dataset,col,[[1,'asc']],print);
            },
        });
        
    });
}
