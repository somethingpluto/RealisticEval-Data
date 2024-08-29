/* function created using chatGPT */
function setEurValue(value) {
    if (!value) return '';
    
    const number = parseInt(value, 10);
    if (isNaN(number)) return '';

    if (number >= 1_000_000) {
        return `${(number / 1_000_000).toFixed(1)}m`;
    } else if (number >= 1_000) {
        return `${(number / 1_000).toFixed(1)}k`;
    } else {
        return `${number}`;
    }
}
