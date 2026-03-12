import os
import subprocess
from urllib.parse import parse_qs, urlparse

from dotenv import load_dotenv

CONFIG_FILE_NAME = "config.env"
RERUN_KEY = "a"


def load_config() -> tuple[str, str]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(base_dir, CONFIG_FILE_NAME)
    adb_executable = os.path.join(base_dir, "platform-tools", "adb.exe")

    load_dotenv(dotenv_path)

    android_tv_ip = os.getenv("atv_ip")
    if not android_tv_ip:
        raise ValueError("Missing 'atv_ip' in config.env.")

    return adb_executable, android_tv_ip


def extract_youtube_watch_url(video_url: str) -> str:
    parsed_url = urlparse(video_url)
    query_params = parse_qs(parsed_url.query)

    video_id = query_params.get("v", [None])[0]
    if not video_id:
        raise ValueError("Invalid YouTube URL. Expected a URL containing a 'v' parameter.")

    return f"https://www.youtube.com/watch?v={video_id}"


def connect_to_device(adb_path: str, android_tv_ip: str) -> None:
    subprocess.run([adb_path, "connect", android_tv_ip], check=False)


def open_video_on_device(adb_path: str, video_url: str) -> None:
    subprocess.run(
        [
            adb_path,
            "shell",
            "am",
            "start",
            "-a",
            "android.intent.action.VIEW",
            "-d",
            video_url,
        ],
        check=False,
    )


def clear_console() -> None:
    subprocess.run("cls", shell=True, check=False)


def main() -> None:
    adb_path, android_tv_ip = load_config()
    subprocess.run("color 9", shell=True, check=False)

    is_connected = False
    should_repeat = True

    while should_repeat:
        print()

        if not is_connected:
            connect_to_device(adb_path, android_tv_ip)
            is_connected = True

        print("-------------------------------")
        raw_video_url = input("Enter YouTube Video URL: ").strip()

        try:
            final_url = extract_youtube_watch_url(raw_video_url)
        except ValueError as error:
            print(error)
        else:
            print("-------------------------------")
            open_video_on_device(adb_path, final_url)

        print("-------------------------------")
        print()
        should_repeat = input("Press A to rerun OR anything else to exit: ").strip().lower() == RERUN_KEY
        clear_console()


if __name__ == "__main__":
    main()
