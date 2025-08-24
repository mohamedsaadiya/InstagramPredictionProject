# File: run_pipeline.py

from download_video import download_tiktok_video
from feed_video import detect_activity

# Step 1: Download a TikTok video
video_path = download_tiktok_video(hashtag="dance", index=0)

# Step 2: Detect the activity
activity = detect_activity(video_path)
