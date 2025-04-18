    // This shit was generated by ChatGPT
    function convertTime(duration) {
        const regex = /PT(?:(\d+)H)?(?:(\d+)M)?([\d.]+)S/;
        const matches = duration.match(regex);

        let convertedTime = '';

        if (matches[1]) {
          convertedTime += matches[1] + 'h';
        }

        if (matches[2]) {
          convertedTime += matches[2] + 'm';
        }

        const seconds = parseFloat(matches[3]);

        if (seconds > 0 || convertedTime === '') {
          const wholeSeconds = Math.floor(seconds);
          convertedTime += wholeSeconds + 's';

          const milliseconds = Math.round((seconds - wholeSeconds) * 1000);

          if (milliseconds > 0) {
            convertedTime += milliseconds + 'ms';
          }
        }

        return convertedTime;
      }