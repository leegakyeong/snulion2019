$(document).ready(() => {
    $('.button-a').on('click', () => {
        $('.comment-toggle-a').hide();
        $('.comment-toggle-b').show();
    })
    $('.button-b').on('click', () => {
        $('.comment-toggle-b').hide();
        $('.comment-toggle-a').show();
    })
    $('.comment-submit').on('click', event => {

        var pk = 1;
        event.preventDefault();
        alert(pk);
        $.ajax({
            type: 'POST',
            url: '/feeds/'+pk+'/comments/',
            data: {
                'content': $('#comment-content'+pk+">input[type=text]").val(),
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            dataType: 'json',
            success: function(data) {
                const $str = ['<p>',data.comment_author,': ',data.content,'</p><form action="/feeds/',pk,'/comments/',data.comment_id,'/" method="POST">{% csrf_token %}<button>댓글 삭제</button></form>'];
                $('.comment-list'+pk).append($str);
                $('#comment-content'+pk).val("");
                return;
            },
            error: () => {
                alert('error');
            }
        })
    })
})