function line(index) {
	var checkBox = document.getElementById(index);
	var text = document.getElementById("row" + index);
	if (checkBox.checked == true) {
		text.style.textDecoration = "line-through";
	} else {
		text.style.textDecoration = "none";
	}
}
function log(data) {
	console.log(data);
}