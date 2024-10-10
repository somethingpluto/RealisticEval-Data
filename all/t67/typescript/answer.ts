import * as fs from 'fs';
import * as path from 'path';

interface Dictionary {
  [key: string]: string;
}

function parseXamlToDict(xamlFilePath: string): Dictionary {
  /**
   * Parses the XAML file, extracts the key-value pairs within the String element, and returns the model_answer_result in a dictionary
   * @param {string} xamlFilePath - Path to the XAML file.
   * @returns {Dictionary} - A dictionary containing the key-value pairs extracted from 'String' elements.
   */

  // Read the content of the XAML file
  const xamlContent = fs.readFileSync(xamlFilePath, 'utf8');

  // Regular expression to match <String> tags with key-value pairs
  const regex = /<String\s+Key="([^"]+)"\s*Value="([^"]+)"/g;

  let match;
  const result: Dictionary = {};

  // Extract key-value pairs using the regular expression
  while ((match = regex.exec(xamlContent)) !== null) {
    const key = match[1];
    const value = match[2];
    result[key] = value;
  }

  return result;
}