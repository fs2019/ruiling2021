var li_nav1=document.getElementById("li_nav01");
var ul_indexs=document.getElementById("ul_nav_index");
li_nav1.onmouseover=function(){
		ul_indexs.style.display='inline';		
}
li_nav1.onmouseout=function(){
		ul_indexs.style.display='';		
}

var li_nav2=document.getElementById("li_nav02");
var ul_goods=document.getElementById("ul_nav_goods");
li_nav2.onmouseover=function(){
		ul_goods.style.display='inline';		
}
function st01(){
	li_nav2.onmouseout=function(){
			ul_goods.style.display='';		
	}
}
setTimeout("st01()",2000)
li_nav2.onmouseout=function(){
		ul_goods.style.display='';		
}

var li_nav3=document.getElementById("li_nav03");
var ul_news=document.getElementById("ul_nav_news");
li_nav3.onmouseover=function(){
		ul_news.style.display='inline';		
}
li_nav3.onmouseout=function(){
		ul_news.style.display='';		
}

