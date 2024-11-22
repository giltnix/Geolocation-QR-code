import qrcode


def is_valid_coordinate(coordinate, min_val, max_val):
    """Проверяет, что координаты находятся в допустимом диапазоне."""
    try:
        value = float(coordinate)
        return min_val <= value <= max_val
    except ValueError:
        return False


def create_qr_code(latitude, longitude):
    """Создает QR-код с ссылкой на Google Maps для заданных координат."""
    # Формируем ссылку на Google Maps с координатами
    google_maps_url = f"https://www.google.com/maps/@{latitude},{longitude},15z"

    # Создаем QR-код
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(google_maps_url)
    qr.make(fit=True)

    print("\nВаш QR-код:")
    qr.print_ascii(invert=True)

    # Создаем изображение QR-кода
    img = qr.make_image(fill_color="pink", back_color="white")

    # Сохраняем изображение
    img_file_name = f"qr_code_{latitude}_{longitude}.png"

    try:
        img.save(img_file_name)
        print(f"QR-код сохранен как {img_file_name}")
    except Exception as e:
        print(f"Ошибка при сохранении изображения: {e}")


def main():
    print("Создание QR-кода с геолокацией")

    # Запрашиваем у пользователя координаты
    latitude = input("Введите широту: ")
    longitude = input("Введите долготу: ")

    # Проверяем допустимость координат
    if not is_valid_coordinate(latitude, -90, 90):
        print("Ошибка: широта должна быть в пределах от -90 до 90.")
        return
    if not is_valid_coordinate(longitude, -180, 180):
        print("Ошибка: долгота должна быть в пределах от -180 до 180.")
        return

    try:
        # Преобразуем введенные значения в float
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        print("Ошибка: координаты должны быть числовыми значениями.")
        return

    create_qr_code(latitude, longitude)


if __name__ == "__main__":
    main()
