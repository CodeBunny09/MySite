$( document ).ready(function() {
    //Misc
    $(".dropdown-trigger").dropdown({hover: true});
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.materialboxed').materialbox();
    $('.scrollspy').scrollSpy();
    $('.tabs').tabs();
    

    
    // SignUp
    $('#password, #confirm_password').on('keyup', function () {
        if ($('#password').val() != $('#confirm_password').val()) {
            $('#message').html('Passwords doesn\'t match!').css('color', 'red');
        } else {
            $('#message').html('');

        }
      });
    // Bookmark
    $('#bookmark').on('click', function() {
        if ($('#bookmark-icon').html() == 'bookmark_border') {
            $('#bookmark-icon').html('bookmark');
            $('#bookmark').attr('data-tooltip', "Remove Bookmark.");
            $('#bookmark').attr('onclick', "M.toast({html: 'Bookmark Removed!', classes: 'rounded'})");

        }
        else if ($('#bookmark-icon').html() == 'bookmark') {
            $('#bookmark-icon').html('bookmark_border');
            $('#bookmark').attr('data-tooltip', "Bookmark this post!!");
            $('#bookmark').attr('onclick', "M.toast({html: 'Bookmark Added!', classes: 'rounded'})");


        }
    });
    // Share
    $('#share').on('click', function () {
        let url = window.location.href;
        let share_message = "The url is coppied to your clipboard, you can now share it with your friends!"
        
        navigator.clipboard.writeText(url)
        .then(() => {M.toast({html: share_message, classes: 'rounded'});})
        .catch((e) => {console.log(`Copy Failed! ${e}`);})
    });
});