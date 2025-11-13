import os
import tempfile
import shutil
import pytest
from file_organizer import (
    determine_destination_path,
    remove_copied_files,
    classify_and_copy_files,
)

# --- 1. determine_destination_path ---
def test_determine_destination_path_images(tmp_path):
    result = determine_destination_path(".jpg", str(tmp_path))
    assert result.endswith("Images")

def test_determine_destination_path_documents(tmp_path):
    result = determine_destination_path(".pdf", str(tmp_path))
    assert result.endswith("Documents")

def test_determine_destination_path_videos(tmp_path):
    result = determine_destination_path(".mp4", str(tmp_path))
    assert result.endswith("Videos")

def test_determine_destination_path_other(tmp_path):
    result = determine_destination_path(".zip", str(tmp_path))
    assert result.endswith("Other")


# --- 2. remove_copied_files ---
def test_remove_copied_files_removes_files(tmp_path):
    # Create a fake file
    f1 = tmp_path / "file1.txt"
    f1.write_text("data")
    copied_files = [str(f1)]
    from file_organizer import remove_copied_files
    remove_copied_files(copied_files, str(tmp_path))
    assert not f1.exists()


# --- 3. classify_and_copy_files ---
def test_classify_and_copy_files(tmp_path):
    # Prepare source & destination
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    src.mkdir()
    dst.mkdir()

    # Create test files
    (src / "photo.jpg").write_text("img")
    (src / "doc.pdf").write_text("pdf")

    # Mock tkinter widgets
    class DummyLabel:
        def config(self, **kwargs): self.last_config = kwargs
    class DummyBar(dict):
        def __setitem__(self, k, v): super().__setitem__(k, v)
    class DummyRoot:
        def update_idletasks(self): pass

    label = DummyLabel()
    bar = DummyBar()
    root = DummyRoot()

    # Run the classification
    classify_and_copy_files(str(src), str(dst), label, bar, root)

    # Check results
    assert (dst / "Images" / "photo.jpg").exists()
    assert (dst / "Documents" / "doc.pdf").exists()
    assert "Success" in label.last_config["text"]


# --- 4. browse_button ---
def test_browse_button(monkeypatch):
    """Simulate selecting a folder without opening a GUI."""
    from file_organizer import browse_button
    selected = "/fake/path"
    monkeypatch.setattr("tkinter.filedialog.askdirectory", lambda: selected)

    import tkinter as tk
    var = tk.StringVar()
    browse_button(var)
    assert var.get() == selected
