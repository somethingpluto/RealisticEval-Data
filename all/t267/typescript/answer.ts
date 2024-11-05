function extractSldTld(fqdn: string): [string, string] {
    // Split the FQDN into parts
    const parts = fqdn.split('.');

    // Check if there are enough parts to extract SLD and TLD
    if (parts.length < 2) {
        throw new Error("The provided FQDN does not contain enough parts to extract SLD and TLD.");
    }

    // Extract the SLD and TLD
    const sld = parts[parts.length - 2];  // Second to last item is the SLD
    const tld = parts[parts.length - 1];  // Last item is the TLD

    return [sld, tld];
}