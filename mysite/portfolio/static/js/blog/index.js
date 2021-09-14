$( document ).ready(function() {
    //Generic
    $(".dropdown-trigger").dropdown({hover: true});
    $('.sidenav').sidenav();
    $('select').formSelect();
    
    // SignUp
    $('#password, #confirm_password').on('keyup', function () {
        if ($('#password').val() != $('#confirm_password').val()) {
            $('#message').html('Passwords doesn\'t match!').css('color', 'red');
        } else {
            $('#message').html('');

        }
      });
    // Bookmark
    function bookmarked_transition() {
        sl = $('#bookmark_transition').toggleClass('close');
        console.log(sl);
        setTimeout(function() {
        $('#bookmark_transition').toggleClass('close');
        console.log('Timer working! It\'s 2 seconds!');
        }, 2000);
    }
    $('#bookmark').on('click', function() {
        if ($('#bookmark-icon').html() == 'bookmark_border') {
            $('#bookmark-icon').html('bookmark');
            $('#bookmark_transition').html('<h4>Bookmark Added!</h4>');
            bookmarked_transition();
        }
        else if ($('#bookmark-icon').html() == 'bookmark') {
            $('#bookmark-icon').html('bookmark_border');
            $('#bookmark_transition').html('<h4>Bookmark Removed!</h4>');
            bookmarked_transition();
        }
    });
    // Share
    $('#share').on('click', function () {
        let url = window.location.href;
        share_message = "The url is coppied to your clipboard, you can now share it with your friends!"
        navigator.clipboard.writeText(url)
        .then(() => {console.log('Copied'); alert(share_message);})
        .catch((e) => {console.log(`Copy Failed! ${e}`)})
    });
});