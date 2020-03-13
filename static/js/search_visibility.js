$(document).ready(function() {
    if (location.pathname !== '/search/') {
        $('#search').css('visibility', 'visible');
    } else {
        $('#search').css('visibility', 'hidden');
    }
});