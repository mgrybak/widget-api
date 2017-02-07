$(document).ready(function(){

    $("#check-availability").click(function(){
        var user_name = $("#usr").val();
        checkAvailability(function( returnValue ){
            handleCheck(returnValue, user_name);
        });
    });

    $("#submit-button").click(function(){
        var user_name = $("#usr").val();
        checkAvailability(function( returnValue ){
            handleSubmit(returnValue, user_name);
        });
    });

});


function checkAvailability(callback_check){
    var user_name = $("#usr").val();
    var user_name_formatted = user_name.replace(/\s+/g, '-').toLowerCase();
    var url_call = "https://platform-api.findthebest.com:443/API/v1/publisher/exists?name=" + user_name_formatted
    $.post( "check_user.php", { url: url_call} )
        .done(callback_check);
}


function handleCheck(data, user_name){
    obj = JSON.parse(data);
    if (user_name == ""){
        alert("Please enter an organization name");
        return;
    }else if (user_name.length > 25){
        alert("Please keep organization name under 25 characters");
        return;
    }else if (obj.exists == true){
        alert("The name " + user_name + " is already taken.");
        return;
    }else if (obj.exists == false){
        alert("The name " + user_name + " is available.");
        return;
    }
}


function handleSubmit(data, user_name){
    obj = JSON.parse(data);
    if (user_name == ""){
        alert("Please enter an organization name");
        return;
    }else if (user_name.length > 25){
        alert("Please keep organization name under 25 characters");
        return;
    }else if (obj.exists == true){
        alert("The name " + user_name + " is already taken.");
        return;
    }

    // Storing Field Values In Variables
    var org_name = document.getElementById("usr").value;
    var domain = document.getElementById("url").value;
    var custom = document.getElementById("custom_form").value;
    var gmaps = document.getElementById("gmaps").value;
    var email = document.getElementById("email").value;
    var color = document.getElementById("hex").value;

    if ($("#location").is(":checked")){
        var location = true;
    }else{
        var location = false;
    }

    if ($("#property").is(":checked")){
        var property = true;
    }else{
        var property = false;
    }

    if ($("#market").is(":checked")){
        var market = true;
    }else{
        var market = false;
    }

    if ($("#title").is(":checked")){
        var title = true;
    }else{
        var title = false;
    }

    if ($("#native").is(":checked")){
        var native_integration = true;
    }else{
        var native_integration = false;
    }

    if ($("#footer").is(":checked")){
        var footer = true;
    }else{
        var footer = false;
    }

    if ($("#sources").is(":checked")){
        var sources = true;
    }else{
        var sources = false;
    }

    if ($("#share").is(":checked")){
        var share = true;
    }else{
        var share = false;
    }


    //Check that email is properly formatted
    var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    
    //Verify that domain is not blank
    if (domain == "") {
        alert("Please enter a valid domain");
        return;
    }

    //Choose package
    var package_option = "";
    if (location == false && property == false && market == false && custom == "") {
        alert("Please choose a visualization package");
        return;
    }

    if(location == true){
        package_option = package_option + "location";
    }

    if(property == true){
        package_option = package_option + "^property";
    }

    if(market == true){
        package_option = package_option + "^market";
    }

    if(custom != ""){
        package_option = package_option + "^" + custom;
    }

    // Conditions
    if(!email.match(emailReg)) {
        alert("Please input a valid e-mail address");
        return;
    }else if(color.length > 0 && (color.length != 7 || color.charAt(0) != "#")) {
        alert("Please input a property formatted hex code");
        return;
    }else{
        submitForm(org_name,domain,email,color,package_option,title,native_integration,footer,sources,share,gmaps);
    }
}


function submitForm(org_name,domain,email,color,package_option,title,native_integration,footer,sources,share,gmaps){
    $.post( "register_user.php", { org_name: org_name,domain: domain,email: email,color: color,package_option: package_option,title: title,native_integration: native_integration,footer: footer,sources: sources,share: share,google_maps_api_key: gmaps} )
        .done(function (response) {
            submission = JSON.parse(response);
            if (submission.status = "SCHEDULED"){
                alert("Thank you, your request for a Graphiq API key has been submitted.");
            }
            else {
                alert("There was an error processing your request. Please contact Graphiq.")
            }
            window.location.reload(1)
        });
}