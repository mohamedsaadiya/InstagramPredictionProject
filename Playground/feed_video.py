from TikTokApi import TikTokApi
import asyncio
import os

# You can set this directly for testing if not using environment variables
ms_token = os.environ.get("ms_token", "YOUR_MS_TOKEN_HERE")

async def get_video_example():
    async with TikTokApi() as api:
        # Create a browser session using WebKit (less detectable) and disable headless mode
        await api.create_sessions(
            ms_tokens=[ms_token],
            num_sessions=1,
            sleep_after=3,
            browser="webkit",
            headless=False  # Makes browser visible and reduces bot detection
            # proxy="http://user:pass@proxyserver:port"  # Optional: Add proxy if needed
        )

        video = api.video(
            url="https://www.tiktok.com/@therock/video/6829267836783971589"
        )

        print("\n🔍 Fetching related videos:")
        try:
            async for related_video in video.related_videos(count=10):
                print(related_video.as_dict)
        except Exception as e:
            print("⚠️ Failed to fetch related videos:", e)

        print("\n📄 Fetching video metadata:")
        try:
            video_info = await video.info()
            print(video_info)
        except Exception as e:
            print("⚠️ Failed to fetch video info:", e)

        print("\n💾 Downloading video file:")
        try:
            video_bytes = await video.bytes()
            with open("video.mp4", "wb") as f:
                f.write(video_bytes)
            print("✅ Video saved to 'video.mp4'")
        except Exception as e:
            print("⚠️ Failed to download video:", e)

if __name__ == "__main__":
    asyncio.run(get_video_example())
