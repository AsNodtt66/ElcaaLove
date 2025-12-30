import streamlit as st
import streamlit.components.v1 as components
import base64

# Konfigurasi halaman
st.set_page_config(page_title="💕Elsayanggg💕", layout="wide")

# Fungsi untuk memproses musik lokal agar bisa diputar
def get_audio_base64(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        return base64.b64encode(audio_bytes).decode()

# Load audio (Pastikan file MP3 berada di folder yang sama di GitHub)
try:
    audio_base64 = get_audio_base64("Still With You.mp3")
except:
    audio_base64 = ""

# Sembunyikan elemen standar Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px; max-width: 100%;}
    </style>
    """, unsafe_allow_html=True)

# Gabungan HTML terbaik
html_code = f"""
<!DOCTYPE html>
<html lang="id">
<head>
  <style>
    body {{ margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background: #000; overflow: hidden; font-family: 'Arial', sans-serif; position: relative; }}
    .night-sky {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, #0a0a1a 0%, #000 100%); z-index: 1; }}
    .night-sky::before {{ content: ''; position: absolute; width: 100%; height: 100%; background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><circle fill="%23fff" cx="50" cy="50" r="1"/><circle fill="%23fff" cx="150" cy="100" r="1"/><circle fill="%23fff" cx="550" cy="150" r="2"/><circle fill="%23fff" cx="250" cy="200" r="1"/><circle fill="%23fff" cx="450" cy="300" r="2"/><circle fill="%23fff" cx="100" cy="400" r="1"/><circle fill="%23fff" cx="400" cy="500" r="1"/><circle fill="%23fff" cx="300" cy="550" r="2"/></svg>') repeat; opacity: 0.5; animation: twinkle 5s infinite alternate; }}
    
    .heart-container {{ perspective: 1000px; z-index: 2; display: none; }}
    .heart-wrapper {{ position: relative; font-size: 1.2rem; white-space: nowrap; color: transparent; animation: rotateHeart 20s infinite linear; }}
    
    /* Menggunakan animasi Spiral 3D dari elcaaaa.html */
    @keyframes rotateHeart {{
        0% {{ transform: translateY(-100%) rotateZ(0deg) rotateX(0deg) rotateY(0deg); }}
        50% {{ transform: translateY(-100%) rotateZ(180deg) rotateX(45deg) rotateY(180deg); }}
        100% {{ transform: translateY(-100%) rotateZ(360deg) rotateX(0deg) rotateY(360deg); }}
    }}

    .love-word {{
      position: absolute; top: 50%; left: 50%; color: #ea80b0; letter-spacing: 2px;
      text-shadow: 0 0 10px #fff, 0 140px 0 #ea80b0, -20px 130px 0 #ea80b0, 20px 130px 0 #ea80b0, -40px 120px 0 #ea80b0, 40px 120px 0 #ea80b0, -70px 100px 0 #ea80b0, 70px 100px 0 #ea80b0, -100px 70px 0 #ea80b0, 100px 70px 0 #ea80b0, -130px 30px 0 #ea80b0, 130px 30px 0 #ea80b0, -140px -10px 0 #ea80b0, 140px -10px 0 #ea80b0, -140px -50px 0 #ea80b0, 140px -50px 0 #ea80b0, -120px -90px 0 #ea80b0, 120px -90px 0 #ea80b0, -90px -110px 0 #ea80b0, 90px -110px 0 #ea80b0, -50px -110px 0 #ea80b0, 50px -110px 0 #ea80b0, -20px -80px 0 #ea80b0, 20px -80px 0 #ea80b0, 0 -50px 0 #ea80b0;
      animation: glowPulse 4s infinite ease-in-out;
    }}

    #overlay {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 100; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #ea80b0; cursor: pointer; transition: 1s; }}
    #overlay h2 {{ border: 1px solid #ea80b0; padding: 15px 30px; border-radius: 30px; animation: pulse 2s infinite; }}
  </style>
</head>
<body>
  <div id="overlay" onclick="startEverything()">
    <h2>Klik untuk Elca 💕</h2>
  </div>

  <audio id="myAudio" loop>
    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
  </audio>

  <div class="night-sky"></div>
  <div class="heart-container" id="heartCont">
    <div class="heart-wrapper" id="heartWrapper"></div>
  </div>

  <script>
    function startEverything() {{
      document.getElementById('overlay').style.opacity = '0';
      setTimeout(() => {{ 
        document.getElementById('overlay').style.display = 'none'; 
        document.getElementById('heartCont').style.display = 'block';
      }}, 1000);
      
      var audio = document.getElementById("myAudio");
      audio.play();

      const wrapper = document.getElementById('heartWrapper');
      for (let i = 0; i < 25; i++) {{
        const span = document.createElement('span');
        span.className = 'love-word';
        span.textContent = 'I love you Elcaa💕';
        span.style.animationDelay = `${{i * 1.5}}s`;
        wrapper.appendChild(span);
      }}
    }}
  </script>
</body>
</html>
"""

components.html(html_code, height=1000)
