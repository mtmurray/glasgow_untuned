$(document).ready(function() {
  $('#likes').click(function(){
  var venid;
  venid = $(this).attr("data-venid");
  $.get('/like_venue/', {venue_id: venid}, function(data){
    $('#like_count').html(data);
      $('#likes').hide();
  });
});
});
