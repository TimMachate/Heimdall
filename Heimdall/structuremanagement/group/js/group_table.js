function group_table(api_data_url,model) {
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
                        "name":"url_detail",
                        "data":"url_detail",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "url_detail" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-info"></i></a>'}
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
                        "name":"devices_count",
                        "data":"devices_count",
                        "defaultContent": "",
                        "className":"",
                        "visible": "devices_count" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.devices_count}
                    },
                    {
                        "name":"devices",
                        "data":"devices",
                        "defaultContent": "",
                        "className":"",
                        "visible": "devices" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.devices){
                                let result = "";
                                row.devices.forEach(element => {
                                    result+='<a class="link-dark text-decoration-none" href="'+element.url_detail+'">'+element.name+' ('+element.reference_number+')</a><br>'
                                });
                                return result
                            } else {
                                return ""
                            }
                        }
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
