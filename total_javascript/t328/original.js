// Remove punctuation in a sentence. This function was written by ChatGPT on the 9th of April 2023. Thanks Chatty!
function CN_RemovePunctuation(str) {
	const regexPonctuation = /[\u2000-\u206F\u2E00-\u2E7F\\'!"#$%&()*+,\-./:;<=>?@\[\]^_`{|}~]/g;
	str = str.replace(regexPonctuation, '')+"";
	return str.toLowerCase().trim();
}
