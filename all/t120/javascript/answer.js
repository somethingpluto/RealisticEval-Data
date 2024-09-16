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
  