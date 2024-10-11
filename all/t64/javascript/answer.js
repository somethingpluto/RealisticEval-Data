const fs = require('fs');
const path = require('path');

function csvToSqlInsert(csvFilePath) {
  const tableName = path.basename(csvFilePath, '.csv');
  let sql = `INSERT INTO ${tableName} VALUES\n`;

  const data = fs.readFileSync(csvFilePath, 'utf8');
  const rows = data.split('\n').map(row => row.trim()).filter(row => row);

  for (let i = 1; i < rows.length; i++) {
    const values = rows[i].split(',').map(value => `'${value}'`);
    sql += `(${values.join(',')})\n`;
  }

  return sql;
}