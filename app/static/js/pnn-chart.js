$(function(){
    var pnn = $("#pnn").val();
    if(pnn != undefined){
        pnn = pnn.split(",");
        var pnnArray = [];
        var time = [];
        pnn.forEach(function(val, index, array){
            time.push(index * 10);
            pnnArray.push(parseFloat(val.replace("[","").replace("]","")));
        });
        console.info(pnnArray);
        var canvas = document.getElementById("chart");
        new Chart(canvas, {
            type: 'line',
            data: {
                labels: time,
                datasets:[{
                    label: "pnn",
                    data: pnnArray,
                    // borderColor: "rgba(255,0,0,1)",
                    // backgroundColor: "rgba(0,0,0,0)"
                }]
            },
            options:{
                title:{
                    text: "PNN-DATA",
                    display: true
                },
                scales: {
                    yAxes:[{
                        ticks:{
                            suggestedMax: 1,
                            suggestedMin: 0
                        }
                    }]
                }
            }
        })    
    }
});
