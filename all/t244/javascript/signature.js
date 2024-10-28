/**
 * Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
 * expected types, based on the method's signature. If there's a discrepancy, it raises an error.
 *
 * @param {Function} methodObj - The method for which arguments are checked.
 * @param {...any} args - Positional arguments passed to the method.
 * @param {Object} [kwargs] - Keyword arguments passed to the method.
 *
 * @property {Array<string>} [kwargs.exclude=[]] - Names of parameters to exclude from the type check.
 */
function methodArgTypeCheck(methodObj, ...args) {}