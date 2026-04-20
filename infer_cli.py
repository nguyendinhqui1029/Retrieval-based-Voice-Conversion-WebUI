import argparse
import soundfile as sf
import librosa

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", required=True)
    parser.add_argument("--model_name", required=True)
    parser.add_argument("--output_path", required=True)
    parser.add_argument("--pitch", type=int, default=0)

    args = parser.parse_args()

    print("👉 Fake voice clone (simple)...")

    # load audio
    y, sr = librosa.load(args.input_path, sr=None)

    # pitch shift (giả lập đổi giọng)
    if args.pitch != 0:
        y = librosa.effects.pitch_shift(y, sr=sr, n_steps=args.pitch)

    # save
    sf.write(args.output_path, y, sr)

    print(f"✅ Saved: {args.output_path}")

if __name__ == "__main__":
    main()