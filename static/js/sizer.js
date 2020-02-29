

function determineTotalWidth() {
    let card = $('.card-container');
    let blockWidth = $('.card-block').width();
    let cardWidth = card.width();
    let cardCount = card.length;

    if(cardCount * cardWidth >= blockWidth) {
        $('.cart-total').css('width', blockWidth - 30);
    } else {
        $('.cart-total').css('width', (cardCount * cardWidth) - 30);
    }

    // if (cardTotal >= cols) {
    //     //cols is the # of cards to measure
    //     factor = cols;
    // } else if (cardTotal < cols){
    //     //cardTotal is the # of cards to measure
    //     factor = cardTotal;
    // }

    // alert(cardTotal + " " + cols + " " + card.width());

    // let displayRowWidth = card.width() * factor;
    //
    // $('.cart-total').css('width', displayRowWidth);
}

$(document).ready(function() {

    determineTotalWidth();





    $(window).resize(function(e) {
        determineTotalWidth()
    });
});

/* screen width 768 sm, 992 md, 1200 lg, */
