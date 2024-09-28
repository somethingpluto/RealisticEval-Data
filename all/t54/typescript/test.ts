// Import the necessary functions from Jest
import { describe, it, expect } from '@jest/globals';
// Import the function to be tested
import { removeTripleBackticks } from './path-to-your-function-file';

// Group related tests in a describe block
describe('removeTripleBackticks', () => {
    
    it('removes triple backticks from basic cases', () => {
        // Test basic functionality
        const inputStrings = ['Here is