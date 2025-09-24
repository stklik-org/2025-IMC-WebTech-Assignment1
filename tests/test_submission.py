
from pathlib import Path
import os
import re
import pytest


@pytest.mark.parametrize("filename", [
    "index.html",
    "about.html",
    "cv.html",
    "gallery.html",
    "contact.html",
    "style.css",
    "Documentation.pdf",
    "images/",
    "css/",
])
def test_all_files_exist(filename):
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"


