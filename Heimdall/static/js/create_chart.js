function drawDiagram(url,time) {
    $.ajax({
        method: 'GET',
        url: url,
        dataType: "json",
        success: function(data){
            var myChart = drawLayout(data, data.id);
            drawGraphs(data.graph, myChart);
            setInterval(function(){
                drawGraphs(data.graph, myChart);
            },time);
            console.log(myChart.data)
            console.log('Diagram '+'chart-'+data.id+' created successfully!');
        },
        error: function(error_data){
            console.log('error');
            console.log(error_data);
        }
    });
};

function drawLayout(data, id){
    var ctx = document.getElementById('chart-'+id);
    var myChart = new Chart(ctx, {
        data: {
            datasets:[],
        },
        options:{
            plugins: {
                title: {
                    display: data.title.titleDisplay,
                    text: data.title.titleText,
                    color: 'rgba('+data.title.titleRed+','+data.title.titleGreen+','+data.title.titleBlue+','+data.title.titleAlpha+')',
                    font: {
                        family: data.title.titleFontFamily,
                        size: data.title.titleFontSize,
                        weight: data.title.titleFontWeight,
                        lineHeight: data.title.titleFontLineHeight,
                    },
                    position: data.title.titlePosition,
                    align: data.title.titleAlign,
                    padding: {
                        top: data.title.titlePaddingTop,
                        bottom: data.title.titlePaddingBottom,
                    },
                },
                subtitle: {
                    display: data.subtitle.subtitleDisplay,
                    text: data.subtitle.subtitleText,
                    color: 'rgba('+data.subtitle.subtitleRed+','+data.subtitle.subtitleGreen+','+data.subtitle.subtitleBlue+','+data.subtitle.subtitleAlpha+')',
                    font: {
                        family: data.subtitle.subtitleFontFamily,
                        size: data.subtitle.subtitleFontSize,
                        weight: data.subtitle.subtitleFontWeight,
                        lineHeight: data.subtitle.subtitleFontLineHeight,
                    },
                    position: data.subtitle.subtitlePosition,
                    align: data.subtitle.subtitleAlign,
                    padding: {
                        top: data.subtitle.subtitlePaddingTop,
                        bottom: data.subtitle.subtitlePaddingBottom,
                    },
                },
                legend: {
                    display: data.legend.legendDisplay,
                    position: data.legend.legendPosition,
                    align: data.legend.legendAlign,
                },
            },
            scales: {
                x: {
                    type: 'category',
                    display: true,
                    title: {
                        display: true,
                        text: 'Wahlmöglichkeiten',
                    },
                    stacked: false, 
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Werte',
                    },
                    stacked: false,
                }
            },
        },
    });
    return myChart;
};

function drawGraphs(data, chart){
    var myChart = chart;
    myChart.data.labels = [];
    myChart.data.datasets = [];
    myChart.update();
    data.forEach(function(value, i){
        var graph = {};
        $.when(
            $.ajax({
                method: 'GET',
                url: value.graphURL,
                dataType: "json",
                success: function(data){
                    graph['data'] = data.results;                    
                },
                error: function(error_data){
                    console.log('error');
                    console.log(error_data);
                }
            })
        ).done(function(){
            graph['type'] = value.graphType;
            graph['label'] = value.graphLabel;
            graph['parsing'] = {xAxisKey: value.graphXData, yAxisKey: value.graphYData};
            graph['order'] = value.graphOrder;
            graph['backgroundColor'] = 'rgba('+value.graphBackgroundColorRed+','+value.graphBackgroundColorGreen+','+value.graphBackgroundColorBlue+','+value.graphBackgroundColorAlpha+')';
            graph['borderColor'] = 'rgba('+value.graphBorderColorRed+','+value.graphBorderColorGreen+','+value.graphBorderColorBlue+','+value.graphBorderColorAlpha+')';
            graph['borderWidth'] = value.graphBorderWidth;
            graph['pointStyle'] = value.graphPointStyle;
            graph['pointRadius'] = value.graphPointRadius;
            graph['pointBackgroundColor'] = 'rgba('+value.graphPointBackgroundColorRed+','+value.graphPointBackgroundColorGreen+','+value.graphPointBackgroundColorBlue+','+value.graphPointBackgroundColorAlpha+')';
            graph['pointBorderColor'] = 'rgba('+value.graphPointBorderColorRed+','+value.graphPointBorderColorGreen+','+value.graphPointBorderColorBlue+','+value.graphPointBorderColorAlpha+')';
            graph['pointBorderWidth'] = value.graphPointBorderWidth;
            graph['pointHitRadius'] = value.graphPointHitRadius;
            myChart.data.datasets.push(graph);
            myChart.update();
        });
    });
};