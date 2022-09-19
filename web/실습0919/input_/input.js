const textInput = document.querySelector('#text-input')
const contentInput = document.querySelector('#input-content')

textInput.addEventListener('input', function(ev) {
  console.log(ev);
  console.log(ev.target.value);
  contentInput.innerText = ev.target.value;
});