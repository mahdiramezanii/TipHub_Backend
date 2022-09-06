// This just toggles the follow/following of the button
$('a.follow').click(function () {
    $(this).toggleClass('followed');

    if($(this).hasClass('followed')) {
        $(this).text('Followed');
        $('ul li:last-child').html('325<span>Followers</span>');
    }
    else {
        $(this).text('Follow Nick');
        $('ul li:last-child').html('324<span>Followers</span>');
    }
});
