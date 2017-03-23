$(document).ready(function(){
  $('.timeFormatDiv').hide();
    $('.newBtn').click(function () {
        $(this).hide();
        $('.timeFormatDiv').show();

    });
    $('.cancelBtn').click(function () {
        $('.timeFormatDiv').hide();
        $('.newBtn').show();
    });
    
      $("#search_id").click(function(){
            var key = $("#search").val();
            $.ajax({
                type:'GET',
                  url:'searchappointments',
                  data:{"key":key},
                  success:function(data){
                    $('#results').empty();
                      $.each( data, function( i, item ) {
                        $('#results').append('<tr><td width="20%">'+item.appointment_date+'</td><td  class="text-left" width="20%">'+item.appointment_time+'</td><td class="text-left">'+item.description+'</td></tr>');
                        
                      });
                  }

            });         
          
        
      });

    getAppointments();

    function getAppointments(){

      $.ajax({
                type:'GET',
                  url:'appointments',
                  success:function(data){
                    $('#results').empty();
                      $.each( data, function( i, item ) {
                        $('#results').append('<tr><td>'+item.appointment_date+'</td><td>'+item.appointment_time+'</td><td>'+item.description+'</td></tr>');
                        
                      });
                  }

            }); 
    }    

    
    $('#datetimepicker1').datepicker({
            autoclose:true,
            format: 'M dd'
        });

    $('#datetimepicker3').datetimepicker({
      pickDate: false,
      language: 'en',
      pick12HourFormat: true
    });

   

});
