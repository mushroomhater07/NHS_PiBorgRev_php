function submit1(text1){
    console.log("hi")
    //get value from id=current //document.getElementById("current").value 
    var formdata = 'mode=' + text1;

    window.alert(formdata);
    re1 =$.ajax({
        type: "POST",
        url: "run.php", //call storeemdata.php to store form data
        data: formdata,
        cache: false,
        complete: function (response) {
            console.log(response);
           // You will get response from your PHP page (what you echo or print)
        },
        error: function(jqXHR, textStatus, errorThrown) {
           console.log(textStatus, errorThrown);
        }
    });
// Callback handler that will be called regardless
// if the re1 failed or succeeded

    // Reenable the inputs
re1.done(function (){
    // Log a message to the console
    console.log("Hooray, it worked!");
});

// Callback handler that will be called on failure
re1.fail(function (){
    // Log the error to the console
    console.error("fail"
    );
});

// Callback handler that will be called regardless
// if the request failed or succeeded
re1.always(function () {
    // Reenable the inputs
    console.log("Halways");
});
   return false;
}