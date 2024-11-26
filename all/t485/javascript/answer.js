import re from 're'
function prepareQuery(sql, params) {
    const namedParams = sql.match(/\$(\w+)/g).map(match => match.slice(1));

    // Remove duplicates while preserving order
    const uniqueParams = [...new Set(namedParams)];

    // Substitute each named parameter with its corresponding positional parameter
    uniqueParams.forEach((param, index) => {
        sql = sql.replace(new RegExp(`\\$${param}`, 'g'), `$${index + 1}`);
    });

    // Prepare the list of values corresponding to the order of the positional parameters
    const values = uniqueParams.filter(param => param in params).map(param => params[param]);

    return [sql, values];
}