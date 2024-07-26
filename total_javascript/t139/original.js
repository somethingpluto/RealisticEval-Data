// This module was written by GPT-4

export default function parseCategoriesFromSummary(summarizedOutput = '') {
    const categoriesRegex = /Categories:\s*\[([^\]]+)\]/;
    const match = summarizedOutput.match(categoriesRegex);
  
    let categories = [];
    let summary = summarizedOutput;
  
    if (match && match[1]) {
      categories = match[1].split(',').map(category => category.trim());
      summary = summarizedOutput.replace(categoriesRegex, '').trim();
    }
  
    return { summary, categories };
  }