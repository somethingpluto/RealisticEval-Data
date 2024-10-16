#include <iostream>
#include <stdexcept>
#include <string>
#include <cmath>
#include <sstream>

double calculateFinalPrice(const std::string& price, const std::string& discount) {
    double priceValue;
    double discountValue;

    // Convert strings to double
    std::istringstream(price) >> priceValue;
    std::istringstream(discount) >> discountValue;

    // Validate the price and discount
    if (std::isnan(priceValue) || std::isnan(discountValue)) {
        throw std::invalid_argument("Invalid price or discount value.");
    }

    if (discountValue < 0 || discountValue > 100) {
        throw std::invalid_argument("Discount percentage must be between 0 and 100.");
    }

    // Calculate the final price
    double discountAmount = priceValue * discountValue / 100;
    double finalPrice = priceValue - discountAmount;

    // Round to two decimal places
    return std::round(finalPrice * 100) / 100;
}