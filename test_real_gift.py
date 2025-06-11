import asyncio
from pyrogram import Client
from data.config import config, t
from app.purchase import buy_gift
from app.utils.logger import success, error


async def test_real_gift_send():
    """
    Тест для реального відправлення подарунка користувачу з конфігурації.
    Використовує реальні дані з config.ini
    """
    try:
        # Створюємо клієнт з даними з конфігурації
        app = Client(
            "gift_sender",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            phone_number=config.PHONE_NUMBER
        )

        # Запускаємо клієнт
        await app.start()
        
        try:
            # Отримуємо список доступних подарунків
            gifts = await app.get_available_gifts()
            
            if not gifts:
                error("Не знайдено доступних подарунків")
                return
            
            # Вибираємо перший доступний подарунок
            test_gift = gifts[0]
            gift_id = test_gift.id
            gift_price = test_gift.price
            
            success(f"Обрано подарунок: ID={gift_id}, Ціна={gift_price} ⭐")
            
            # Отримуємо ID користувача з конфігурації
            user_id = config.USER_ID[0]  # Беремо першого користувача зі списку
            
            success(f"Спроба відправлення подарунка користувачу: {user_id}")
            
            # Відправляємо подарунок
            await buy_gift(app, user_id, gift_id, quantity=1)
            
            success("Тест успішно завершено! Подарунок відправлено.")
            
        except Exception as e:
            error(f"Помилка під час тестування: {str(e)}")
        finally:
            # Зупиняємо клієнт
            await app.stop()
            
    except Exception as e:
        error(f"Помилка ініціалізації клієнта: {str(e)}")


if __name__ == "__main__":
    # Запускаємо тест
    asyncio.run(test_real_gift_send()) 