#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::pair<std::string, std::string> extract_sld_tld(const std::string& fqdn) {
    // Split the FQDN into parts based on dots
    std::istringstream iss(fqdn);
    std::vector<std::string> parts;
    std::string part;
    while (getline(iss, part, '.')) {
        parts.push_back(part);
    }

    int num_parts = parts.size();
    if (num_parts <= 1) {
        throw std::invalid_argument("Invalid FQDN");
    }

    // Join all but the last two parts to get the SLD
    std::string sld;
    for (int i = 0; i < num_parts - 2; ++i) {
        sld += parts[i];
        if (i != num_parts - 3) {
            sld += '.';
        }
    }

    // The last two parts are TLD
    std::string tld = parts[num_parts - 2] + "." + parts[num_parts - 1];

    return {sld, tld};
}