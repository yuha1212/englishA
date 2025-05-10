import streamlit as st
import fitz  # PyMuPDF
import random
from PIL import Image
import io

# 初期設定
pdf_path = "englisha_until4.pdf"
doc = fitz.open(pdf_path)
valid_pages = [i for i in range(0, len(doc) - 1, 2)]  # 奇数インデックスページのみ

# セッション状態の初期化
if "mode" not in st.session_state:
    st.session_state.mode = "odd"
    st.session_state.current = None

# タイトル
st.markdown("## 📘 英語A単語特訓")

# ページ表示関数
def get_image(page_num):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    return img

# ボタンを押した時の処理
if st.button("push"):
    if st.session_state.mode == "odd":
        page = random.choice(valid_pages)
        st.session_state.current = page
        st.session_state.mode = "even"
    else:
        page = st.session_state.current + 1
        st.session_state.mode = "odd"

    # ページ表示
    if page < len(doc):
        st.image(get_image(page), caption=f"{page+1}ページ", use_container_width=True)
    else:
        st.warning("次のページが存在しません。")
