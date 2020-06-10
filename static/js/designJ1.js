function focusFun(sp) {
	// body...
	span=document.getElementById(sp);
	span.classList.add("focus");
}
function blurFun(inn,sp) {
	// body...
	span=document.getElementById(sp);
	if(inn.value==''){
		if(span.classList.contains("focus")){
			span.classList.remove("focus");
		}
	}
	
}