import streamlit as st
import plotly.figure_factory as ff
import numpy as np


# This code is different for each deployed app.
CURRENT_THEME = "light"
IS_DARK_THEME = False
EXPANDER_TEXT = """
    This is a custom theme. You can enable it by copying the following code
    to `.streamlit/config.toml`:

    ```python
    [theme]
    primaryColor = "#E694FF"
    backgroundColor = "#00172B"
    secondaryBackgroundColor = "#0083B8"
    textColor = "#C6CDD4"
    font = "sans-serif"
    ```
    """


# This code is the same for each deployed app.
st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/artist-palette_1f3a8.png",
    width=100,
)

"""
# Try out Theming!

Click on the images below to view this app with different themes. 
"""

""

THEMES = [
    "light",
    "dark",
    "green",
    "blue",
]
GITHUB_OWNER = "jrieke"

# Show thumbnails for available themes.
# As html img tags here, so we can add links on them.
cols = st.beta_columns(len(THEMES))
for col, theme in zip(cols, THEMES):

    # Get repo name for this theme (to link to correct deployed app)-
    if theme == "light":
        repo = "theming-showcase"
    else:
        repo = f"theming-showcase-{theme}"

    # Set border of current theme to red, otherwise black or white
    if theme == CURRENT_THEME:
        border_color = "red"
    else:
        border_color = "lightgrey" if IS_DARK_THEME else "black"

    col.markdown(
        f'<a href="https://share.streamlit.io/{GITHUB_OWNER}/{repo}/main"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a>',
        unsafe_allow_html=True,
    )


""

with st.beta_expander("How can I use this theme in my app?"):
    st.write(EXPANDER_TEXT)

""
""

# Draw some dummy content in main page and sidebar.
def draw_all(
    key,
    plot=False,
):
    st.write(
        """
        # Hi there!
        
        Look at all the cool colors I got now 👀 

        ```python
        streamlit = "cool"
        theming = "fantastic"
        both = "💥"
        ```
        """
    )

    st.checkbox("Do you like it?", key=key)
    st.radio("How much?", ["1 balloon 🎈", "2 balloons 🎈🎈", "3 balloons 🎈🎈🎈"], key=key)
    st.button("🤡 Click to show your love for theeemes", key=key)

    if plot:
        st.write("Oh look, a plot:")
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        hist_data = [x1, x2, x3]
        group_labels = ["Group 1", "Group 2", "Group 3"]

        fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

        st.plotly_chart(fig, use_container_width=True)

    st.slider(
        "From 10 to 11, how cool are themes?", min_value=10, max_value=11, key=key
    )
    # st.select_slider("Pick a number", [1, 2, 3], key=key)
    st.number_input("For exact people", key=key)
    st.text_input("Write your thoughts on theming down here...", key=key)
    st.text_area("...and here if you need more space", key=key)
    st.selectbox(
        "Pick your favorite", ["Streamlit", "Theming", "Baloooons 🎈 "], key=key
    )
    # st.multiselect("Pick a number", [1, 2, 3], key=key)
    st.file_uploader("Upload your fav theme here", key=key)
    st.color_picker("And pick your fav color here", key=key)
    with st.beta_expander("Expand me!"):
        st.write("Nothing to see here 👀 ")
    st.write("")
    st.write("That's our progress on theming:")
    st.progress(0.99)
    if plot:
        st.write("Still reading this?")
        st.json({"data": [1, 2, 3, 4]})
        st.dataframe({"data": [1, 2, 3, 4]})
        st.table({"data": [1, 2, 3, 4]})
        st.line_chart({"data": [1, 2, 3, 4]})
        # st.help(st.write)
    st.write("This is the end. Have fun building themes!")


draw_all("main", plot=True)

with st.sidebar:
    draw_all("sidebar")