from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

STREAM_KEY = "mitchiscool123"

@app.post("/hooks/publish")
async def on_publish(request: Request):
    form = await request.form()
    key = form.get("name") or form.get("key") or ""
    if key != STREAM_KEY:
        return Response(status_code=403)
    return Response(status_code=200)

@app.post("/hooks/unpublish")
async def on_unpublish(request: Request):
    return Response(status_code=200)

@app.get("/watch", response_class=HTMLResponse)
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
        const src = `${location.protocol}//${location.hostname}/hls/mitchiscool123.m3u8`;
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