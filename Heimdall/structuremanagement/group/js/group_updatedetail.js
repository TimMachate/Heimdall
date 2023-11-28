function group_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset.reference_number){
                    document.getElementById("reference_number").innerHTML = dataset.reference_number
                };
                if(dataset.name){
                    document.getElementById("reference_number").setAttribute("value",dataset.name)
                };
                if(dataset.create.datetime_formated){
                    document.getElementById("create_datetime_formated").setAttribute("value",dataset.create.datetime_formated)
                };
                if(dataset.create.username){
                    document.getElementById("create_username").setAttribute("value",dataset.create.username)
                };
                if(dataset.update.datetime_formated){
                    document.getElementById("update_datetime_formated").setAttribute("value",dataset.update.datetime_formated)
                };
                if(dataset.update.username){
                    document.getElementById("update_username").setAttribute("value",dataset.update.username)
                };
                if(dataset.description){
                    document.getElementById("description").innerHTML = dataset.description
                };
                if(dataset.description){
                    document.getElementById("devices_count").innerHTML = dataset.devices_count + " Geräte"
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
                        "name":"reference_number",
                        "data":"reference_number",
                        "defaultContent": "",
                        "className":"",
                        "visible": "reference_number" in dataset.devices[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url_detail){
                                return '<a class="link-dark text-decoration-none" href="'+ row.url_detail +'">'+row.reference_number+'</a>'
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
                        "visible": "name" in dataset.devices[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url_detail){
                                return '<a class="link-dark text-decoration-none" href="'+ row.url_detail +'">'+row.name+'</a>'
                            } else {
                                return row.name
                            }
                        }
                    },
                ];
                transformTable("devices",dataset.devices,col,[[2,'asc']]);
            },
        });
        
    });
}