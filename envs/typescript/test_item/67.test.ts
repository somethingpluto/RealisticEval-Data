// ... (previous code for context)
import { parseFile } from 'xml2js';
import { readFile } from 'fs/promises';
import { createHash } from 'crypto';

interface XamlKeyValuePair {
  key: string;
  value: string;
}

async function parseXamlToDict(xamlFile: string): Promise<Record<string, string>> {
  const hash = createHash('sha256');
  const fileBuffer = await readFile(xamlFile);
  hash.update(fileBuffer);
  const fileHash = hash.digest('hex');

  // Check if the file has been modified since the last parse
  // This is a placeholder for the actual implementation of caching logic
  if (/* file has not been modified */) {
    return {}; // Return cached result
  }

  try {
    const xamlString = fileBuffer.toString();
    const result: Record<string, string> = {};
    const { String } = await parseFile(xamlString, { explicitArray: false });

    if (String) {
      String.forEach((element: XamlKeyValuePair) => {
        if (element.key && element.value) {
          result[element.key] = element.value;
        }
      });
    }

    return result;
  } catch (error) {
    console.error('Error parsing XAML file:', error);
    throw error;
  }
}
// ... (rest of the code)
import * as fs from 'fs';
import * as xml2js from 'xml2js';

describe('TestParseXamlToDict', () => {
  it('should correctly parse valid strings', () => {
    const xamlData = `
      <root>
        <String Key="Username">Alice</String>
        <String Key="Password">secret</String>
      </root>
    `;
    const expected = { Username: 'Alice', Password: 'secret' };
    const result = parseXamlToDict(xamlData);
    expect(result).toEqual(expected);
  });

  it('should handle missing key attribute', () => {
    const xamlData = `
      <root>
        <String>Alice</String>
      </root>
    `;
    const expected = {};
    const result = parseXamlToDict(xamlData);
    expect(result).toEqual(expected);
  });

  it('should handle no string tags', () => {
    const xamlData = `
      <root>
        <Data>Some question</Data>
      </root>
    `;
    const expected = {};
    const result = parseXamlToDict(xamlData);
    expect(result).toEqual(expected);
  });

  it('should correctly parse nested string tags', () => {
    const xamlData = `
      <root>
        <Container>
          <String Key="Username">Bob</String>
        </Container>
        <String Key="Location">Earth</String>
      </root>
    `;
    const expected = { Username: 'Bob', Location: 'Earth' };
    const result = parseXamlToDict(xamlData);
    expect(result).toEqual(expected);
  });
});
