const { JSDOM } = require("jsdom");

// Test case setup using jsdom
function createMockDocument(html) {
  const dom = new JSDOM(html);
  return dom.window.document;
}

// Test cases
function runTestCases() {
  // Test Case 1: Table with multiple rows and columns
  const testCase1HTML = `
    <table class="waffle">
      <tbody>
        <tr><td>Cell 1</td><td>Cell 2</td></tr>
        <tr><td>Cell 3</td><td>Cell 4</td></tr>
      </tbody>
    </table>`;
  const document1 = createMockDocument(testCase1HTML);
  console.assert(
    JSON.stringify(extractCSVDataFromHTML(document1)) === JSON.stringify([["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]]),
    "Test Case 1 Failed"
  );

  // Test Case 2: Table with empty cells
  const testCase2HTML = `
    <table class="waffle">
      <tbody>
        <tr><td>Cell 1</td><td></td></tr>
        <tr><td></td><td>Cell 4</td></tr>
      </tbody>
    </table>`;
  const document2 = createMockDocument(testCase2HTML);
  console.assert(
    JSON.stringify(extractCSVDataFromHTML(document2)) === JSON.stringify([["Cell 1", ""], ["", "Cell 4"]]),
    "Test Case 2 Failed"
  );

  // Test Case 3: Table with only one row
  const testCase3HTML = `
    <table class="waffle">
      <tbody>
        <tr><td>Single Cell 1</td><td>Single Cell 2</td></tr>
      </tbody>
    </table>`;
  const document3 = createMockDocument(testCase3HTML);
  console.assert(
    JSON.stringify(extractCSVDataFromHTML(document3)) === JSON.stringify([["Single Cell 1", "Single Cell 2"]]),
    "Test Case 3 Failed"
  );

  // Test Case 4: Table with only one column
  const testCase4HTML = `
    <table class="waffle">
      <tbody>
        <tr><td>Column Cell 1</td></tr>
        <tr><td>Column Cell 2</td></tr>
      </tbody>
    </table>`;
  const document4 = createMockDocument(testCase4HTML);
  console.assert(
    JSON.stringify(extractCSVDataFromHTML(document4)) === JSON.stringify([["Column Cell 1"], ["Column Cell 2"]]),
    "Test Case 4 Failed"
  );

  // Test Case 5: No table with the class "waffle" present
  const testCase5HTML = `
    <div>
      <p>No table here!</p>
    </div>`;
  const document5 = createMockDocument(testCase5HTML);
  console.assert(
    JSON.stringify(extractCSVDataFromHTML(document5)) === JSON.stringify([]),
    "Test Case 5 Failed"
  );

  console.log("All test cases passed!");
}

// Define the function to be tested
function extractCSVDataFromHTML(document) {
  const table = document.querySelector("table.waffle");
  const result = [];

  if (!table) {
    console.error("CSV table not found.");
    return result;
  }

  const rows = table.querySelectorAll("tbody tr");

  rows.forEach(row => {
    const rowData = Array.from(row.querySelectorAll("td")).map(td => td.textContent.trim());
    result.push(rowData);
  });

  return result;
}

// Run all test cases
runTestCases();
