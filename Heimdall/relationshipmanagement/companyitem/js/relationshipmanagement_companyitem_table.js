function companyitem_table(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
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
                                if (row.reference_number){
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
                                if (row.name){
                                    return row.name
                                }
                            }
                        },
                        {
                            "name":"item_number",
                            "data":"item_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "item_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.item_number){
                                    return row.item_number
                                }
                            }
                        },
                        {
                            "name":"company",
                            "data":"company",
                            "defaultContent": "",
                            "className":"",
                            "visible": "company_name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.company_name && row.company_url_detail){
                                    return '<a class="link-dark text-decoration-none" href="'+row.company_url_detail+'">'+row.company_name+'</a>'
                                }else{
                                    return row.company_name
                                };
                            }
                        },
                        {
                            "name":"unit",
                            "data":"unit",
                            "defaultContent": "",
                            "className":"",
                            "visible": "unit" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.unit){return row.unit}}
                        },
                        {
                            "name":"price",
                            "data":"price",
                            "defaultContent": "",
                            "className":"",
                            "visible": "price" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if (row.price){return row.price+" €"}}
                        },
                        {
                            "name":"create_date",
                            "data":"create_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.create_date){return row.create_date};}
                        },
                        {
                            "name":"create_time",
                            "data":"create_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.create_time){return row.create_time};}
                        },
                        {
                            "name":"create_username",
                            "data":"create_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.create_username && row.create_username_url_detail){
                                    return '<a class="link-dark" href="'+ row.create_username_url_detail +'">'+row.create_username+'</a>'
                                } else {
                                    return row.create_username
                                };
                            }
                        },
                        {
                            "name":"update_date",
                            "data":"update_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_date" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.update_date){return row.update_date};}
                        },
                        {
                            "name":"update_time",
                            "data":"update_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_time" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.update_time){return row.update_time};}
                        },
                        {
                            "name":"update_username",
                            "data":"update_username",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update_username" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.update_username && row.update_username_url_detail){
                                    return '<a class="link-dark" href="'+ row.update_username_url_detail +'">'+row.update_username+'</a>'
                                } else {
                                    return row.update_username
                                }
                            }
                        },
                        {
                            "name":"url_request_create",
                            "data":"url_request_create",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_request_create" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_request_create){
                                    return '<a class="btn btn-success" href="'+ row.url_request_create +'"><i class="fas fa-envelope"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_detail",
                            "data":"url_detail",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_detail" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                    };
                            }
                        },
                        {
                            "name":"url_update",
                            "data":"url_update",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_update){
                                    return '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_delete",
                            "data":"url_delete",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_delete" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_delete){
                                    return '<a class="btn btn-danger" href="'+ row.url_delete + "?next=" + dataset.url_detail +'"><i class="fas fa-trash"></i></a>'
                                };
                            }
                        },
                        {
                            "name":"url_block",
                            "data":"url_block",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_block" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_detail){
                                    detail = '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                } else {detail = ""};
                                if (row.url_update){
                                    update = '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                } else {update = ""};
                                if (row.url_delete){
                                    del = '<a class="btn btn-danger" href="'+ row.url_delete +'"><i class="fas fa-trash"></i></a>'
                                } else {del = ""};
                                return '<div class="btn-group">'+detail+update+del+'</div>'
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createTable(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}
