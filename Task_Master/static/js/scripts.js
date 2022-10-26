
$("form[name=signin_form").submit(function(event) {

    var $form = $(this);

    var $error = $form.find(".error");

    var data = $form.serialize();

    $.ajax({
                url: "/user/signin_action/",
                type: "POST",
                data: data,
                dataType: "json",
                success: () => { window.location.href = "/tasks/user/dashboard/"; },
                erorr: (response) => { $error.text(response.responseJSON.error).removeClass("error--hidden"); }
           });

    event.preventDefault();

});


$("form[name=signup_form").submit(function(event) {

    var $form = $(this);

    var $error = $form.find(".error");

    var data = $form.serialize();

    $.ajax({
                url: "/user/signup_action/",
                type: "POST",
                data: data,
                dataType: "json",
                success: () => {  window.location.href = "/tasks/user/dashboard/"; },
                error: (response) => { $error.text(response.responseJSON.error).removeClass("error--hidden"); console.log(response)}

           });

    event.preventDefault();

});
