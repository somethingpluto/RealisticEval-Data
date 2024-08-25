module.exports = {
    preset: 'ts-jest',
    transform: {
        '^.+\\.tsx?$': ['ts-jest', {
            babel: true,
            tsconfig: 'tsconfig.json', // 修改字段名
        }]
    },
    // 允许测试 .ts 和 .tsx 文件
    testRegex: '(/__tests__/.*|(\\.|/)(test|spec))\\.tsx?$',

    // 指定文件扩展名的处理顺序
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],

    // 测试环境，通常是 'node' 或 'jsdom'
    testEnvironment: 'node',

    // 配置 Jest 是否生成覆盖率报告
    collectCoverage: false,

    // 设置 Jest 需要显示的警告
    verbose: false,
};
