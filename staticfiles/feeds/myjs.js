$(document).ready(() => {
    $('.button-a').on('click', () => {
        $('.comment-toggle-a').hide();
        $('.comment-toggle-b').show();
    })
    $('.button-b').on('click', () => {
        $('.comment-toggle-b').hide();
        $('.comment-toggle-a').show();
    })
})