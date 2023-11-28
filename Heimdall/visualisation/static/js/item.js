function itemUpdate(id,url,value,minW,maxW,minV,maxV) {
        $.ajax({
        method: 'GET',
        url: url,
        dataType: "json",
        success: function(data){
            var elem = document.getElementById("item-"+id);
            var new_value = data[value]
            elem.innerHTML = new_value;
            if (minW != "None") {
                if (new_value<=minW){elem.style.backgroundColor = "yellow"}
            };
            if (maxW != "None") {
                if (new_value>=maxW){elem.style.backgroundColor = "yellow"}
            };
            if (minW != "None") {
                if (new_value<=minV){elem.style.backgroundColor = "red"}
            };
            if (maxW != "None") {
                if (new_value>=maxV){elem.style.backgroundColor = "red"}
            };
            },
        error: function(error_data){
            console.log('error');
            console.log(error_data);
        }
    });
};

function runItemUpdate(id,url,value,time,minW,maxW,minV,maxV){
    itemUpdate(id,url,value,minW,maxW,minV,maxV);
    if (time != "None"){
       setInterval(function(){
            itemUpdate(id,url,value,minW,maxW,minV,maxV)
        },Math.imul(parseInt(time),1000));
    };    
}