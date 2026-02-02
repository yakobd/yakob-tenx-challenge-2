#!/usr/bin/env python3
"""Create a simple test video using moviepy (already installed)."""

def create_test_video():
    """Create a simple 5-second test video."""
    try:
        from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
        import numpy as np
        from pathlib import Path
        
        output_path = Path("exports/test_video.mp4")
        output_path.parent.mkdir(exist_ok=True)
        
        # Create a simple colored background
        clip = ColorClip(size=(640, 480), color=(50, 150, 50), duration=5)
        
        # Add some text
        txt_clip = TextClip("Test Video for FFmpeg Demo", 
                           fontsize=50, color='white', 
                           font='Arial-Bold').set_position('center').set_duration(5)
        
        # Composite the clips
        video = CompositeVideoClip([clip, txt_clip])
        
        # Write the video file
        video.write_videofile(str(output_path), fps=24, verbose=False, logger=None)
        
        print(f"✅ Test video created: {output_path}")
        return True
        
    except ImportError as e:
        print(f"❌ MoviePy import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Video creation failed: {e}")
        return False

if __name__ == "__main__":
    create_test_video()