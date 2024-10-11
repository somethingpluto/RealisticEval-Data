function htmlToPlainText(html) {
	// Create a new div element
	const div = document.createElement('div');
	// Set the HTML content of the div to the input string
	div.innerHTML = html;
	// Retrieve the plain text version of the HTML string
	let text = div.textContent || div.innerText;
	// Remove new lines
	text = text.replace(/\n/g, ' ').replace("Copy code", "");
	// Remove leading and trailing white space
	text = text.trim();
	return text;
}