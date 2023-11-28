function customer_updatedetail(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.type && document.getElementById("id_type")){
                        document.getElementById("id_type").setAttribute("value",dataset.type);
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
                    if(dataset.street && document.getElementById("id_street")){
                        document.getElementById("id_street").setAttribute("value",dataset.street);
                    };
                    if(dataset.house_number && document.getElementById("id_house_number")){
                        document.getElementById("id_house_number").setAttribute("value",dataset.house_number);
                    };
                    if(dataset.post_code && document.getElementById("id_post_code")){
                        document.getElementById("id_post_code").setAttribute("value",dataset.post_code);
                    };
                    if(dataset.city && document.getElementById("id_city")){
                        document.getElementById("id_city").setAttribute("value",dataset.city);
                    };
                    if(dataset.country && document.getElementById("id_country")){
                        document.getElementById("id_country").setAttribute("value",dataset.country);
                    };
                    if(dataset.telephones){
                        if(dataset.telephones.count && document.getElementById("id_telephone_count")){
                            document.getElementById("id_telephone_count").innerHTML=dataset.telephones.count;
                        };
                    };
                    if (dataset.telephones){
                        if (dataset.telephones.data){
                            dataset.telephones.data.forEach(element => {
                                if(element.type && document.getElementById("id_telephone_type-"+element.id)){
                                    if (element.type == "Telefon"){
                                        document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-phone"></i>';
                                    } else if(element.type == "Handy"){
                                        document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-mobile"></i>';
                                    } else if(element.type == "Fax"){
                                        document.getElementById("id_telephone_type-"+element.id).innerHTML='<i class="fas fa-fax"></i>';
                                    };
                                };
                                if(element.number && document.getElementById("id_telephone_number-"+element.id)){
                                    document.getElementById("id_telephone_number-"+element.id).setAttribute("value",element.number);
                                };
                                if(element.target && document.getElementById("id_telephone_target-"+element.id)){
                                    document.getElementById("id_telephone_target-"+element.id).setAttribute("value",element.target);
                                };
                            });
                        };
                    };
                    if(dataset.emails){
                        if(dataset.emails.count && document.getElementById("id_email_count")){
                            document.getElementById("id_email_count").innerHTML=dataset.emails.count;
                        };
                    };
                    if (dataset.emails){
                        if (dataset.emails.data){
                            dataset.emails.data.forEach(element => {
                                if(element.email && document.getElementById("id_email_email-"+element.id)){
                                    document.getElementById("id_email_email-"+element.id).setAttribute("value",element.email);
                                };
                                if(element.target && document.getElementById("id_email_target-"+element.id)){
                                    document.getElementById("id_email_target-"+element.id).setAttribute("value",element.target);
                                };
                            });
                        };                     
                    };
                    if(dataset.customer && document.getElementById("id_customer")){
                        document.getElementById("id_customer").setAttribute("checked",true)
                    };
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML=dataset.notice;
                    };
                    if(dataset.persons){
                        if(dataset.persons.count && document.getElementById("id_persons_count")){
                            document.getElementById("id_persons_count").innerHTML = dataset.persons.count
                        };
                        if(dataset.persons.data){
                            let persons = [
                                {
                                    "name":"id",
                                    "data":"",
                                    "defaultContent": "",
                                    "width":"10px",
                                    "className":"",
                                    "visible":true,
                                },
                                {
                                    "name":"last_name",
                                    "data":"last_name",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "last_name" in dataset.persons.data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.last_name){
                                            return row.last_name
                                        };
                                    }
                                },
                                {
                                    "name":"first_name",
                                    "data":"first_name",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "first_name" in dataset.persons.data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.first_name){
                                            return row.first_name
                                        };
                                    }
                                },
                                {
                                    "name":"telephones",
                                    "data":"telephones",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "telephones" in dataset.persons.data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.telephones){
                                            if(row.telephones.data){
                                                string = ""
                                                row.telephones.data.forEach(element => {
                                                    string+='<div>'+element.number+'</div>'
                                                });
                                                return string
                                            };
                                        }
                                    }
                                },
                                {
                                    "name":"emails",
                                    "data":"emails",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "emails" in dataset.persons.data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.emails){
                                            if(row.emails.data){
                                                string = ""
                                                row.emails.data.forEach(element => {
                                                    string+='<div>'+element.email+'</div>'
                                                });
                                                return string
                                            };
                                        }
                                    }
                                },
                                {
                                    "name":"url",
                                    "data":"url",
                                    "defaultContent": "",
                                    "width":"35px",
                                    "className":"",
                                    "visible": "url" in dataset.persons.data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.url){
                                            if (row.url.detail){
                                                detail = '<a class="btn btn-primary" href="'+ row.url.detail +'"><i class="fas fa-search"></i></a>'
                                            } else {detail = ""};
                                            if (row.url.update){
                                                update = '<a class="btn btn-primary" href="'+ row.url.update +'"><i class="fas fa-pen"></i></a>'
                                            } else {update = ""};
                                            if (row.url.delete){
                                                del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                            } else {del = ""};
                                            return '<div class="btn-group">'+detail+update+del+'</div>'
                                        };
                                    }
                                },
                            ];
                            let print = [];
                            for (let i = 0; i < persons.length; i++){
                                if (persons[i]["visible"] === true) {print.push(i)};
                            };
                            transformTable("id_persons",dataset.persons.data,persons,[[1,'asc']],print);
                        };
                    };
                };
            },
        });
        
    });
}
