from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def watch():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Stream</title>
      <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
      <style>
        body { background: #111; display: flex; justify-content: center;
               align-items: center; height: 100vh; margin: 0; }
        video { width: 90%; max-width: 900px; border-radius: 8px; }
      </style>
    </head>
    <body>
      <video id="v" controls autoplay muted></video>
      <script>
        const video = document.getElementById('v');
        const src = `http://${location.hostname}:8080/hls/stream.m3u8`;
        if (Hls.isSupported()) {
          const hls = new Hls();
          hls.loadSource(src);
          hls.attachMedia(video);
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
          video.src = src;
        }
      </script>
    </body>
    </html>
    """