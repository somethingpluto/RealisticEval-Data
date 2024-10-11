
// TODO: TEST_CASE_1 ---> PASCAL_CASE
// @Created by ChatGPT
export const NAMING_CONVENTIONS_REGEX = {
    [NamingConventionEnum.KEBAB_CASE]: /^[a-z][a-z0-9-]*$/,
    [NamingConventionEnum.PASCAL_CASE]: /^[A-Z][a-zA-Z0-9]*$/,
    [NamingConventionEnum.CAMEL_CASE]: /^[a-z][a-zA-Z0-9]*$/,
    [NamingConventionEnum.SNAKE_CASE]: /^[a-z][a-z0-9_]*$/,
    [NamingConventionEnum.UNDEFINED_CASE]: /^.*$/, // it should be at the end
  };
  
  export const DEFAULT_PATH = '/';