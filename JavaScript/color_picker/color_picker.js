x = document.getElementById("color");
ctx = x.getContext("2d");

setTimeout(check, 1);

function save(){

	document.getElementById("r_value").value = document.getElementById("r_slider").value;
	document.getElementById("g_value").value = document.getElementById("g_slider").value;
	document.getElementById("b_value").value = document.getElementById("b_slider").value;
	
	document.getElementById("r_value").innerHTML = r;
	document.getElementById("g_value").innerHTML = g;
	document.getElementById("b_value").innerHTML = b;

	r = document.getElementById("r_value").value;
	g = document.getElementById("g_value").value;
	b = document.getElementById("b_value").value;

	ctx.fillStyle = "rgb(" + r + "," + g + "," + b + ")";
	ctx.fillRect(0, 0, 120, 120);
	document.getElementById("to_copy").innerHTML = "Rgb values: rgb(" + r +", " + g + ", " + b + ")";
		
	if(r > 198 && r < 218 && g > 194 && g < 214 && b > 194 && b < 214){
		document.body.style.backgroundColor = "rgb(80, 80, 220)";
	}

	else{
		document.body.style.backgroundColor = "rgb(208, 204, 204)";
	}
}

function check(){
	save();
setTimeout(check, 1);
}
