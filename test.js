var div_element = document.createElement("div");
div_element.setAttribute('style', 'position: absolute; left: 10px; top: 350px;　width:130px;　height:50px; background-color:orange;');
div_element.setAttribute('id', 'test');
var parent_object = document.getElementById("swiffycontainer");
parent_object.appendChild(div_element);