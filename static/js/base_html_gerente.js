// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
    if (mySidebar.style.display === 'block') {
        mySidebar.style.display = 'none';
        overlayBg.style.display = "none";
        resize_mapa();
    } else {
        mySidebar.style.display = 'block';
        overlayBg.style.display = "block";
        resize_mapa();
    }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
    resize_mapa();
}

function controleDropdown(elementId) {
    var x = document.getElementById(elementId);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        resize_mapa();
    } else { 
        x.className = x.className.replace(" w3-show", "");
        resize_mapa();
    }
}

