module.exports = {
    // 设置测试环境
    testEnvironment: "node",
    // 指定需要忽略的文件或目录
    testPathIgnorePatterns: ["/node_modules/"],
    silent: true,
    collectCoverage: false,  // 收集测试覆盖率
    transform: {
        "^.+\\.jsx?$": "babel-jest"
    }
};