import streamlit as st
import time

# ==============================
# GENERAL CONFIGURATION
# ==============================
st.set_page_config(page_title="EDA Sprint 1", layout="wide")

# Inject custom CSS for font size and readability
st.markdown("""
<style>
    html, body, [class*="css"]  {
        font-size: 18px !important;
    }
    .stCode pre {
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER SECTION
# ==============================
st.title("📊 Exploratory Data Analysis — Sprint 1")
st.markdown("""
Welcome to the interactive demonstration of the **Exploratory Data Analysis (EDA)**.  
Here you can see how we clean, transform, and summarize user data step by step.
""")

# Spinner with button activation
if st.button("🚀 Start Analysis"):
    with st.spinner("Loading environment..."):
        time.sleep(2)
    st.success("Environment loaded successfully ✅")

    # ==============================
    # STEP 1 — Cleaning user names
    # ==============================
    st.subheader("🧹 Step 1 — Cleaning user names")
    st.markdown("""
Let's implement the changes we identified. First, we need to fix the issues with the user_name variable. As we can see, it has unnecessary spaces and an underscore as a separator between the first and last name. Your goal is to remove the spaces and then replace the underscore with a space.
""")

    with st.expander("View code and result"):
        st.code("""
user_name = ' mike_reed '
user_name = user_name.strip()
user_name = user_name.replace('_', ' ')
print(user_name)
        """, language="python")
        user_name = ' mike_reed '
        user_name = user_name.strip()
        user_name = user_name.replace('_', ' ')
        st.success(f"Result: {user_name}")

    # ==============================
    # STEP 2 — Splitting the full name
    # ==============================
    st.subheader("✂️ Step 2 — Splitting the full name")
    st.markdown("""
Then, we should split the updated user_name variable into two substrings to obtain a list containing two values: one string for the first name and one string for the last name.
""")

    with st.expander("View code and result"):
        st.code("""
user_name_list = user_name.split(' ')
print(user_name_list)
        """, language="python")
        user_name_list = user_name.split(' ')
        st.success(f"Result: {user_name_list}")

    # ==============================
    # STEP 3 — Converting age to integer
    # ==============================
    st.subheader("🔢 Step 3 — Converting age to integer")
    st.markdown("""
Great! Now we should work with the user_age variable. As we mentioned before, this variable has an incorrect data type. Let’s fix this by converting its data type and displaying the final result.
""")

    with st.expander("View code and result"):
        st.code("""
user_age = 32.0
user_age = int(user_age)
print(user_age)
        """, language="python")
        user_age = 32.0
        user_age = int(user_age)
        st.success(f"Result: {user_age}")

    # ==============================
    # STEP 4 — Handling invalid age input
    # ==============================
    st.subheader("⚠️ Step 4 — Handling invalid age input")
    st.markdown("""
Step Five
As we know, data is not always perfect. We must consider cases where the user_age value can't be converted into an integer number. To prevent our system from crashing, we must take precautions in advance.

Write code that tries to convert the variable user_age to an integer and assign the converted value to the variable user_age_int. If the attempt fails, display a message asking the user to provide their age as a numerical value, with the message:

Please provide your age as a numerical value.
""")

    with st.expander("View code and result"):
        st.code("""
user_age = 'thirty two'
try:
    user_age_int = int(user_age)
except:
    print('Please provide your age as a numerical value.')
        """, language="python")
        user_age = 'thirty two'
        try:
            user_age_int = int(user_age)
            st.success(f"Result: {user_age_int}")
        except:
            st.error("Please provide your age as a numerical value.")

    # ==============================
    # STEP 5 — Calculating total amount spent
    # ==============================
    st.subheader("💰 Step 5 — Calculating total amount spent")
    st.markdown("""
We have information about our users' consumption habits, including the amount spent in each of their favorite categories.

The management is interested in knowing the total amount spent by each user.
Let's calculate this value and display it.
""")

    with st.expander("View code and result"):
        st.code("""
fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]
total_amount = sum(spendings_per_category)
print(total_amount)
        """, language="python")
        spendings_per_category = [894, 213, 173]
        total_amount = sum(spendings_per_category)
        st.metric("💰 Total Amount", f"{total_amount}")

    # ==============================
    # STEP 6 — Creating a formatted summary string
    # ==============================
    st.subheader("🧾 Step 6 — Creating a formatted summary string")
    st.markdown("""
The management enterprice asked us to think a way to summarize all the information from a user. Your goal is to create a formatted string that use user_id, user_name, user_age variables information
This is the final string what we want to create: "User 32415 is mike who is 32 years old".  

""")

    with st.expander("View code and result"):
        st.code("""
user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

final_string = f"User {user_id} is {user_name[0].capitalize()}, who is {user_age} years old."
print(final_string)
        """, language="python")
        user_id = '32415'
        user_name = ['mike', 'reed']
        user_age = 32
        final_string = f"User {user_id} is {user_name[0].capitalize()}, who is {user_age} years old."
        st.info(final_string)

    # ==============================
    # STEP 7 — Counting registered users
    # ==============================
    st.subheader("👥 Step 7 — Counting registered users")
    st.markdown("""
The management also wants an easy way to know the number of customers whose data we have.
Your goal is to create a formatted string that shows the total number of registered customers.
""")

    with st.expander("View code and result"):
        st.code("""
users = [
 ['32415', 'mike reed', 32.0],
 ['31980', 'kate morgan', 24.0],
 ['32156', 'john doe', 37.0],
]

user_info = f"We have received data from {len(users)} clients."
print(user_info)
        """, language="python")
        users = [
            ['32415', 'mike reed', 32.0],
            ['31980', 'kate morgan', 24.0],
            ['32156', 'john doe', 37.0],
        ]
        st.success(f"We have received data from {len(users)} clients.")

    # ==============================
    # STEP 8 — Processing and cleaning the user list
    # ==============================
    st.subheader("🧠 Step 8 — Processing and cleaning the user list")
    st.markdown("""
Let's now apply all the changes to the list of clients.
To simplify things, we'll give you a shorter one. You should:

Remove all leading and trailing spaces from the names, and also replace any underscores.
Convert all ages to integers.
Separate all first and last names into sublists.
Save the modified list as a new one called users_clean and display it on the screen.
""")

    with st.expander("View code and result"):
        st.code("""
users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', ' kate morgan ', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
]

users_clean = []
for user in users:
    name = user[1].strip().replace('_', ' ')
    name_split = name.split(' ')
    age = int(user[2])
    users_clean.append([user[0], name_split, age, user[3], user[4]])

print(users_clean)
        """, language="python")

        users = [
            ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
            ['31980', ' kate morgan ', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
            ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
        ]
        users_clean = []
        for user in users:
            name = user[1].strip().replace('_', ' ')
            name_split = name.split(' ')
            age = int(user[2])
            users_clean.append([user[0], name_split, age, user[3], user[4]])
        st.json(users_clean)

    # ==============================
    # FOOTER
    # ==============================
    st.divider()
    st.caption("Developed by **Luis Antonio López Marrón** — Interactive Version 1.0")

else:
    st.info("Click **Start Analysis** to begin the interactive demonstration.")