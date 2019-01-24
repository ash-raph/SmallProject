$(document).ready(function() {
    $("form.ajax_call").on('submit', function(event){
            parent = $(this).parent().parent();
            event.preventDefault();
            // ---------------------
            $.ajax({
                type: "POST",
                url: $(this).attr("action"),
                data: $(this).serialize(),
                beforeSend: function() {
                    }, /* beforeSend */

                error: function(xhr, errmsg, err) {
                    window.alert("Unknown error occurred ");
                    }, /* error */

                success: function(json) {
                    $(parent).fadeOut(500, function() { $(this).remove(); });
                }, /* success */
               });
            // ---------------------
        });
    });