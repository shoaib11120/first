
$(document).ready(function () {
	// body...
	console.log("loaded");
	$.material.init();
	$(document).on("submit","#sign_up_form",function (e) {
		// body...
		e.preventDefault();
		console.log("jquery-3.5.1.js");
		// var form=$('#sign_up_form').serialize();
		// $.ajax({
		// 	url:'/post-sign-up',
		// 	type:'POST',
		// 	data:form,
		// 	success:function(res){
		// 		console.log(res);
		// 	}
		// });
	});
});