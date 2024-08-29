const { Pool } = require('pg');
const poolModule = require('./path_to_your_module'); // 这里替换成实际文件路径
const originalEnv = process.env;

beforeEach(() => {
  process.env = { ...originalEnv }; // 每个测试前重置环境变量
});

afterEach(() => {
  process.env = originalEnv; // 测试后恢复原环境变量
});

// 测试用例 1: 所有环境变量都正确设置
test('should create a pool instance when all environment variables are set', () => {
  process.env.POSTGRES_USER = 'test_user';
  process.env.POSTGRES_HOST = 'localhost';
  process.env.POSTGRES_DB = 'test_db';
  process.env.POSTGRES_PASSWORD = 'test_password';
  process.env.POSTGRES_PORT = '5432';

  const pool = poolModule;
  expect(pool).toBeInstanceOf(Pool);
});

// 测试用例 2: 缺少 POSTGRES_USER 环境变量
test('should throw an error when POSTGRES_USER is missing', () => {
  process.env.POSTGRES_HOST = 'localhost';
  process.env.POSTGRES_DB = 'test_db';
  process.env.POSTGRES_PASSWORD = 'test_password';
  process.env.POSTGRES_PORT = '5432';
  delete process.env.POSTGRES_USER;

  expect(() => require('./path_to_your_module')).toThrow();
});

// 测试用例 3: 缺少 POSTGRES_HOST 环境变量
test('should throw an error when POSTGRES_HOST is missing', () => {
  process.env.POSTGRES_USER = 'test_user';
  process.env.POSTGRES_DB = 'test_db';
  process.env.POSTGRES_PASSWORD = 'test_password';
  process.env.POSTGRES_PORT = '5432';
  delete process.env.POSTGRES_HOST;

  expect(() => require('./path_to_your_module')).toThrow();
});

// 测试用例 4: 非数字字符串作为端口号
test('should handle non-numeric POSTGRES_PORT by converting to NaN', () => {
  process.env.POSTGRES_USER = 'test_user';
  process.env.POSTGRES_HOST = 'localhost';
  process.env.POSTGRES_DB = 'test_db';
  process.env.POSTGRES_PASSWORD = 'test_password';
  process.env.POSTGRES_PORT = 'not_a_number';

  const pool = poolModule;
  expect(pool.options.port).toBeNaN();
});

// 测试用例 5: 所有环境变量都正确设置，包括有效的端口号
test('should create a pool instance with a valid port number', () => {
  process.env.POSTGRES_USER = 'test_user';
  process.env.POSTGRES_HOST = 'localhost';
  process.env.POSTGRES_DB = 'test_db';
  process.env.POSTGRES_PASSWORD = 'test_password';
  process.env.POSTGRES_PORT = '5432';

  const pool = poolModule;
  expect(pool.options.port).toBe(5432);
});
