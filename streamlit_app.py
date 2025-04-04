import streamlit as st

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title='Frog Clicker',
    page_icon="🐸",
    layout='centered'
)

# Custom CSS for animations and button styles
st.markdown("""
<style>
@keyframes click-animation {
    0% { transform: scale(1); opacity: 1; }
    100% { transform: scale(3); opacity: 0; }
}
.click-animation {
    position: absolute;
    animation: click-animation 0.8s ease-out;
    color: #008000;
    font-weight: bold;
    pointer-events: none;
}
/* Styles for the main button */
div[data-testid='stButton']:has(button:contains('🐸 Кликнуть')) button {
    font-size: 35px !important;
    padding: 25px 37px !important;
    border-radius: 15px !important;
    background: lightgrey !important;
}
</style>
""", unsafe_allow_html=True)

# Function to get Telegram user data from query parameters
def get_telegram_users():
    params = st.experimental_get_query_params()
    return {
        'name': params.get('name', [None])[0],
        'user_id': params.get('user_id', [None])[0],
        'auth_data': params.get('auth_data', [None])[0],
    }

# Initialize session state variables if not already set
if 'clicks' not in st.session_state:
    st.session_state.update({
        'clicks': 0,
        'animations': [],
        'last_click': None
    })

# Function to handle clicks
def handle_clicks():
    st.session_state['clicks'] += 1
    st.session_state['animations'].append(f'clicks-{st.session_state["clicks"]}')
    st.session_state['last_click'] = st.session_state['clicks']

# Get user data
user_data = get_telegram_users()

# Title of the app
st.title('Frog Clicker')

# User profile expander
with st.expander('Профиль пользователя', expanded=True):
    col_info = st.columns([1, 4])

    with col_info[0]:
        # Display a placeholder image (you can replace this with an actual image URL)
        st.image('https://lottiefiles.com/free-animation/click-effect-8BOCELCcjs', use_container_width=True)

# Button to click and increase the count
if st.button('🐸 Кликнуть'):
    handle_clicks()

# Display the number of clicks
st.write(f'Количество кликов: {st.session_state["clicks"]}')

# Display animations (if needed)
for animation in st.session_state['animations']:
    st.markdown(f'<div class="click-animation">{animation}</div>', unsafe_allow_html=True)