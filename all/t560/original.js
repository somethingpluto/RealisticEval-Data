function getLineNumber(content, index) {
    return content.slice(0, index).split("\n").length;
  }