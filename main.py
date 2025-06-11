import asyncio
import traceback

from pyrogram import Client

from app.core.callbacks import new_callback
from app.notifications import send_start_message
from app.utils.detector import detector
from app.utils.logger import info, error
from data.config import config, t, get_language_display

async def main() -> None:
  

    async with Client(
            name=config.SESSION,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            phone_number=config.PHONE_NUMBER
    ) as client:
        await send_start_message(client)
        await detector(client, new_callback)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        info(t("console.terminated"))
    except Exception:
        error(t("console.unexpected_error"))
        traceback.print_exc()