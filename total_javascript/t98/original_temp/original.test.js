// filename: dbConnection.test.js

const { Pool } = require('pg');

// Mock the pg module
jest.mock('pg', () => {
  return {
    Pool: jest.fn(),
  };
});

// Function to load the dbConnection module after mocking
const loadDbConnection = () => require('./dbConnection');

describe('PostgreSQL Pool Configuration', () => {
  let originalEnv;

  beforeEach(() => {
    // Save the original environment variables
    originalEnv = { ...process.env };
  });

  afterEach(() => {
    // Restore the original environment variables after each test
    process.env = originalEnv;
    jest.resetModules(); // Reset module registry to avoid caching between tests
  });

  test('should configure pool with correct environment variables', () => {
    process.env.POSTGRES_USER = 'testuser';
    process.env.POSTGRES_HOST = 'localhost';
    process.env.POSTGRES_DB = 'testdb';
    process.env.POSTGRES_PASSWORD = 'testpassword';
    process.env.POSTGRES_PORT = '5432';

    loadDbConnection();

    expect(Pool).toHaveBeenCalledWith({
      user: 'testuser',
      host: 'localhost',
      database: 'testdb',
      password: 'testpassword',
      port: 5432,
    });
  });

  test('should throw error if POSTGRES_USER is not set', () => {
    delete process.env.POSTGRES_USER;
    process.env.POSTGRES_HOST = 'localhost';
    process.env.POSTGRES_DB = 'testdb';
    process.env.POSTGRES_PASSWORD = 'testpassword';
    process.env.POSTGRES_PORT = '5432';

    expect(() => loadDbConnection()).toThrow();
  });

  test('should throw error if POSTGRES_PASSWORD is missing', () => {
    process.env.POSTGRES_USER = 'testuser';
    process.env.POSTGRES_HOST = 'localhost';
    process.env.POSTGRES_DB = 'testdb';
    delete process.env.POSTGRES_PASSWORD;
    process.env.POSTGRES_PORT = '5432';

    expect(() => loadDbConnection()).toThrow();
  });

  test('should set default port to 5432 if POSTGRES_PORT is not defined', () => {
    process.env.POSTGRES_USER = 'testuser';
    process.env.POSTGRES_HOST = 'localhost';
    process.env.POSTGRES_DB = 'testdb';
    process.env.POSTGRES_PASSWORD = 'testpassword';
    delete process.env.POSTGRES_PORT;

    loadDbConnection();

    expect(Pool).toHaveBeenCalledWith({
      user: 'testuser',
      host: 'localhost',
      database: 'testdb',
      password: 'testpassword',
      port: 5432, // Default port
    });
  });

  test('should convert POSTGRES_PORT to an integer', () => {
    process.env.POSTGRES_USER = 'testuser';
    process.env.POSTGRES_HOST = 'localhost';
    process.env.POSTGRES_DB = 'testdb';
    process.env.POSTGRES_PASSWORD = 'testpassword';
    process.env.POSTGRES_PORT = '5432';

    loadDbConnection();

    expect(Pool).toHaveBeenCalledWith({
      user: 'testuser',
      host: 'localhost',
      database: 'testdb',
      password: 'testpassword',
      port: 5432, // Ensure port is an integer
    });
  });
});
