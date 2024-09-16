function createSquareDivs(num) {
    for (let i = 0; i < num; i++) {
      const square = document.createElement('div');
      square.classList.add('square');
      container.appendChild(square);
    }
  }