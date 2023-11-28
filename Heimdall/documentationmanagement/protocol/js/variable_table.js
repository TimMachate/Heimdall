function variable_table(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replace("=&amp;", '=&').replace("&amp;", '&'),
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
                                if(row.reference_number){
                                    return row.reference_number
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"name",
                            "data":"name",
                            "defaultContent": "",
                            "className":"",
                            "visible": "name" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.name){
                                    return row.name
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"symbol",
                            "data":"symbol",
                            "defaultContent": "",
                            "className":"",
                            "visible": "symbol" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.symbol){
                                    return row.symbol
                                }else{
                                    return '-'
                                };
                            }
                        },

                        {
                            "name":"unit",
                            "data":"unit",
                            "defaultContent": "",
                            "className":"",
                            "visible": "unit" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.unit){
                                    return row.unit
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"input_type",
                            "data":"input_type",
                            "defaultContent": "",
                            "className":"",
                            "visible": "input_type" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.input_type){
                                    return row.input_type
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"create_date",
                            "data":"create_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "create" in dataset[0] ? true : false,
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
                            "visible": "create" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.create){
                                    return row.create.time
                                }else{
                                    return '-'
                                };
                            }
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
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"update_date",
                            "data":"update_date",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.update){
                                    return row.update.date
                                }else{
                                    return '-'
                                };
                            }
                        },
                        {
                            "name":"update_time",
                            "data":"update_time",
                            "defaultContent": "",
                            "className":"",
                            "visible": "update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.update){
                                    return row.update.time
                                }else{
                                    return '-'
                                };
                            }
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
                                }else{
                                    return '-'
                                };
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
