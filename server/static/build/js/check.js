/**
 * Created by minhkma on 9/7/18.
 */
$(window).load(function() {

    (function top(){
        $.ajax({
            url: 'ajax/top',
            success: function(data) {
                $('#user_1').html(data['user_1']);
                $('#user_2').html(data['user_2']);
                $('#user_3').html(data['user_3']);
                $('#user_4').html(data['user_4']);
                $('#user_5').html(data['user_5']);
                $('#user_6').html(data['user_6']);
                $('#user_7').html(data['user_7']);
                $('#user_8').html(data['user_8']);
                $('#user_9').html(data['user_9']);
                $('#user_10').html(data['user_10']);
            },
            failure: function(data) {
                console.log('Got an error total parameter');
            }
        }).then(function() {           // on completion, restart
            setTimeout(top, 10000);  // function refers to itself
        });
    })();

});