function toggleVisible(id) {
  elem = document.getElementById(id);
  if (elem.style.display != 'block') {
    elem.style.display = 'block';
  } else {
    elem.style.display = 'none';
  }
}