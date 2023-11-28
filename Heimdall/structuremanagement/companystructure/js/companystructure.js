function companystructure(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url,
            success: function(dataset){
                dataset.forEach(element => {
                    if (element["url_detail"] != null ) {
                        let link_create = document.createElement('a');
                        link_create.setAttribute('href',element["url_detail"]);
                        link_create.setAttribute('class',"link-dark text-decoration-none");
                        link_create.innerHTML = element["name"]+" ("+element["reference_number"]+")"
                        document.getElementById("card-title-"+element["id"]).appendChild(link_create);
                    } else {
                        document.getElementById("card-title-"+element["id"]).innerHTML = "-"
                    };
                    let link_create = document.getElementById("card-image-"+element["id"]);
                    link_create.setAttribute("src",element["image_file_url"]);
                    if (element["responsible_url_detail"] != null ) {
                        let link_create = document.createElement('a');
                        link_create.setAttribute('href',element["responsible_url_detail"]);
                        link_create.setAttribute('class',"link-dark text-decoration-none");
                        link_create.innerHTML = element["responsible_name"];
                        document.getElementById("responsible-"+element["id"]).appendChild(link_create);
                    } else {
                        document.getElementById("responsible-"+element["id"]).innerHTML = "-"
                    };
                    if (element["responsible_telephone"] != null ) {
                        document.getElementById("responsible-telephone-"+element["id"]).innerHTML = element["responsible_telephone"];
                    } else {
                        document.getElementById("responsible-telephone-"+element["id"]).innerHTML = "-";
                    };
                    if (element["responsible_email"] != null ) {
                        document.getElementById("responsible-email-"+element["id"]).innerHTML = element["responsible_email"];
                    } else {
                        document.getElementById("responsible-email-"+element["id"]).innerHTML = "-";
                    };
                    if (element["substitute_url_detail"] != null ) {
                        let link_create = document.createElement('a');
                        link_create.setAttribute('href',element["substitute_url_detail"]);
                        link_create.setAttribute('class',"link-dark text-decoration-none");
                        link_create.innerHTML = element["substitute_name"];
                        document.getElementById("substitute-"+element["id"]).appendChild(link_create);
                    } else {
                        document.getElementById("substitute-"+element["id"]).innerHTML = "-"
                    };
                    if (element["substitute_telephone"] != null ) {
                        document.getElementById("substitute-telephone-"+element["id"]).innerHTML = element["substitute_telephone"];
                    } else {
                        document.getElementById("substitute-telephone-"+element["id"]).innerHTML = "-";
                    };
                    if (element["substitute_email"] != null ) {
                        document.getElementById("substitute-email-"+element["id"]).innerHTML = element["substitute_email"];
                    } else {
                        document.getElementById("substitute-email-"+element["id"]).innerHTML = "-";
                    };
                });
            },
        });
    });
}