// checking if DOM is loaded

function checkDOMLoaded() {
  if (document.readyState === 'interactive' || document.readyState === 'complete') {
    console.log('DOM has loaded!');
    // code to handle the loaded DOM goes here
    document.getElementById('loader').style.display = 'none';
  } else {
    console.log('DOM is still loading...');
    document.getElementById('loader').style.display = 'block';

  }
}
// calling the function
document.addEventListener('DOMContentLoaded', checkDOMLoaded);

