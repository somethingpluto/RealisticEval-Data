/**
 * generated by ChatGPT
 */
export const formatCurrency = (
    value: number,
    currencyCode: string,
    locale = "en-US"
  ) => {
    return new Intl.NumberFormat(locale, {
      style: "currency",
      currency: currencyCode,
    }).format(value);
  };