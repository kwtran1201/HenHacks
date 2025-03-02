let points = parseInt(document.getElementById("points").textContent) || 0;  // Get the initial points value from the DOM

function previewImage(event, previewId) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById(previewId);
        output.src = reader.result;
        output.style.display = "block";
    };
    reader.readAsDataURL(event.target.files[0]);
    
    checkUploadButton();
}

function checkUploadButton() {
    let fileInput1 = document.getElementById("image1");
    let fileInput2 = document.getElementById("image2");
    let uploadButton = document.getElementById("uploadButton");

    if (fileInput1.files.length > 0 && fileInput2.files.length > 0) {
        uploadButton.disabled = false;
    } else {
        uploadButton.disabled = true;
    }
}

function uploadImages() {
    let fileInput1 = document.getElementById("image1");
    let fileInput2 = document.getElementById("image2");

    let pointsEarned = 0;

    if (fileInput1.files.length > 0) pointsEarned += 10;  // 10 points for each image uploaded
    if (fileInput2.files.length > 0) pointsEarned += 10;

    if (pointsEarned > 0) {
        points += pointsEarned;  // Add points to the global points counter
        document.getElementById("points").textContent = points;  // Update the points display on the page
        alert(`Images uploaded successfully! You earned ${pointsEarned} points.`);
        
        // Disable the upload button after uploading
        let uploadButton = document.getElementById("uploadButton");
        uploadButton.disabled = true;
    }
}

// Reset the upload button when a new location is selected
function resetUploadButton() {
    let uploadButton = document.getElementById("uploadButton");
    let fileInput1 = document.getElementById("image1");
    let fileInput2 = document.getElementById("image2");

    uploadButton.disabled = true;  // Disable the button
    fileInput1.value = '';        // Clear file input
    fileInput2.value = '';        // Clear file input
    document.getElementById("preview1").style.display = "none";  // Hide the preview for image 1
    document.getElementById("preview2").style.display = "none";  // Hide the preview for image 2
}
