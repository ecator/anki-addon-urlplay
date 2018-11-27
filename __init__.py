import os
import requests
import hashlib
from anki.sound import play,mpvManager
from anki.utils import tmpdir,isWin
from aqt.reviewer import Reviewer

__version__ = "0.1.0"

def review_link_handler_wrapper(reviewer, url):
    """Play the sound or call the original link handler."""
    if url.startswith("urlplayhttp://") or url.startswith("urlplayhttps://"):
        if isWin:
            # download audio from url
            name = os.path.join(tmpdir(),hashlib.md5(url.encode(encoding="UTF-8")).hexdigest()+".mp3")
            if not os.path.exists(name):
                f = open(name, "wb")
                f.write(requests.get(url[7:]).content)
                f.close()
            # it wants unix paths, too!
            path = name.replace("\\", "/")
            play(path)
        else:
            # use mpv directly
            mpvManager.command("loadfile", url[7:], "append-play")
    else:
        original_review_link_handler(reviewer, url)

original_review_link_handler = Reviewer._linkHandler
Reviewer._linkHandler = review_link_handler_wrapper
