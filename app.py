import streamlit as st
import requests

def get_posts(id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts"
    req = requests.get(url)
    json = req.json()
    return json

def get_media(id, post_id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts/{post_id}"
    req = requests.get(url)
    json = req.json()
    media = json["media"]
    return media

def show_menus(col, store_id):
    posts = get_posts(store_id)
    post_ids = [p['id'] for p in posts['items']]
    for post_id in post_ids:
        media = get_media(store_id, post_id)
        for m in media:
            col.image(m['xlarge_url'])
    col.write(post_ids)

st.write("# 6300원의 행복")

col1, col2 = st.columns(2)

col1.write("## The 좋은밥상")
show_menus(col, "_xfWxfCxj")

col2.write("## 우림구내식당")
show_menus(co2, "_ixcNxexj")