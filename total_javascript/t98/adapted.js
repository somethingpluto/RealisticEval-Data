// Import the pg module
const { Pool } = require('pg');

// Configure the PostgreSQL connection pool using environment variables
const pool = new Pool({
  user: process.env.POSTGRES_USER,
  host: process.env.POSTGRES_HOST,
  database: process.env.POSTGRES_DB,
  password: process.env.POSTGRES_PASSWORD,
  port: parseInt(process.env.POSTGRES_PORT, 10), // Ensure the port is an integer
});

// Export the pool for use in other parts of the application
module.exports = pool;
