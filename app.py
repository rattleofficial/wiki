import streamlit as sl
import wikipedia
sl.title('Rattle wiki')
inp=sl.text_input('Search about something:')
btn=sl.button('Search')

if btn:
    sl.header(wikipedia.summary(inp))
