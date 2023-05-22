// utilizing inbuilt web browser js for loading animation

window.addEventListener('load', function() {
    // Delay the display of page contents by 3 seconds
    setTimeout(function() {
      document.getElementById('loader').style.display = 'none'; // Hide the loader
      //document.getElementById('content').style.display = 'block'; // Show the page contents
    }, 3000);
  });
  

