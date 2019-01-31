const buttons = document.querySelectorAll('button');

for (let btn of buttons) {
    btn.onclick = click;
}

function click(e) {
  const btn = e.target || e.srcElement;
  const action = document.getElementById(btn.id).innerHTML;
  const screen = document.getElementById('res');

  switch (action) {
    case '0':
    case '1':
    case '+':
    case '-':
    case '*':
    case '/':
      screen.innerHTML += action;
      break;
    case 'C':
      screen.innerHTML = '';
      break;
    case '=':
      const equalRegex = /(\d+)/g;
      let result = screen.innerHTML;
      result = result.replace(equalRegex, match => parseInt(match, 2))
      screen.innerHTML = parseInt(eval(result).toString(2));
      break;
  }
}
