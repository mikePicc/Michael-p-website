from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='michael p', page_icon=":tada", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styling/style.css")

# -- page animation 
lottie_animation = load_lottieurl("https://lottie.host/d7913857-0613-4ea2-bfbb-970ca4bde555/RUrKszVUrN.json")
img_bone = Image.open("images/bone.JPG")
img_evolve = Image.open("images/evolve.jpeg")
 

# HEADER SECTION
with st.container():

    st.subheader("Hey there! :wave:")
    st.markdown("<h3 style='text-align: center; color: white;'>Now this is a story all about how my life got flipped turned upside down and I'd like to take a minute, just sit right there, I'll tell you how I became the King of a town called Altoona!</h1>", unsafe_allow_html=True)
    st.write("##")
    st.write("##")
    st.markdown("<h1 style='text-align: center; color:#fdb827;'>Welcome to the life of Michael P!</h1>", unsafe_allow_html=True)
    st.write("##")
    st.write("##")
    st.write("Based out of Oakland, CA and originally from Altoona, PA, I'm a recent grad from San Jose State Univeristy & current  employee! I was born with a basketball in my hands and I am a huge fan of the sport. My favorite team is the 76ers, and along with them, I root for the Pittsburgh Pirates, Penguins, & Steelers!")
    st.write("Other than being a sports fanatic, I love to endulge myself in philosophy, psychology, and theology!")


with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do!")
        st.write("##")
        st.write("• Graduated from SJSU in 2022, I majored in software engineering with a concentration in AI/ML. ")
        st.write("• Currently work for  in retail operations.")
        st.write("• Perfer to work with front-end development, human interface design, and user expereince design")
        st.write("• Previous work deals with full-stack development, database design and creation, and ML predictions using statistical probabilites.  ")
        st.write("##")
        st.markdown("""<a href="https://www.linkedin.com/in/michael-piccerillo/" style="color:#fdb827;">My LinkedIn</a>""", unsafe_allow_html=True,)
        st.markdown("""<a href="https://github.com/mikePicc/" style="color:#fdb827;">My GitHub</a>""", unsafe_allow_html=True,)
    with right_col:
        st_lottie(lottie_animation)

# ---- PROJECTS ----

with st.container():
    st.write("---")
    st.header("Sample Projects")
    st.write("##")
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(img_bone)

    with text_col:
        st.subheader("Integrate Lottie Animations Inside your Streamlit App")
        st.write(
             """
                Learn how to use Lottie Files in streamlit
                Animations make our web app more enaging and fun, and lottie files are the easiest way to do it
             """
       )
        st.markdown("""<a href="https://www.linkedin.com/company/evolvestartups/" style="color:#fdb827;">LinkedIn Page</a>""", unsafe_allow_html=True,)
        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(img_evolve)

    with text_col:
        st.subheader("Evolve")
        st.write("• Developed with the aim of helping students who were in a similar position as us, my other Co-cFounder and I made an internship-finding application for those with no industry experience.")
        st.write("• Reached out, presented to, and recruited hundreds of local small businesses and startups to join our platform.")
        st.write("• Main focus was centered on the full-stack development, utilizing Xcode for development and Google Firebase for the backend database.")
        st.write("• Within the first month of launch, our application had over 1,500 downloads and garnered attention from SJSU alumni as angel investors.")
        st.markdown("""<a href="https://www.linkedin.com/company/evolvestartups/" style="color:#fdb827;">LinkedIn Page</a>""", unsafe_allow_html=True,)



# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("Hit me up!")
    st.write("##")

    # Documentation: https://formsubmit.co/ /// change email address///
    contact_form = """
    <form action="https://formsubmit.co/piccerillomichael@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()
