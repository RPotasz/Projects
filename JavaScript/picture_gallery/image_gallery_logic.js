class image_state{
	constructor(current, freeze){
		this.current = current;
		this.freeze = freeze;
	}
}


let gallery = new image_state(1, false);

// Function to change images in loop
function iterate_through(gallery){
	setTimeout(function() {
	if (gallery.freeze == false){
		next = gallery.current + 1;
	if (next > 4){
		next = 1;
	}
		document.getElementById("dot_" + gallery.current.toString()).style.backgroundColor = "blue";
		document.getElementById("dot_" + next.toString()).style.backgroundColor = "gold";
		document.getElementById("image_" + gallery.current.toString()).style.display = "none";
		document.getElementById("image_" + next.toString()).style.display = "block";
		gallery.current = next;
		iterate_through(gallery);
	}
	if (gallery.freeze == true){
		iterate_through(gallery);
	}
	}, 4000);
}


function hide_images(){
	for(let i = 1; i < 5; i++){
		document.getElementById("image_" + i.toString()).style.display = "none";
	} }

// Function to toggle freezing
function change_state(gallery){
	button_text = document.getElementById("state");
	if (button_text.innerText == "Pause"){
		button_text.innerText = "Resume";
		gallery.freeze = true;
	}
	else{
		button_text.innerText = "Pause";
		gallery.freeze = false;
	}
}

// Function to display clicked image
function set_image(gallery, idx){
	hide_images();
	document.getElementById("dot_" + gallery.current).style.backgroundColor = "blue";
	if (idx > -10 & idx < 10){
		display = "image_" + idx.toString()
	}
	if (idx == -10){
		idx = gallery.current - 1;
		if (idx < 1){
			idx = 4;
		}		}
	if (idx == 10){
		idx = gallery.current + 1;
		if (idx > 4){
			idx = 1;
		}		}

		display = "image_" + idx.toString()
		display_dot = "dot_" + idx.toString()
		image_to_display = document.getElementById(display)
		button_to_change = document.getElementById(display_dot)
		button_to_change.style.backgroundColor = "gold";
		image_to_display.style.display = "block"
		gallery.current = idx;
	}

function show_controls(){
	document.getElementById("buttons_display").style.display = "block";
}

function hide_controls(){
	document.getElementById("buttons_display").style.display = "none";
}


iterate_through(gallery);