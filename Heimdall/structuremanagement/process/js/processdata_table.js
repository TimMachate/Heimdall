function processdata_table(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url.replace("=&amp;", '=&').replace("&amp;", '&'),
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
                        "name":"begin",
                        "data":"begin",
                        "defaultContent": "",
                        "className":"",
                        "visible": "begin" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.begin){return row.begin.date}}
                    },
                    {
                        "name":"begin",
                        "data":"begin",
                        "defaultContent": "",
                        "className":"",
                        "visible": "begin" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.begin){return row.begin.time}}
                    },
                    {
                        "name":"begin",
                        "data":"begin",
                        "defaultContent": "",
                        "className":"",
                        "visible": "begin" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.begin){
                            if (row.begin.url_detail){
                                return '<a class="link-dark" href="'+ row.begin.url_detail +'">'+row.begin.username+'</a>'
                            } else {
                                return row.begin.username
                            }
                        }}
                    },
                    {
                        "name":"duration_formated",
                        "data":"duration_formated",
                        "defaultContent": "",
                        "className":"",
                        "visible": "duration_formated" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.duration_formated){return row.duration_formated}}
                    },
                    {
                        "name":"end",
                        "data":"end",
                        "defaultContent": "",
                        "className":"",
                        "visible": "end" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.end){return row.end.date}}
                    },
                    {
                        "name":"end",
                        "data":"end",
                        "defaultContent": "",
                        "className":"",
                        "visible": "end" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.end){return row.end.time}}
                    },
                    {
                        "name":"end",
                        "data":"end",
                        "defaultContent": "",
                        "className":"",
                        "visible": "end" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.end){
                            if (row.end.url_detail){
                                return '<a class="link-dark" href="'+ row.end.url_detail +'">'+row.end.username+'</a>'
                            } else {
                                return row.end.username
                            }
                        }}
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
                        "name":"device",
                        "data":"device",
                        "defaultContent": "",
                        "className":"",
                        "visible": "device" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.device){
                                return '<a class="link-dark" href="'+ row.device.url_detail +'">'+row.device.name+'</a>'
                            } else {
                                return ''
                            }
                        }
                    },
                    {
                        "name":"process",
                        "data":"process",
                        "defaultContent": "",
                        "className":"",
                        "visible": "process" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.process){
                                return '<a class="link-dark" href="'+ row.process.url_detail +'">'+row.process.name+'</a>'
                            } else {
                                return ''
                            }
                        }
                    },
                    {
                        "name":"count",
                        "data":"count",
                        "defaultContent": "",
                        "className":"",
                        "visible": "count" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.count){
                                return row.count
                            } else {
                                return ''
                            }
                        }
                    },
                    {
                        "name":"utilization",
                        "data":"utilization",
                        "defaultContent": "",
                        "className":"",
                        "visible": "utilization" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.utilization){
                                return row.utilization.formated
                            } else {
                                return ''
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
