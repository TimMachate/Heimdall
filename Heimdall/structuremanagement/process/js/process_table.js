function process_table(api_data_url,model) {
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
                        "render":function(data,type,row,meta){return '<a class="link-dark text-decoration-none" href="'+ row.url_detail +'">'+row.reference_number+'</a>'}
                    },
                    {
                        "name":"name",
                        "data":"name",
                        "defaultContent": "",
                        "className":"",
                        "visible": "name" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return '<a class="link-dark text-decoration-none" href="'+ row.url_detail +'">'+row.name+'</a>'}
                    },
                    {
                        "name":"duration_days",
                        "data":"duration_days",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "duration_days" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.duration_days}
                    },
                    {
                        "name":"duration_hours",
                        "data":"duration_hours",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "duration_hours" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.duration_hours}
                    },
                    {
                        "name":"duration_minutes",
                        "data":"duration_minutes",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "duration_minutes" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.duration_minutes}
                    },
                    {
                        "name":"duration_seconds",
                        "data":"duration_seconds",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "duration_seconds" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){return row.duration_seconds}
                    },
                    {
                        "name":"count_total",
                        "data":"count_total",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "count" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.count){
                                if(row.count.total){
                                    return row.count.total
                                };
                            };
                        }
                    },
                    {
                        "name":"count_average",
                        "data":"count_average",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "count" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.count){
                                if(row.count.average){
                                    return row.count.average + " %"
                                };
                            };
                        }
                    },
                    {
                        "name":"utilization",
                        "data":"utilization",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "utilization" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.utilization){
                                if(row.utilization.average){
                                    return row.utilization.average + " %"
                                };
                            };
                        }
                    },
                    {
                        "name":"processes_last",
                        "data":"processes_last",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "processes" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.processes){
                                if(row.processes.last){
                                    if(row.processes.last.begin.date && row.processes.last.begin.time){
                                        return '<a class="link-dark" href='+row.processes.last.url_detail+'>' + row.processes.last.begin.date + " " + row.processes.last.begin.time + "</a>"
                                    }
                                };
                            };
                        }
                    },
                    {
                        "name":"processes_next",
                        "data":"processes_next",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "processes" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.processes){
                                if(row.processes.next){
                                    if(row.processes.next.begin.date && row.processes.next.begin.time){
                                        return '<a class="link-dark" href='+row.processes.next.url_detail+'>' + row.processes.next.begin.date + " " + row.processes.next.begin.time + "</a>"
                                    }
                                };
                            };
                        }
                    },
                    {
                        "name":"picture",
                        "data":"picture",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "picture" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.picture != null){
                                return '<a class="btn btn-primary" href="'+ row.picture.url_file +'" target="_blank"><i class="fas fa-image"></i></a>'
                            } else {
                                return '-'
                            }                        
                        }
                    },
                    {
                        "name":"technical_data_sheet",
                        "data":"technical_data_sheet",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "technical_data_sheet" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.technical_data_sheet != null){
                                return '<a class="btn btn-primary" href="'+ row.technical_data_sheet.url_file +'" target="_blank"><i class="fas fa-file-pdf"></i></a>'
                            } else {
                                return '-'
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
                createTable(model,dataset,col,[[5,'asc']],print);
            },
        });
        
    });
}