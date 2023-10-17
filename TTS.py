from gtts import gTTS
import os
import time
import pygame

class TTS:
    def __init__(self, lang='es'):
        self.lang = lang
        pygame.init()

    def reproducir_elementos(self, elementos, delay):
        for elemento in elementos:
            tts = gTTS(text=elemento, lang=self.lang)
            audio_file = f"{elemento}.mp3"
            tts.save(audio_file)

            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            # Eliminar el archivo de audio si lo deseas
            os.remove(audio_file)

            time.sleep(delay)

# Ejemplo de uso
if __name__ == "__main__":
    tts = TTS()
    elementos = ["Hola", "Mundo", "como", "estas", "12124"]
    tts.reproducir_elementos(elementos, 1)  # 2 segundos de delay entre elementos
