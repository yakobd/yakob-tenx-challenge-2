#!/usr/bin/env python3
"""Create a simple test video for FFmpeg demonstration."""

import subprocess
import sys
from pathlib import Path

def create_test_video():
    """Create a simple test video using FFmpeg if available."""
    output_path = Path("exports/test_video.mp4")
    output_path.parent.mkdir(exist_ok=True)
    
    # Try to create a simple test video with FFmpeg
    try:
        # Create a 5-second test video with moving text
        cmd = [
            "ffmpeg", "-y",  # -y to overwrite
            "-f", "lavfi",
            "-i", "testsrc=duration=5:size=640x480:rate=30",
            "-f", "lavfi", 
            "-i", "sine=frequency=1000:duration=5",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-shortest",
            str(output_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Test video created: {output_path}")
            return True
        else:
            print(f"❌ FFmpeg failed: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ FFmpeg not found in PATH")
        return False

if __name__ == "__main__":
    create_test_video()