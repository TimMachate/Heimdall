function programm_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    dataset.forEach(element => {
                        console.log(element)
                        // Programm Item
                        if(element.name && document.getElementById("id_programm-"+element.id)){
                            document.getElementById("id_programm-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail && document.getElementById("id_programm-"+element.id)){
                            document.getElementById("id_programm-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Description
                        if(element.description && document.getElementById("id_description-"+element.id)){
                            document.getElementById("id_description-"+element.id).innerHTML = element.description;
                        };
                    });
                };
            },
        });
        
    });
}
