from TikTokApi import TikTokApi
import asyncio
import os

# 1) Configuration
ms_token      = os.environ.get("ms_token", "YOUR_MS_TOKEN_HERE")
DOWNLOAD_DIR  = "downloads"

async def trending_videos():
    # ensure our download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    async with TikTokApi() as api:
        # 2) create session
        await api.create_sessions(
            ms_tokens=[ms_token],
            num_sessions=1,
            sleep_after=3,
            browser=os.getenv("TIKTOK_BROWSER", "chromium"),
            headless=False  # helps avoid empty responses
        )

        # 3) iterate trending videos
        async for video in api.trending.videos(count=10):
            data     = video.as_dict
            username = data['author']['uniqueId']
            video_id = data['id']
            watch_url = f"https://www.tiktok.com/@{username}/video/{video_id}"
            print(f"▶ Trending: {watch_url}")

            # seed a Video object
            t = api.video(url=watch_url)

            # 4) load metadata
            await t.info()

            # 5) download and write to unique file
            print("   • downloading …")
            video_bytes = await t.bytes()
            out_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp4")
            with open(out_path, "wb") as f:
                f.write(video_bytes)
            print("     ✓ saved to", out_path)

if __name__ == "__main__":
    asyncio.run(trending_videos())