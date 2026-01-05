import streamlit as st
import random
import json
import os

# --- DATA PERSISTENCE ---
SCORE_FILE = "high_scores.json"

def load_high_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_high_score(mode, accuracy):
    scores = load_high_scores()
    # Only update if the new accuracy is higher than the previous record
    if mode not in scores or accuracy > scores[mode]:
        scores[mode] = accuracy
        with open(SCORE_FILE, "w") as f:
            json.dump(scores, f)

# --- THE DATA ---
MODES = {
    "Gojūon (Hiragana)": {
        "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
        "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
        "さ": "sa", "し": "shi", "す": "su", "せ": "see", "そ": "so",
        "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
        "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no", 
        "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
        "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
        "や": "ya", "ゆ": "yu", "よ": "yo",
        "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
        "わ": "wa", "を": ["wo", "o"], "ん": "n"
    },
    "Dakuon (Hiragana)": {
        "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
        "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
        "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
        "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
        "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"
    },
    "Yōon (Hiragana)": {
        "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo",
        "しゃ": "sha", "しゅ": "shu", "しょ": "sho",
        "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
        "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo",
        "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo",
        "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
        "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo",
        "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo",
        "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
        "びゃ": "bya", "びゅ": "byu", "びょ": "byo",
        "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo"
    }
}

# Auto-generate Mixed mode
ALL_MODES_DICT = {}
for m_data in MODES.values():
    ALL_MODES_DICT.update(m_data)
MODES["Mixed / All"] = ALL_MODES_DICT

# --- SESSION STATE ---
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.chars_to_test = []
    st.session_state.current_char = ""
    st.session_state.total_correct = 0
    st.session_state.total_attempts = 0
    st.session_state.wrong_answers = set()
    st.session_state.feedback = ""
    st.session_state.quiz_finished = False

def reset_session(mode_name):
    data = MODES[mode_name]
    st.session_state.chars_to_test = list(data.keys())
    random.shuffle(st.session_state.chars_to_test)
    st.session_state.total_correct = 0
    st.session_state.total_attempts = 0
    st.session_state.wrong_answers = set()
    st.session_state.quiz_finished = False
    next_question()

def next_question():
    if st.session_state.chars_to_test:
        st.session_state.current_char = st.session_state.chars_to_test.pop()
    else:
        st.session_state.quiz_finished = True

def check_answer():
    user_input = st.session_state.user_input.lower().strip()
    if not user_input: return

    correct_answer = MODES[st.session_state.mode_select][st.session_state.current_char]
    is_correct = user_input in correct_answer if isinstance(correct_answer, list) else user_input == correct_answer

    st.session_state.total_attempts += 1
    if is_correct:
        st.session_state.total_correct += 1
        st.session_state.feedback = "Correct! ✅"
    else:
        display_ans = "/".join(correct_answer) if isinstance(correct_answer, list) else correct_answer
        st.session_state.feedback = f"Incorrect: It was '{display_ans}' ❌"
        st.session_state.wrong_answers.add(st.session_state.current_char)
        st.session_state.chars_to_test.insert(0, st.session_state.current_char)
    
    st.session_state.user_input = "" # Clear input
    next_question()

# --- UI ---
st.set_page_config(page_title="Kana Mastery", layout="centered")

st.markdown("""
    <style>
    .big-char { font-size: 100px !important; font-weight: bold; color: #58CC02; text-align: center; margin: 20px 0; }
    </style>
    """, unsafe_allow_index=True)

# Sidebar for High Scores
with st.sidebar:
    st.header("🏆 Personal Bests")
    high_scores = load_high_scores()
    if high_scores:
        for mode, score in high_scores.items():
            st.write(f"**{mode}**: {score}%")
    else:
        st.write("No records yet. Finish a quiz!")

# Top Bar
col1, col2 = st.columns([2, 1])
with col1:
    mode = st.selectbox("Quiz Mode", list(MODES.keys()), key="mode_select", on_change=lambda: reset_session(st.session_state.mode_select))
with col2:
    endless = st.toggle("Endless Mode")

if not st.session_state.current_char and not st.session_state.quiz_finished:
    reset_session(mode)

# Progress
if not endless:
    total = len(MODES[mode])
    left = len(st.session_state.chars_to_test) + (1 if st.session_state.current_char else 0)
    st.progress((total - left) / total)
    st.caption(f"{left} remaining")

# Main Interface
if st.session_state.quiz_finished:
    st.header("Results 🏁")
    accuracy = int((st.session_state.total_correct / st.session_state.total_attempts) * 100) if st.session_state.total_attempts > 0 else 0
    st.metric("Your Accuracy", f"{accuracy}%")
    
    # Save the score
    save_high_score(mode, accuracy)
    
    if st.button("Try Again"):
        reset_session(mode)
        st.rerun()
else:
    st.markdown(f"<p class='big-char'>{st.session_state.current_char}</p>", unsafe_allow_index=True)
    st.text_input("Romanization", key="user_input", on_change=check_answer)
    
    if st.session_state.feedback:
        if "Correct" in st.session_state.feedback: st.success(st.session_state.feedback)
        else: st.error(st.session_state.feedback)

    # Hint Button
    if st.button("Need a Hint?"):
        ans = MODES[mode][st.session_state.current_char]
        char_hint = ans[0][0] if isinstance(ans, list) else ans[0]
        st.warning(f"It starts with: **{char_hint}**")
