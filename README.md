# Bilingual Video Caption Generator (GPU Accelerated)

Automatically generate bilingual captions (Chinese & English) from videos using OpenAI's Whisper with GPU acceleration. Captions are saved in SRT format, ready for Adobe Premiere Pro.

## 🚀 Features

- **GPU Acceleration** using CUDA & PyTorch
- Auto-detection of mixed-language (English & Chinese)
- Export subtitles in **SRT** format for Adobe Premiere Pro

## 🛠️ Requirements

Install Python dependencies:

```bash
git clone https://github.com/innovation64/bilingual-caption-generator.git
cd bilingual-caption-generator
pip install -r requirements.txt

```

## FFmpeg Installation:
Ensure ffmpeg is installed and available in your PATH:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS (Homebrew: https://brew.sh/)
brew install ffmpeg

# Windows (Chocolatey: https://chocolatey.org/)
choco install ffmpeg


```
### 🔥 Quick Start

Launch the caption generator:
```bash
python wishper.py

```
A web interface (Gradio) opens automatically. Upload a video to generate and download captions.

### ⚡ GPU Check (optional):
To verify GPU acceleration:

```bash
python -c "import torch; print(torch.cuda.is_available())"

```
Returns True if GPU is correctly configured.