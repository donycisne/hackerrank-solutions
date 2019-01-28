const btn = document.createElement('button');

btn.innerHTML = '0';
btn.id = 'btn';
document.body.appendChild(btn);

btn.addEventListener('click', () => btn.innerHTML++);
