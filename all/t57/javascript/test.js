describe('convert_png_to_ico', () => {
     test('should convert PNG to ICO with default size', async () => {
       const pngFilePath = 'path/to/source.png';
       const icoFilePath = 'path/to/output.ico';

       await convert_png_to_ico(pngFilePath, icoFilePath);

       // Assuming there's a way to check if the ICO file was created successfully
       expect(fs.existsSync(icoFilePath)).toBe(true);
     });

     test('should convert PNG to ICO with custom sizes', async () => {
       const pngFilePath = 'path/to/source.png';
       const icoFilePath = 'path/to/output.ico';
       const iconSizes = [(32, 32), (64, 64)];

       await convert_png_to_ico(pngFilePath, icoFilePath, iconSizes);

       // Assuming there's a way to check if the ICO file was created successfully
       expect(fs.existsSync(icoFilePath)).toBe(true);
     });
   });