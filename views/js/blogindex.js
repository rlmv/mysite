
// hide all but the first paragraph of the post
$(document).ready(function() {
    $(".blogcontent").children().not(":first-child").hide();
})


// reveal the rest of the post, or link to it if already revealed.
$(".blogtitle").click(function(event){
    event.preventDefault();
    $(this).siblings().children().show();
})