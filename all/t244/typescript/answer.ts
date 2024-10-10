function methodArgTypeCheck(methodObj: Function, ...args: any[], ...kwargs: any[]): void {
  const signature = getMethodSignature(methodObj);

  if (!signature) {
    throw new Error('Could not retrieve method signature');
  }

  const argNames = Object.keys(signature.parameters);
  const argValues = [...args, ...Object.values(kwargs)];

  if (argNames.length !== argValues.length) {
    throw new Error('Argument count mismatch');
  }

  argNames.forEach((name, index) => {
    const value = argValues[index];
    const type = signature.parameters[name];

    if (typeof value !== type) {
      throw new Error(`Argument ${name} has incorrect type. Expected ${type}, got ${typeof value}`);
    }
  });
}