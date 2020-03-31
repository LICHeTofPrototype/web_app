$(function(){
    // var pnn = $("#pnn").val();
    // if(pnn != undefined){
    //     pnn = pnn.split(",");
    //     var pnnArray = [];
    //     var time = [];
    //     pnn.forEach(function(val, index, array){
    //         time.push(index * 10);
    //         pnnArray.push(parseFloat(val.replace("[","").replace("]","")));
    //     });
    // }
    var count = 0;
    var canvas = document.getElementById("chart").getContext("2d");
    var chart = new Chart(canvas, {
        type: 'line',
        data: {
            datasets:[{
                label:"pnn",
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
                    type: "realtime",
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 15 //値の最大表示数
                    }
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
                    delay: 2000,        
                    frameRate: 30,      
                    pause: false,       
                    onRefresh: function(chart) {
                        getData().then(response =>{
                            var pnn = response[count] == undefined ? 0 : response[count].pnn_data
                            // TODO 表示時間の指定
                            chart.data.datasets[0].data.push({
                                x: Date.now(),//ここに取得したデータの時間を入れる
                                y: pnn//ここに取得した値を入れる
                            });
                            count++;
                        }).catch(error =>{
                            count++;
                            console.info(error);
                            return error;
                        });
                    }
                }
            }
        }
    })    

});

// TODO 現時点では連続して取得する対象のデータを判断できない
function getData(request_index){
    var body = {
        measurement_id: 13,
        request_index: 0
    };
    const url = '/v1/api/get_data/pnn/';
    return fetch(url, {
        method: "post",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    }).then(function(response){
        return response.json();
    });
}

function getCookie(name) {
    var result = null;
    var cookieName = name + '=';
    var allcookies = document.cookie;
    var position = allcookies.indexOf( cookieName );
    if( position != -1 ) {
      var startIndex = position + cookieName.length;
      var endIndex = allcookies.indexOf( ';', startIndex );
      if( endIndex == -1 ) {
        endIndex = allcookies.length;
      }
      result = decodeURIComponent(allcookies.substring( startIndex, endIndex ));
    }
    return result;
}