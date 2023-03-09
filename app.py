import streamlit as st
import requests
from datetime import datetime
import pytz
from streamlit.components.v1 import html
API_KEY = st.secrets["KAKAO_API_KEY"]

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

def show_menus(store_id):
    posts = get_posts(store_id)
    post_ids = [p['id'] for p in posts['items']]
    images = []
    for post_id in post_ids:
        media = get_media(store_id, post_id)
        for m in media:
            images.append(m['xlarge_url'])
    cols = st.columns(min(3, len(images)))
    for i, col in enumerate(cols[:3]):
        col.image(images[i])

st.write("# 6300원의 행복")
now = datetime.now(pytz.timezone("Asia/Seoul"))
st.metric(
    label="현재일자",
    value=now.strftime("%Y-%m-%d"))
st.write("## The 좋은밥상")

code1 = """
    <style>
        #map {
            width: 500px;
            height: 400px;
        }
    </style>
    <div id="map"></div>
"""

code2 = f"""
    <script src="//dapi.kakao.com/v2/maps/sdk.js?appkey={API_KEY}"></script>
"""

code3 = """
    <script>
        var container = document.getElementById('map');
        var options = {
            center: new kakao.maps.LatLng(37.506502, 127.053617),
            level: 3
        };

        var map = new kakao.maps.Map(container, options);

        var markerPosition  = new kakao.maps.LatLng(37.506502, 127.053617);

        var marker = new kakao.maps.Marker({
            position: markerPosition
        });
        marker.setMap(map);
    </script>
"""

html(code1)
html(code2)
html(code3)

show_menus("_xfWxfCxj")
st.write("## 우림구내식당")
show_menus("_ixcNxexj")
