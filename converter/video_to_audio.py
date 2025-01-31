import os
from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_path, output_path):
    """Extracts audio from a video file and saves it as an MP3."""
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"File not found: {video_path}")
        
        clip = VideoFileClip(video_path)
        audio_path = os.path.join(output_path, os.path.splitext(os.path.basename(video_path))[0] + ".mp3")
        clip.audio.write_audiofile(audio_path)
        clip.close()
        return audio_path
    except Exception as e:
        return f"Error: {str(e)}"