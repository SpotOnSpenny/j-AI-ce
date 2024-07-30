function check_vid_devices() {
  if ("mediaDevices" in navigator && "getUserMedia" in navigator.mediaDevices) {
    return true;
  } else {
    return false;
  }
}

function permission_and_start() {
  console.log("Starting function on load");
  const video = document.querySelector("video");
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then((constraints) => {
      console.log("Permission granted");
      stream = startStream(constraints);
      video.srcObject = stream;
    })
    .catch(function (err) {
      console.log("Permission denied");
      // Load the image file input into the video element on page
    });
}

let constraints = {
  video: {
    width: { min: 640, ideal: 1280, max: 1920 },
    height: { min: 480, ideal: 720, max: 1080 },
    facingMode: "environment",
  },
  audio: false,
};
