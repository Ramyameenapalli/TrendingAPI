import pickle
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pprint


st.header("TRENDING")
u="https://github.com/trending"
r=requests.get(u,headers={'User-Agent': "Chrome/5.0"})
rc=r.status_code
if rc != 200:
    print("Error")

h=r.content
d=BeautifulSoup(h,"html.parser")
a = d.select('article.Box-row h1')
tr = []
linn=[]
for each_t in a:
    a1 = d.select('article.Box-row h1')
    tr = []
    linn = []
    for eachh_t in a1:
        hl = eachh_t.a.attrs["href"]
        n = hl[1:]
        n1=hl[2:]
        re = {"Repository": n.format(hl)}
        le={"Name": n,
            "Repository_link": "https://github.com{}".format(hl)}
        tr.append(re)
        linn.append(le)



movie_list = tr
yy= linn
#sm =st.markdown(movie_list.index.tolist())
sm = st.selectbox(
    "Type or select a repository from the dropdown",
    movie_list)


if st.button('Show Repository'):
    st.text(yy[0])
    st.text(yy[1])
    st.text(yy[2])
    st.text(yy[3])
    st.text(yy[4])
    st.text(yy[5])
    st.text(yy[6])
    st.text(yy[7])





if __name__=="__main__":
    print("Trending Github Repositories")
