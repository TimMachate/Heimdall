function variable_list(api_url,model) {
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
                            "name":"url_detail",
                            "data":"url_detail",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_detail" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'}
                        },
                        {
                            "name":"url_update",
                            "data":"url_update",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_update" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){return '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'}
                        },
                        {
                            "name":"url_delete",
                            "data":"url_delete",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url_delete" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){return '<a class="btn btn-danger" href="'+ row.url_delete +'"><i class="fas fa-trash"></i></a>'}
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
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createList(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}
