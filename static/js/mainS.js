
$(document).ready(function(){
	console.log("loaded");
	$(document).on("submit","#sign_up_form",function (e) {
		// body...
		e.preventDefault();
		var form=$('#sign_up_form').serialize();
		console.log(form);
		$.ajax({
			url:'/post-sign-up',
			type:'POST',
			data:form,
			success:function(res){
				console.log(res);
			}
		});
	});
});