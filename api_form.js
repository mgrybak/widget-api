$(document).ready(function(){
    $("#check-availability").click(function(){
        var user_name = $("#usr").val();
        var user_name_formatted = user_name.replace(/\s+/g, '-').toLowerCase();
        var url_call = "https://platform-api.findthebest.com:443/API/v1/publisher/exists?name=" + user_name_formatted
        $.ajax({
            async: true,
            url: "http://api.graphiq.com/timeseries-analysis/test",
            type: "GET",
            headers: {
                "token": "e6ba237f501f81b49fff3ceed9fec201",
                "cache-control": "no-cache",
                "Content-Type": "text/plain"
            }
        }).done(function (response) {
            alert(response);
        });
    });
});