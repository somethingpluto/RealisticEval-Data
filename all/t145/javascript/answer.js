function formatCurrency(value, currencyCode, locale = "en-US") {
    const options = {
        style: "currency",
        currency: currencyCode
    };
    return new Intl.NumberFormat(locale, options).format(value);
}