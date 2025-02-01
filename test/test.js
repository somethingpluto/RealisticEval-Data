// 引入 jest 测试功能
const { expect, test } = require('@jest/globals');

// 一个简单的函数用于测试
function sum(a, b) {
  return a + b;
}

// 一个测试用例
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('adds 2 + 3 to equal 5', () => {
  expect(sum(2, 3)).toBe(5);
});
