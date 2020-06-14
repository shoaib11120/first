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
function hoverFun(span) {
			// body...
			span.classList.add("FHover");
		}
		function nonhoverFun(span) {
			// body...
			span.classList.remove("FHover");
		}
		function DTextFun(inp){
			alert(this.value)
		}
		function fun1(ev){
			document.getElementById(ev).click();
		}