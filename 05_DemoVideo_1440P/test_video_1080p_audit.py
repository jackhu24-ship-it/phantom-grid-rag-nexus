# -*- coding: utf-8 -*-
"""
PHANToM Grid :: AMD AI League Match 3 (RAG) 1080P Demo Video Audit Test
Drawer: 05_方案B演示影片_DemoVideo_1440P / test_video_1080p_audit.py
Standard: Rule 59 Sentence-Level Phase-Locked Sync & 1080P Full HD Spec
"""

import os
import sys
import json
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
WORKSPACE_ROOT = PROJECT_ROOT.parent.parent

VIDEO_LOCAL = CURRENT_DIR / "PHANTOM_GRID_AMD_AI_Demo_1080P.mp4"
VIDEO_GDRIVE = Path(r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202610_AMD_AI_League_Match3_RAG\05_方案B演示影片_DemoVideo_1440P\PHANTOM_GRID_AMD_AI_Demo_1080P.mp4")

def test_video_file_exists():
    assert VIDEO_LOCAL.exists() or VIDEO_GDRIVE.exists(), "Demo video MP4 file must exist locally or on G-Drive!"

def test_video_resolution_and_streams():
    target = VIDEO_LOCAL if VIDEO_LOCAL.exists() else VIDEO_GDRIVE
    cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", str(target)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert res.returncode == 0, f"ffprobe failed: {res.stderr}"

    data = json.loads(res.stdout)
    streams = data.get("streams", [])
    video_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)

    assert video_stream is not None, "Video stream missing!"
    assert audio_stream is not None, "Audio stream missing!"

    width = int(video_stream.get("width", 0))
    height = int(video_stream.get("height", 0))
    assert width == 1920, f"Width must be 1920 (got {width})"
    assert height == 1080, f"Height must be 1080 (got {height})"

def test_video_duration():
    target = VIDEO_LOCAL if VIDEO_LOCAL.exists() else VIDEO_GDRIVE
    cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", str(target)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert res.returncode == 0

    data = json.loads(res.stdout)
    duration = float(data["format"]["duration"])
    # Duration must be within 60s to 150s
    assert 60.0 <= duration <= 150.0, f"Duration {duration:.2f}s is out of bounds (60s-150s)"

def test_video_file_size():
    target = VIDEO_LOCAL if VIDEO_LOCAL.exists() else VIDEO_GDRIVE
    size_mb = target.stat().st_size / (1024 * 1024)
    # File size should be reasonable: > 1.0 MB and < 50.0 MB
    assert 1.0 <= size_mb <= 50.0, f"Video size {size_mb:.2f} MB is unexpected"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "-s", __file__])
