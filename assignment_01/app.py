import streamlit as st

# Task 1: The UI Shell
st.title("🦸 Marvel Universe Recruiter")
st.write(
    "Welcome, future hero! Nick Fury is assembling the next generation of Avengers. "
    "Enter your details and prove you're ready for the mission. ⚡🛡️"
)

# Task 2: Multi-Data Collection
hero_name = st.text_input("🦸 What's your hero name?")
hero_power = st.text_input("💥 Describe your greatest superpower")

# Task 3: The Action Gate
if st.button("🚀 Join the Avengers"):

    # Task 4: Conditional Routing (Edge Cases)
    if hero_name == "":
        st.error("❌ S.H.I.E.L.D. cannot recruit an unknown hero. Please enter your hero name.")
    elif hero_power == "":
        st.warning("⚠️ Every Avenger needs a superpower. Tell us what makes you special!")
    else:

        # Simple Hero Assignment
        if "technology" in hero_power.lower() or "tech" in hero_power.lower():
            team = "Iron Man's Tech Division 🤖"
        elif "magic" in hero_power.lower():
            team = "Doctor Strange's Mystic Order 🔮"
        elif "strength" in hero_power.lower() or "strong" in hero_power.lower():
            team = "Hulk's Gamma Squad 💚"
        elif "speed" in hero_power.lower() or "fast" in hero_power.lower():
            team = "Quicksilver's Speed Force ⚡"
        else:
            team = "The Avengers Initiative 🛡️"

        # Task 5: Formatted Output
        st.success(
            f"🎉 Welcome, **{hero_name}**!\n\n"
            f"Nick Fury has analyzed your ability: **'{hero_power}'**.\n\n"
            f"🛡️ You have officially been assigned to **{team}**!"
        )

        st.balloons()

        # Advanced Challenge: Token Cost Estimator
        char_count = len(hero_power)
        token_count = char_count // 4

        st.info(
            f"📊 Mission Report:\n"
            f"Your power description contains **{char_count} characters**.\n"
            f"Estimated AI token usage: **{token_count} tokens**."
        )