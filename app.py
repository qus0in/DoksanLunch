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

st.write("# 6300원의 행복")

col1, col2 = st.columns(2)

col1.write("## The 좋은밥상")
store1 = "_xfWxfCxj"
posts = get_posts(store1)
post_id = posts['items'][0]['id']
media = get_media(store1, post_id)
for m in media:
    col1.image(m['xlarge_url'])

col2.write("## 우림구내식당")
store2 = "_ixcNxexj"
posts = get_posts(store2)
post_ids = [p['id'] for p in posts['items']]
col2.write(post_ids)