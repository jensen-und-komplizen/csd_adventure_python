$( document ).ready(function() {
    $('#command').focus();
    $('#commandForm').submit(function( event ) {
        event.preventDefault();
        $.ajax({
            url: "/command",
            data: {command: $('#command').val()},
        })
            .done(function( data ) {
                if ( console && console.log ) {
                    console.log( "Sample of data--:", data.slice( 0, 100 ) );
                }
                $("#gameInfo").html(data);
                $('#command').val("");
            });
    });
    $('.standard-command-button').on('click', ({ currentTarget }) => {
        $('#command').val(currentTarget.innerText).trigger('submit');
    });
});