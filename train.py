import os
import shutil

INPUT_DIR = "../input"
MODEL_DIR = "../model"

os.makedirs(MODEL_DIR, exist_ok=True)

print("👉 Fake training model...")

# tìm file wav
wav_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".wav")]

if not wav_files:
    print("❌ Không tìm thấy voice.wav trong input/")
    exit()

# copy làm "model giả"
src = os.path.join(INPUT_DIR, wav_files[0])
dst = os.path.join(MODEL_DIR, "voice.pth")

shutil.copy(src, dst)

print("✅ Done: model/voice.pth")