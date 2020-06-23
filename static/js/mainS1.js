
$(document).ready(function(){
	$(document).on("submit","#sign_up_form",function (e) {
		// body...
		e.preventDefault();
		var form=$('#sign_up_form').serialize();
		$.ajax({
			url:'/post-sign-up',
			type:'POST',
			data:form,
			success:function(res){
				if(res=="PError"){
					alert("Password dosn't matches");
				}else if( res=="EUError"){
					 alert("username already taken");
				}else if( res!=""){
					 alert("Added Successfully");
					 window.location.href="/";
				}
			}
		});
	});
	$(document).on("submit","#log_in_form",function (e) {
		// body...
		e.preventDefault();
		var form=$('#log_in_form').serialize();
		$.ajax({
			url:'/post-log-in',
			type:'POST',
			data:form,
			success:function(res){
				if(res=="PError"){
					alert("Password dosn't matches");
				}else if( res=="UError"){
					 alert("user dosn't exists");
				}else if( res!=""){
					 OAlertBox("Logged in","/")
					 // window.location.href="/";
				}
			}
		});

	});
	$(document).on("submit","#passBoxForm",function (e) {
		// body...
		
		alert("message?: DOMString");
		e.preventDefault();
	});
	$(document).on("click","#logoutB",function (e) {
		e.preventDefault();
		$.ajax({
			url: '/profile/log_out',
			type: 'GET',
			success:function(res){
				if( res=="success"){
					 OAlertBox("Success!","/profile")
					 // window.location.href="/profile";
				}
			}
		});
		
	});

	// $(document).on("click","#test",function (e) {
	// 	e.preventDefault();
	// 	$("#alertBOX").css("transform","scale(1)");
	// 	$("#app").css('filter', 'blur(2px)');
	// 	$("#header").css('filter', 'blur(2px)');
	// });
});
function OAlertBox(mesg,buVal){
	$("#alertBOX").css("transform","scale(1)");
	$('#alertC').text(mesg)
	$('#alertBU').attr("data-val",buVal)
	$("#app").css('filter', 'blur(2px)');
	$("#header").css('filter', 'blur(2px)');
	$("#blurBG").css('display', 'block');
	
	
}
function CAlertBox(){
	$("#alertBOX").css("transform","scale(0)");
	$("#app").css('filter', 'blur(0px)');
	$("#header").css('filter', 'blur(0px)');
	$("#blurBG").css('display', 'none');
	if(($('#alertBU').attr("data-val"))!=""){
		window.location.href=$('#alertBU').attr("data-val");
	}
}