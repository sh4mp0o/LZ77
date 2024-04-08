def lz77_encode(text, window_size=10):
    encoded_text = []
    index = 0
    text_length = len(text)

    while index < text_length:
        max_length = 0
        max_length_offset = 0

        # Найти самое длинное совпадение в окне
        for i in range(1, min(window_size, index) + 1):
            substring = text[index:index + i]
            previous_occurrence = text.rfind(substring, 0, index)

            if previous_occurrence != -1:
                offset = index - previous_occurrence
                length = len(substring)

                if length > max_length:
                    max_length = length
                    max_length_offset = offset

        # Добавить код в закодированный текст
        if max_length > 0:
            encoded_text.append((max_length_offset, max_length, text[index + max_length]))
            index += max_length + 1
        else:
            encoded_text.append((0, 0, text[index]))
            index += 1

    return encoded_text

def lz77_decode(encoded_text):
    decoded_text = ""

    for (offset, length, char) in encoded_text:
        if length == 0:
            decoded_text += char
        else:
            start_index = len(decoded_text) - offset
            for i in range(start_index, start_index + length):
                decoded_text += decoded_text[i]
            decoded_text += char

    return decoded_text

if __name__ == "__main__":
    text = input("Введите текст для кодирования: ")

    encoded_text = lz77_encode(text)
    print("Закодированный текст:", encoded_text)

    decoded_text = lz77_decode(encoded_text)
    print("Декодированный текст:", decoded_text)

