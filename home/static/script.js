
function handleClick(event) {
  event.preventDefault(); 
  
  var audio = document.getElementById("my_audio");
  audio.play(); 
  
  
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

function closeModal() {
  var audio = document.getElementById("my_audio");
  audio.pause(); 
  
  var modal = document.getElementById("myModal");
  modal.style.display = "none"; 
}

window.onclick = function(event) {
  var modal = document.getElementById("myModal");
  if (event.target == modal) {
      closeModal();
  }
}
