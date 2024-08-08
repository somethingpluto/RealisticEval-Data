/* function created using chatGPT */
function calculateAge(birthDateString) {
    if (!birthDateString || isNaN(Date.parse(birthDateString))) {
        return '';
    }
    var today = new Date();
    var birthDate = new Date(birthDateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var monthDifference = today.getMonth() - birthDate.getMonth();
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return birthDateString + ' (' + age + ')';
}