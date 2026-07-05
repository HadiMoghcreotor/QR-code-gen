import streamlit as st
import qrcode
from io import BytesIO

# ---------------- Settings ---------------- #
st.set_page_config(page_title="QR Code Generator", page_icon="📱")

# ---------------- UI Layout ---------------- #
st.title("Instant QR Code Generator")
st.write("Type in any link or text, and get a downloadable QR code instantly!")

data = st.text_input("Enter your link here:", placeholder="https://www...")

# ---------------- App Logic ---------------- #
if st.button("Generate QR Code"):
    if not data.strip():
        st.error("Please enter a link first!")
    else:
        # 1. Create the QR Code
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 2. Save it to virtual memory (so we don't have to deal with saving physical files)
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        # 3. Show the image on the website
        st.image(byte_im, caption="Your Custom QR Code")
        
        # 4. Give the user a button to download it
        st.download_button(
            label="💾 Download QR Code",
            data=byte_im,
            file_name="qr_code.png",
            mime="image/png"
        )