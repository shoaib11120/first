
$(document).ready(function(){
	console.log("loaded");
	$(document).on("submit","#sign_up_form",function (e) {
		// body...
		e.preventDefault();
		var form=$('#sign_up_form').serialize();
		$.ajax({
			url:'/post-sign-up',
			type:'POST',
			data:form,
			success:function(res){
				if (res=="success"){
					alert("Added Successfully");
					window.location.href="/profile";
				}else if(res=="PError"){
					alert("Password dosn't matches");
				}
			}
		});
	});
});