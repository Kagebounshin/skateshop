$(document).ready(function () {
    // DOT HOVER FUNCTION
    $('.dot1').hover(
        function () {
            $('.dot-text').fadeIn('slow');
        },
        function () {
            $('.dot-text').fadeOut('slow')
        }
    );

    $('.dot2').hover(
        function () {
            $('.dot-text2').fadeIn('slow');
        },
        function () {
            $('.dot-text2').fadeOut('slow')
        }
    );
}); 