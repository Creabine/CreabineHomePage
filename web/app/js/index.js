$(document).ready(function(){

	$("#headerNavBtn").on('click', function(event) {
		$("#headerMenu").slideToggle(400);
		$("#headerMenu").css('display', 'block');
	});

	$('body').scrollTop(0);

});
function scrollfuntion(){
	var topDistance = $("#allpage").scrollTop();
	topDistance != 0 ? $("#header").addClass('headerHover') : $("#header").removeClass('headerHover');
	topDistance > 300 ? $("#up").slideDown(300) : $("#up").slideUp(500);
	if( !$("#pc").hasClass('pc') && topDistance > 300 ){
		$("#pc").addClass('pc');
		$("#phone").addClass('phone');
		$("#pad").addClass('pad');
	}
	if( $("#pc").hasClass('pc') && (topDistance > 1400 || topDistance < 300) ){
		$("#pc").removeClass('pc');
		$("#phone").removeClass('phone');
		$("#pad").removeClass('pad');
	}
}
function up(){
	$('body').animate({ scrollTop: 0 },300);
}