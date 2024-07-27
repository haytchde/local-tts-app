Here's the reformatted content for a `README.md` file:

# Coqui TTS Web Application

This is a simple web application that utilizes Coqui TTS to convert text into speech using various voice models. The application allows users to select different voices and generate audio files from text input.

## Features

- Text-to-speech conversion using Coqui TTS
- Support for multiple voice models, including multi-speaker models
- User-friendly web interface for easy interaction
- Adjustable playback speed for generated audio

## Requirements

- Python 3.6 or higher
- [Coqui TTS](https://github.com/coqui-ai/TTS) installed in a virtual environment
- Flask for the web server
- Soundfile for audio file handling

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/haytchde/local-tts-app.git
   cd local-tts-app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv coqui_env
   source coqui_env/bin/activate  # On Windows use `coqui_env\Scripts\activate`
   ```

3. **Install required packages**:
   ```bash
   pip install TTS Flask flask-cors soundfile
   ```

4. **Install espeak (for macOS)**:
   ```bash
   brew install espeak
   ```

## Usage

1. **Run the TTS server**:
   ```bash
   python custom_tts_server.py
   ```

2. **Serve the web interface**:
   In a new terminal window (keeping the TTS server running), navigate to the project directory and run:
   ```bash
   python -m http.server 8000
   ```

3. **Access the web application**:
   Open your web browser and go to `http://localhost:8000`.

4. **Using the application**:
   - Enter the text you want to convert to speech in the textarea.
   - Select a voice from the dropdown menu.
   - Click the "Generate Speech" button to create the audio.
   - Use the audio player to listen to the generated speech and adjust playback speed as needed.

## Available Models

The application supports various TTS models. By default, it uses the following:
- LJSpeech Tacotron2: `tts_models/en/ljspeech/tacotron2-DDC`
- VCTK VITS Multi-Speaker: `tts_models/en/vctk/vits`

You can modify the models in the code as needed.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Coqui TTS for providing the TTS framework
- Flask for the web framework