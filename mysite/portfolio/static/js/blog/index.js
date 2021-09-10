$( document ).ready(function() {
    $(".dropdown-trigger").dropdown({hover: true});
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('#password, #confirm_password').on('keyup', function () {
        if ($('#password').val() != $('#confirm_password').val()) {
            $('#message').html('Passwords doesn\'t match!').css('color', 'red');
        } else {
            $('#message').html('');

        }
      });
});