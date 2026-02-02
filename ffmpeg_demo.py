#!/usr/bin/env python3
"""
FFmpeg Audio/Video Combination Demonstration

This script shows how to combine audio and video files using FFmpeg,
as required by the TRP1 challenge Part 4.
"""

import subprocess
from pathlib import Path

def combine_audio_video(audio_path, video_path, output_path):
    """
    Combine audio and video files using FFmpeg.
    
    Args:
        audio_path: Path to audio file (.wav, .mp3, etc.)
        video_path: Path to video file (.mp4, .avi, etc.)
        output_path: Path for combined output file
    """
    cmd = [
        "ffmpeg", "-y",  # -y to overwrite existing files
        "-i", str(video_path),  # Input video
        "-i", str(audio_path),  # Input audio
        "-c:v", "copy",         # Copy video codec (no re-encoding)
        "-c:a", "aac",          # Convert audio to AAC
        "-shortest",            # Stop when shortest stream ends
        str(output_path)        # Output file
    ]
    
    print(f"🎬 Combining audio and video...")
    print(f"   Audio: {audio_path}")
    print(f"   Video: {video_path}")
    print(f"   Output: {output_path}")
    print(f"   Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"✅ Successfully created: {output_path}")
            return True
        else:
            print(f"❌ FFmpeg failed:")
            print(f"   Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ FFmpeg timed out after 60 seconds")
        return False
    except FileNotFoundError:
        print("❌ FFmpeg not found in PATH")
        print("   Install with: winget install ffmpeg")
        return False

def main():
    """Demonstrate FFmpeg combination with existing audio files."""
    
    # Check available audio files
    exports_dir = Path("exports")
    audio_files = list(exports_dir.glob("*.wav")) + list(exports_dir.glob("*.mp3"))
    
    if not audio_files:
        print("❌ No audio files found in exports/")
        return
    
    print(f"📁 Found {len(audio_files)} audio file(s):")
    for audio in audio_files:
        print(f"   • {audio}")
    
    # For demonstration, we would combine with a video file
    # Since video generation failed, show the concept:
    
    audio_file = audio_files[0]  # Use first available audio
    video_file = Path("exports/test_video.mp4")  # Hypothetical video
    output_file = Path("exports/music_video_combined.mp4")
    
    print(f"\n🎯 FFmpeg Combination Command (from TRP1 challenge):")
    print(f"   ffmpeg -i {video_file} -i {audio_file} -c:v copy -c:a aac -shortest {output_file}")
    
    if video_file.exists():
        # If we had a video file, we would combine them
        success = combine_audio_video(audio_file, video_file, output_file)
        if success:
            print(f"🎉 Music video created successfully!")
    else:
        print(f"\n⚠️  Video file not available (video generation blocked by API)")
        print(f"   But the FFmpeg combination concept is demonstrated above.")

if __name__ == "__main__":
    main()