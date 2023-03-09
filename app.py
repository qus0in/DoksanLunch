import streamlit as st
import requests
st.write("# 6300원의 행복")

col1, col2 = st.columns(2)

col1.write("## The 좋은밥상")
url = "https://pf-wapi.kakao.com/web/profiles/_xfWxfCxj/posts"
req = requests.get(url)
json = req.json()
# col1.write(json['items'][0]['id'])
id = json['items'][0]['id']
req = requests.get(f"{url}/{id}")
json = req.json()
media = json["media"]
for m in media:
    col1.image(m['xlarge_url'])

col2.write("## 우림구내식당")