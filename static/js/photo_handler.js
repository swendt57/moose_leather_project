let photoWidth;
let photoHeight;

$(document).ready(function() {
    let photoDiv = $('.item-photo');
    setPhotoDimensions(photoDiv);

    $(window).resize(function(e) {
        setPhotoDimensions(photoDiv);
    });
});


function setPhotoDimensions(photoDiv) {
    photoWidth = photoDiv.parent().width() - 10;
    photoHeight = photoWidth * .75;
    photoDiv.css({'width': photoWidth, 'height': photoHeight});
}
