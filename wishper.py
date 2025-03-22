import gradio as gr
import whisper
import torch
import os
import datetime

# Load Whisper model optimized for GPU
model = whisper.load_model("medium").cuda() if torch.cuda.is_available() else whisper.load_model("medium")

# Function to convert transcription to SRT format
def transcription_to_srt(transcription):
    segments = transcription['segments']
    srt_content = ""

    for i, segment in enumerate(segments, start=1):
        start_time = str(datetime.timedelta(seconds=int(segment['start']))) + ",000"
        end_time = str(datetime.timedelta(seconds=int(segment['end']))) + ",000"
        text = segment['text'].strip()
        srt_content += f"{i}\n{start_time} --> {end_time}\n{text}\n\n"

    return srt_content

# Function to extract audio and transcribe
def generate_caption(video_path):
    audio_path = "extracted_audio.mp3"
    # Extract audio using ffmpeg
    os.system(f'ffmpeg -y -i "{video_path}" -ar 16000 -ac 1 -c:a mp3 {audio_path}')

    # Generate transcription with Whisper (auto-detect language)
    transcription = model.transcribe(audio_path, verbose=False)

    # Convert transcription to SRT format
    srt_caption = transcription_to_srt(transcription)

    srt_filename = "captions.srt"
    with open(srt_filename, "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_caption)

    return srt_filename

# Gradio UI setup
iface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Video(label="Upload Video"),
    outputs=gr.File(label="Download Caption (SRT)"),
    title="Bilingual Video Caption Generator (GPU Accelerated)",
    description="Upload a video and automatically generate captions as SRT files ready for Adobe Premiere."
)

iface.launch()
