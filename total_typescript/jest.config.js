module.exports = {
    // 指定测试文件所在的目录
    roots: ['<rootDir>/src'],
  
    // 使用 ts-jest 作为处理 TypeScript 文件的预处理器
    transform: {
      '^.+\\.tsx?$': 'ts-jest',
    },
  
    // 允许测试 .ts 和 .tsx 文件
    testRegex: '(/__tests__/.*|(\\.|/)(test|spec))\\.tsx?$',
  
    // 指定文件扩展名的处理顺序
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
  
    // 配置 Jest 用于 TypeScript 的类型检查
    globals: {
      'ts-jest': {
        tsconfig: 'tsconfig.json',
      },
    },
  
    // 测试环境，通常是 'node' 或 'jsdom'
    testEnvironment: 'node',
  
    // 配置 Jest 是否生成覆盖率报告
    collectCoverage: true,
  
    // 指定覆盖率报告生成的位置
    coverageDirectory: '<rootDir>/coverage',
  
    // 设置需要忽略的模块路径
    modulePathIgnorePatterns: ['<rootDir>/dist/'],
  
    // 忽略 node_modules 中的文件，但允许处理一些特殊模块
    transformIgnorePatterns: ['<rootDir>/node_modules/'],
  
    // 设置 Jest 需要显示的警告
    verbose: true,
  };