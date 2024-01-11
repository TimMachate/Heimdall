function supplieritem_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        // Supplier Item
                        if(element.name && document.getElementById("id_supplieritem-"+element.id)){
                            document.getElementById("id_supplieritem-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_supplieritem-"+element.id)){
                            document.getElementById("id_supplieritem-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Supplier Item Number
                        if(element.item_number && document.getElementById("id_item_number-"+element.id)){
                            document.getElementById("id_item_number-"+element.id).innerHTML = element.item_number;
                        };
                        if(element.url_detail && document.getElementById("id_item_number-"+element.id)){
                            document.getElementById("id_item_number-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Supplier
                        if(element.supplier_name && document.getElementById("id_supplier-"+element.id)){
                            document.getElementById("id_supplier-"+element.id).innerHTML = element.supplier_name;
                        };
                        if(element.supplier_url_detail && document.getElementById("id_supplier-"+element.id)){
                            document.getElementById("id_supplier-"+element.id).setAttribute("href",element.supplier_url_detail);
                        };
                        // Stock Value
                        if(element.stock_value && document.getElementById("id_stock_value-"+element.id)){
                            document.getElementById("id_stock_value-"+element.id).innerHTML = element.stock_value;
                        };
                        // Stock Count
                        if(element.stock_count && document.getElementById("id_stock_count-"+element.id)){
                            document.getElementById("id_stock_count-"+element.id).innerHTML = element.stock_count;
                        };
                        
                    });
                };
            },
        });
        
    });
}
