function simplifyWindowsPath(path: string): string {
  // Match the drive letter at the beginning of the path (e.g., "C:" or "D:")
  const driveMatch = path.match(/^([A-Z]):/i); 
  let simplifiedDrive = '';   // This will hold the simplified drive part
  let simplifiedPath = path;  // This will hold the simplified path without drive

  // If there is a drive letter, modify it
  if (driveMatch) {
      simplifiedDrive = driveMatch[1] + '_'; // Replace the colon (:) with an underscore (_)
      simplifiedPath = path.slice(driveMatch[0].length); // Remove the drive part (e.g., "C:" from the path)
  }

  // Replace backslashes with underscores, and remove a leading underscore if present
  simplifiedPath = simplifiedPath.replace(/\\/g, '_').replace(/^_/, ''); // Remove leading underscore

  // Return the modified path: drive + path
  return simplifiedDrive + simplifiedPath;
}
