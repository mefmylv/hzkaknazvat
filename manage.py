#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# import threading
# import schedule
# import time
# import datetime
# from apps.geekscoins.models import GeekcoinBalance

# def expire_and_update_coins():
#     current_date = datetime.now().date()

#     # Получаем список монет, у которых истек срок действия
#     coins_to_expire = GeekcoinBalance.objects.filter(expiration_date__lte=current_date)

#     # Обновляем статус монет и сохраняем изменения в базе данных
#     for coin in coins_to_expire:
#         coin.status = 'Expired'
#         coin.save()
# # Функция для запуска планировщика в отдельном потоке
#     def run_scheduler():
#         # Расписание выполнения задачи: каждый месяц в полночь первого числа
#         schedule.every().month.at('00:00').do(expire_and_update_coins)

#         # Бесконечный цикл для выполнения расписания
#         while True:
#             schedule.run_pending()
#             time.sleep(60)  # Проверка каждую минуту

#     # Создание и запуск потока
#     scheduler_thread = threading.Thread(target=run_scheduler)
#     scheduler_thread.start()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
