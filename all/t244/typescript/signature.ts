/**
 * Checks that the arguments passed to a given method object (e.g., method of a class) comply with their
 * expected question types, based on the method's signature. If there's a discrepancy, it raises a ValueError.
 *
 * @param methodObj - The method for which arguments are checked.
 * @param args - Positional arguments passed to the method.
 * @param kwargs - Keyword arguments passed to the method.
 *
 * @returns Nothing, but throws an error if there's a discrepancy in argument types.
 */
function methodArgTypeCheck(methodObj: (...args: any[]) => any, ...args: any[], ...kwargs: any[]): void{

}