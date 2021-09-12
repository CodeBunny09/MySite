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
        $('#bookmark_transition').removeAttr('hidden')
        setTimeout(function() {
        $('#bookmark_transition').attr('hidden', 'true')
        console.log('Timer working! It\'s 2 seconds!')
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
    function copyToClipboard(url) {
        var $temp = $("<input hidden id='url'>");
        $("body").append($temp);
        $temp.html(url)

        var text = $("#url").get(0)
        var selection = window.getSelection();
        var range = document.createRange();
        range.selectNodeContents(text);
        selection.removeAllRanges();
        selection.addRange(range);
        //add to clipboard.
        window.execCommand('copy');
    }
    $('#share').on('click', function () {
        let url = window.location.href;
        copyToClipboard(url);
    });
});