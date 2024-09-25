// Code generated with ChatGPT (I had to modify most of it though for it to actual work lol)

function convertAudioToBase64(arrayBuffer) {

  let name = `./tmp/${Date.now()}`
  // Convert ArrayBuffer to Buffer
  const buffer = Buffer.from(arrayBuffer);

  // Save the Buffer to a temporary WAV file
  fs.writeFileSync(`${name}.wav`, buffer);

  return new Promise((resolve, reject) => {
    // Convert the WAV file to raw format using fluent-ffmpeg
    ffmpeg(`${name}.wav`)
    .format(`s16le`)
    .audioCodec(`pcm_s16le`)
    .audioFrequency(44100)
    .audioChannels(1)
    .duration(`00:00:05.000`)
    .output(`${name}.raw`)
      .on('end', () => {
        try {
          // Read the converted raw audio file
          const convertedBuffer = fs.readFileSync(`${name}.raw`);

          // Convert the audio data to Base64
          const base64Data = convertedBuffer.toString('base64');

          // Delete the temporary files
          fs.unlinkSync(`${name}.wav`);
          fs.unlinkSync(`${name}.raw`);

          resolve(base64Data);
        } catch (error) {
          reject(error);
        }
      })
      .on('error', (error) => {
        reject(error);
      })
      .run();
  });
}