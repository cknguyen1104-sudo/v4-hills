from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import os, webbrowser
class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, '.wasm':'application/wasm','.data':'application/octet-stream','.js':'application/javascript'}
    def end_headers(self):
        self.send_header('Cache-Control','no-store')
        super().end_headers()
if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    with ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(root))) as server:
        url = f'http://127.0.0.1:{server.server_port}/original/'
        print('Speed Stars native test: '+url,flush=True)
        print('Keep this window open while playing. Close it to stop the server.',flush=True)
        if not os.environ.get('SS_NO_BROWSER'): webbrowser.open(url)
        try: server.serve_forever()
        except KeyboardInterrupt: pass
