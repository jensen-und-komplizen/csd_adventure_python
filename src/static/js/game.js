let commandArray = [];
lastItemIndex = 0
searchIndex = 1

// Push items to the array
$( document ).ready(function() {
    $('#command').focus();
    $('#commandForm').submit(function( event ) {
        event.preventDefault();
        updateCommandArray($('#command').val());
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
});

// Listen to keystrokes
$(document).keydown(function(e) {
    switch(e.which) {
        case 38: // up arrow
            if (searchIndex < commandArray.length) {
                searchIndex++
            }
            $('#command').val(commandArray[lastItemIndex - searchIndex]);
            break;
        case 40: // down arrow
            if (searchIndex > 0) {
                searchIndex--
            }
            $('#command').val(commandArray[lastItemIndex - searchIndex]);
            break;
    }
});

function updateCommandArray(command){
    commandArray.push(command);
    lastItemIndex = commandArray.length
    searchIndex = 0
}
