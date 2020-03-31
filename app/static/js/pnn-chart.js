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
        var canvas = document.getElementById("chart").getContext("2d");
        var chart = new Chart(canvas, {
            type: 'line',
            // data: {
            //     labels: time,
            //     datasets:[{
            //         label: "pnn",
            //         data: pnnArray,
            //         // borderColor: "rgba(255,0,0,1)",
            //         // backgroundColor: "rgba(0,0,0,0)"
            //     }]
            // },
            data: {
                datasets:[{
                    data:[]
                },{
                    data:[]
                }]
            },
            options:{
                title:{
                    text: "PNN-DATA",
                    display: true
                },
                scales: {
                    xAxes:[{
                        type: "realtime"
                    }],
                    yAxes:[{
                        ticks:{
                            suggestedMax: 1,
                            suggestedMin: 0
                        }
                    }]
                },
                plugins:{
                    streaming:{
                        duration: 20000,    
                        refresh: 1000,      
                        delay: 1000,        
                        frameRate: 30,      
                        pause: false,       
                        onRefresh: function(chart) {
                            console.info("onRefresh");
                            chart.data.datasets[0].data.push({
                                x: Date.now(),//ここに取得したデータの時間を入れる
                                y: Math.random()//ここに取得した値を入れる
                            });
                        }
                    }
                }
            }
        })    
    }
});
