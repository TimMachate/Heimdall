function drawDiagram(url,time) {
    $.ajax({
        method: 'GET',
        url: url,
        dataType: "json",
        success: function(data){
            var myChart = drawLayout(data, data.id);
            drawGraphs(data.data, myChart);
            setInterval(function(){
                drawGraphs(data.data, myChart);
            },Math.imul(parseInt(time),1000));
            //console.log(myChart.data)
            //console.log('Diagram '+'chart-'+data.id+' created successfully!');
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
                    display: data.titleDisplay,
                    text: data.titleText,
                    color: 'rgba('+data.titleRed+','+data.titleGreen+','+data.titleBlue+','+data.titleAlpha+')',
                    font: {
                        family: data.titleFontFamily,
                        size: data.titleFontSize,
                        weight: data.titleFontWeight,
                        lineHeight: data.titleFontLineHeight,
                    },
                    position: data.titlePosition,
                    align: data.titleAlign,
                    padding: {
                        top: data.titlePaddingTop,
                        bottom: data.titlePaddingBottom,
                    },
                },
                subtitle: {
                    display: data.subtitleDisplay,
                    text: data.subtitleText,
                    color: 'rgba('+data.subtitleRed+','+data.subtitleGreen+','+data.subtitleBlue+','+data.subtitleAlpha+')',
                    font: {
                        family: data.subtitleFontFamily,
                        size: data.subtitleFontSize,
                        weight: data.subtitleFontWeight,
                        lineHeight: data.subtitleFontLineHeight,
                    },
                    position: data.subtitlePosition,
                    align: data.subtitleAlign,
                    padding: {
                        top: data.subtitlePaddingTop,
                        bottom: data.subtitlePaddingBottom,
                    },
                },
                legend: {
                    display: data.legendDisplay,
                    position: data.legendPosition,
                    align: data.legendAlign,
                },
            },
            scales: {
                mhm: {
                    type: 'category',
                    position: 'top',
                    display: true,
                    title: {
                        display: true,
                        text: 'Wahlmöglichkeiten',
                        align: 'center',
                        font: {
                            family: 'Arial',
                            size: '12',
                            weight: 'normal',
                            lineHeight: '1.2',
                        },
                        color: 'rgba('+0+','+0+','+255+','+1+')',
                        padding: {
                            top: 10,
                            bottom: 10,
                        },
                    },
                    stacked: false, 
                },
                legga: {
                    type: 'linear',
                    position: 'right',
                    display: true,
                    title: {
                        type: 'line',
                        display: true,
                        text: 'Werte',
                        align: 'center',
                        font: {
                            family: 'Arial',
                            size: '12',
                            weight: 'normal',
                            lineHeight: '1.2',
                        },
                        color: 'rgba('+0+','+255+','+0+','+1+')',
                        padding: {
                            top: 10,
                            bottom: 10,
                        },
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