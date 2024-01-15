function requestdata_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    // Storage Item
                    if(dataset.storageitem_name && document.getElementById('id_storageitem')){
                        document.getElementById('id_storageitem').setAttribute('value',dataset.storageitem_name);
                    };
                    if(dataset.storageitem_url_detail && document.getElementById('id_storageitem_url_detail')){
                        document.getElementById('id_storageitem_url_detail').setAttribute('href',dataset.storageitem_url_detail);
                    };
                    // Supplier Item
                    if(dataset.supplieritem_name && document.getElementById('id_supplieritem')){
                        document.getElementById('id_supplieritem').setAttribute('value',dataset.supplieritem_name);
                    };
                    if(dataset.supplieritem_url_detail && document.getElementById('id_supplieritem_url_detail')){
                        document.getElementById('id_supplieritem_url_detail').setAttribute('href',dataset.supplieritem_url_detail);
                    };
                    // Create
                    if(dataset.create_date && dataset.create_time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create_date+' '+dataset.create_time);
                    };
                    if(dataset.create_username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create_username);
                    };
                    // Update
                    if(dataset.update_date && dataset.create_time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update_date+' '+dataset.update_time);
                    };
                    if(dataset.update_username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update_username);
                    };
                    // Authorized
                    if(dataset.authorized == true && document.getElementById('id_authorize')){
                        document.getElementById('id_authorize').setAttribute("class","input-group-text btn btn-success disabled");
                        document.getElementById('id_authorize').innerHTML='<i class="fas fa-check"></i>';
                    } else if (dataset.authorized == false && document.getElementById('id_authorize')){
                        document.getElementById('id_authorize').setAttribute("class","input-group-text btn btn-danger disabled");
                        document.getElementById('id_authorize').innerHTML='<i class="fas fa-times"></i>';
                    };
                    if(dataset.url_authorize_true && document.getElementById('id_url_authorize_true')){
                        document.getElementById('id_url_authorize_true').setAttribute("href",dataset.url_authorize_true);

                    };
                    if(dataset.url_authorize_false && document.getElementById('id_url_authorize_false')){
                        document.getElementById('id_url_authorize_false').setAttribute("href",dataset.url_authorize_false);
                        
                    };
                    if(dataset.authorized_date && dataset.authorized_time && document.getElementById('id_authorized_datetime')){
                        document.getElementById('id_authorized_datetime').setAttribute('value',dataset.authorized_date+' '+dataset.authorized_time);
                    };
                    if(dataset.authorized_username && document.getElementById('id_authorized_username')){
                        document.getElementById('id_authorized_username').setAttribute('value',dataset.authorized_username);
                    };
                    // Supplier
                    if(dataset.supplier_name && document.getElementById('id_supplier')){
                        document.getElementById('id_supplier').setAttribute('value',dataset.supplier_name);
                    };
                    if(dataset.supplier_url_detail && document.getElementById('id_supplier_url_detail')){
                        document.getElementById('id_supplier_url_detail').setAttribute('href',dataset.supplier_url_detail);
                    };
                    // Supplier Item
                    if(dataset.supplieritem_name && document.getElementById('id_supplieritem_standard')){
                        document.getElementById('id_supplieritem_standard').setAttribute('value',dataset.supplieritem_name);
                    };
                    if(dataset.supplieritem_url_detail && document.getElementById('id_supplieritem_standard_url_detail')){
                        document.getElementById('id_supplieritem_standard_url_detail').setAttribute('href',dataset.supplieritem_url_detail);
                    };
                    // Amount
                    if(dataset.amount && document.getElementById("id_amount")){
                        document.getElementById("id_amount").setAttribute('value',dataset.amount);
                    };
                    if(dataset.unit && document.getElementById("id_unit")){
                        document.getElementById("id_unit").innerHTML=dataset.unit;
                    };
                    if(dataset.price && dataset.unit && document.getElementById("id_price")){
                        document.getElementById("id_price").setAttribute('value',dataset.price + " € / " + dataset.unit);
                    } else if(dataset.price && document.getElementById("id_price")){
                        document.getElementById("id_price").setAttribute('value',dataset.price + " €");
                    };
                    if(dataset.value && document.getElementById("id_value")){
                        document.getElementById("id_value").setAttribute('value',dataset.value + " €");
                    };
                };
            },
        });
        
    });
}
