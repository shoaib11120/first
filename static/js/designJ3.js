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
			var inP=inp.value;
			i=inP.lastIndexOf("\\");
			alert("hello "+ inP.substring(i+1));
			uploadButton=document.getElementById('AUButton');
			uploadButton.style.display = 'block';
			uploadButton.innerHTML=inP.substring(i+1);
		}
		function fun1(ev){
			document.getElementById(ev).click();
		}