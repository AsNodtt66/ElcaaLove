import streamlit as st
import streamlit.components.v1 as components

# Mengatur konfigurasi halaman agar terlihat bersih
st.set_page_config(page_title="💕Elsayanggg💕", layout="wide")

# Trik CSS untuk menyembunyikan elemen bawaan Streamlit (Header, Footer, Menu)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding: 0px; max-width: 100%;}
            iframe {display: block; width: 100vw; height: 100vh; border: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Masukkan kode HTML lengkapmu di sini
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
  <style>
    body { margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background: #000; overflow: hidden; font-family: 'Arial', sans-serif; position: relative; }
    .night-sky { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, #0a0a1a 0%, #000 100%); z-index: 1; }
    .night-sky::before { content: ''; position: absolute; width: 100%; height: 100%; background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><circle fill="%23fff" cx="50" cy="50" r="1"/><circle fill="%23fff" cx="150" cy="100" r="1"/><circle fill="%23fff" cx="550" cy="150" r="2"/><circle fill="%23fff" cx="250" cy="200" r="1"/><circle fill="%23fff" cx="450" cy="300" r="2"/><circle fill="%23fff" cx="100" cy="400" r="1"/><circle fill="%23fff" cx="400" cy="500" r="1"/><circle fill="%23fff" cx="300" cy="550" r="2"/></svg>') repeat; opacity: 0.5; animation: twinkle 5s infinite alternate; }
    @keyframes twinkle { 0% { opacity: 0.3; } 100% { opacity: 0.8; } }
    .shooting-star { position: absolute; width: 2px; height: 2px; background: #fff; border-radius: 50%; box-shadow: 0 0 10px #ea80b0, 0 0 20px #ea80b0; animation: shoot 4s linear infinite; z-index: 1; opacity: 0; }
    @keyframes shoot { 0% { transform: translate(0, 0) rotate(45deg) scale(0); opacity: 1; } 100% { transform: translate(400px, 800px) rotate(45deg) scale(1.5); opacity: 0; } }
    .heart-container { perspective: 1000px; z-index: 2; display: none; }
    .heart-wrapper { position: relative; font-size: 1.2rem; white-space: nowrap; color: transparent; transform: translateY(-100%) rotateZ(-15deg); animation: rotateHeart 15s infinite linear; }
    .love-word { position: absolute; top: 50%; left: 50%; color: #ea80b0; letter-spacing: 2px;
      text-shadow: 0 0 10px #fff, 0 140px 0 #ea80b0, -20px 130px 0 #ea80b0, 20px 130px 0 #ea80b0, -40px 120px 0 #ea80b0, 40px 120px 0 #ea80b0, -70px 100px 0 #ea80b0, 70px 100px 0 #ea80b0, -100px 70px 0 #ea80b0, 100px 70px 0 #ea80b0, -130px 30px 0 #ea80b0, 130px 30px 0 #ea80b0, -140px -10px 0 #ea80b0, 140px -10px 0 #ea80b0, -140px -50px 0 #ea80b0, 140px -50px 0 #ea80b0, -120px -90px 0 #ea80b0, 120px -90px 0 #ea80b0, -90px -110px 0 #ea80b0, 90px -110px 0 #ea80b0, -50px -110px 0 #ea80b0, 50px -110px 0 #ea80b0, -20px -80px 0 #ea80b0, 20px -80px 0 #ea80b0, 0 -50px 0 #ea80b0;
      animation: glowPulse 4s infinite ease-in-out; }
    @keyframes rotateHeart { 0% { transform: translateY(-100%) rotateZ(-15deg) rotateX(0deg) rotateY(0deg); } 100% { transform: translateY(-100%) rotateZ(-15deg) rotateX(360deg) rotateY(360deg); } }
    @keyframes glowPulse { 0%, 100% { opacity: 0.8; filter: drop-shadow(0 0 5px #fff); } 50% { opacity: 1; filter: drop-shadow(0 0 20px #ea80b0); } }
    #overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 100; display: flex; flex-direction: column; justify-content: center; align-items: center; color: #ea80b0; cursor: pointer; transition: 1s; }
    #overlay h2 { border: 1px solid #ea80b0; padding: 15px 30px; border-radius: 30px; font-weight: 300; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(234, 128, 176, 0.7); } 70% { transform: scale(1.05); box-shadow: 0 0 0 20px rgba(234, 128, 176, 0); } 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(234, 128, 176, 0); } }
  </style>
</head>
<body>
  <div id="overlay" onclick="startEverything()">
    <h2>Klik untuk Elca 💕</h2>
    <p style="margin-top: 20px; font-size: 0.8rem; opacity: 0.6;">(Nyalakan Volume)</p>
  </div>
  <div class="night-sky"></div>
  <div class="shooting-star" style="left: 10%; animation-delay: 0s;"></div>
  <div class="shooting-star" style="left: 30%; animation-delay: 2s;"></div>
  <div class="shooting-star" style="left: 70%; animation-delay: 1s;"></div>
  <div class="shooting-star" style="left: 90%; animation-delay: 3s;"></div>
  <div class="heart-container" id="heartCont">
    <div class="heart-wrapper" id="heartWrapper"></div>
  </div>
  <div id="musicContainer"></div>
  <script>
    function startEverything() {
      document.getElementById('overlay').style.opacity = '0';
      setTimeout(() => { 
        document.getElementById('overlay').style.display = 'none'; 
        document.getElementById('heartCont').style.display = 'block';
      }, 1000);
      const musicDiv = document.getElementById('musicContainer');
      // Menggunakan YouTube Jungkook Still With You
      musicDiv.innerHTML = `<iframe width="0" height="0" src="https://www.youtube.com/embed/BksE6fAt348?autoplay=1" frameborder="0" allow="autoplay"></iframe>`;
      const wrapper = document.getElementById('heartWrapper');
      const numWords = 25; 
      for (let i = 0; i < numWords; i++) {
        const span = document.createElement('span');
        span.className = 'love-word';
        span.textContent = 'I love you Elcaa💕';
        span.style.animationDelay = `${i * 1.5}s`;
        wrapper.appendChild(span);
      }
    }
  </script>
</body>
</html>
"""

# Menampilkan HTML di Streamlit
components.html(html_code, height=1000)