import { Dictionary } from "lodash";
/**
 * Recursively sanitizes a dictionary by removing specific keys.
 * 
 * @param data - The original dictionary to sanitize.
 * @param keyToRemove - An optional list of keys to remove. If not provided, defaults to a predefined set of keys.
 * @returns The sanitized dictionary.
 */
function sanitizeData(data: Dictionary<any>, keyToRemove?: string[]): Dictionary<any> {}