$(function () { 

    var $players = $('#players_ul')
    var $ip      = $('#ipNumber')
    var $port   = $('#portNumber')

    $.ajax({
        type: "get",
        url: "/api/players", /** getting data */
        success: function (players) { /** then split  with success func it to the page */
          $.each(players, function (index, player) { /** for each players run the func give us a player */
              $(players).append((players.ip, players.port)); /** u can insert li inside the append */  
          });  
        },
        error: function () { 
            alert('Hello Awet tell me where to send the player if error! ')/** will be alert if url is wrong */
         }
    });



    $('#sendStudent').on('click', function () { /** on click of the button do sth */
        var player = {
            /** built an object and send to the server */
            ip:   $ip.val(),
            port: $port.val(),
        };


        $.ajax({
            type: "POST",
            url: "/api/players",
            data = order,
            success: function (players) {
              $.each(player, function (index, player) { 
                  $(players).append(content);   
              });  
            },
            error: function () { 
                alert('Wrong input ! ')
             }
        });
     });
 });