import whisper

# Cargar el modelo prueba
# Opciones de modelo: "tiny", "base", "small", "medium", "large"
# - tiny/base  -> rápidos pero menos precisos
# - small      -> buena calidad y razonable en CPU (recomendado para ti)
# - medium     -> más preciso pero tarda mucho más
model = whisper.load_model("small")

# Ruta del archivo de audio/vídeo de la reunión (cámbiala a lo tuyo)
archivo_audio = r"C:\Users\TP647EP\Videos\2026-01-27 11-33-12.mp4"

# Transcribir (forzamos español; si en la call hay inglés también, podemos quitar language)
resultado = model.transcribe(archivo_audio, language="Spanish")

# Guardar la transcripción en un .txt 
ruta_salida = r"C:\Users\TP647EP\Downloads\Sandbox.txt"

with open(ruta_salida, "w", encoding="utf-8") as f:
    f.write(resultado["text"])

print("✅ Transcripción completada")
print("Fichero guardado en:", ruta_salida)
