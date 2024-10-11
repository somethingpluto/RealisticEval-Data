interface Loggable {
  toString(): string;
}

function log<T extends Loggable>(item: T): T {
  try {
    console.log(item.toString());
  } catch (error) {
    console.error(`Error logging item: ${error}`);
  }
  return item;
}