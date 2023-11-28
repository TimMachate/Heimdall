function status_list(api_data_url,model) {
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
                        "name":"background_color",
                        "data":"background_color",
                        "defaultContent": "",
                        "className":"",
                        "visible": "background_color" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.background_color){
                                if(row.background_color.style && row.background_color.value){
                                    return '<div class="btn" '+row.background_color.style+'>&nbsp;&nbsp;</div>'
                                };
                            };
                        }
                    },
                    {
                        "name":"red",
                        "data":"red",
                        "defaultContent": "",
                        "className":"",
                        "visible": "background_color" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.background_color){
                                if(row.background_color.red){
                                    return row.background_color.red
                                }else{
                                    return 0
                                };
                            };
                        }
                    },
                    {
                        "name":"green",
                        "data":"green",
                        "defaultContent": "",
                        "className":"",
                        "visible": "background_color" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.background_color){
                                if(row.background_color.green){
                                    return row.background_color.green
                                }else{
                                    return 0
                                };
                            };
                        }
                    },
                    {
                        "name":"blue",
                        "data":"blue",
                        "defaultContent": "",
                        "className":"",
                        "visible": "background_color" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.background_color){
                                if(row.background_color.blue){
                                    return row.background_color.blue
                                }else{
                                    return 0
                                };
                            };
                        }
                    },
                    {
                        "name":"alpha",
                        "data":"alpha",
                        "defaultContent": "",
                        "className":"",
                        "visible": "background_color" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.background_color){
                                if(row.background_color.alpha){
                                    return row.background_color.alpha
                                }else{
                                    return 0
                                };
                            };
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
                createList(model,dataset,col,[[4,'asc']],print);
            },
        });
        
    });
}
