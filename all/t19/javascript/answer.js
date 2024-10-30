function containsPhoneNumber(s) {
    const pattern = /(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})/;
    return pattern.test(s);
}