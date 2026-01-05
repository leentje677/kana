import customtkinter as ctk
import random

# 1. THE DATA
MODES = {
    "Gojūon (Hiragana)": {
        "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
        "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
        "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
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
    },
    "Katakana Basic": {
        "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
        "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
        "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
        "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
        "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
        "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
        "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
        "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
        "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
        "ワ": "wa", "ヲ": "wo", "ン": "n"
    },
    "Katakana Dakuon": {
        "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
        "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ぞ": "zo",
        "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do",
        "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
        "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po"
    },
    "Katakana Yōon": {
        "キャ": "kya", "キュ": "kyu", "キョ": "kyo",
        "シャ": "sha", "シュ": "shu", "ショ": "sho",
        "チャ": "cha", "チュ": "chu", "ちょ": "cho",
        "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo",
        "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo",
        "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
        "リャ": "rya", "リュ": "ryu", "リョ": "ryo",
        "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo",
        "ジャ": "ja", "ジュ": "ju", "ジョ": "jo",
        "ビャ": "bya", "ビュ": "byu", "ビョ": "byo",
        "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo"
    }
}

# Auto-generate Mixed mode
ALL_MODES_DICT = {}
for m_data in MODES.values():
    ALL_MODES_DICT.update(m_data)
MODES["Mixed / All"] = ALL_MODES_DICT

COLORS = {
    "bg": "#FFFFFF",
    "text": "#4B4B4B",
    "primary": "#58CC02",
    "secondary": "#1CB0F6",
    "wrong": "#FF4B4B",
    "hint": "#AFAFAF",
    "entry_bg": "#F7F7F7",
    "progress_bg": "#E5E5E5"
}

ctk.set_appearance_mode("light")

class HiraganaQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
    
        self.title("Japanese Kana Practice")
        self.geometry("400x800")
        self.configure(fg_color=COLORS["bg"])

        # State Variables
        self.wrong_answers = set()
        self.endless_var = ctk.BooleanVar(value=False)
        self._is_processing = False
        self.total_correct = 0
        self.total_attempts = 0

        # --- Top Menu Area ---
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(pady=(20, 10), fill="x", padx=20)

        self.mode_menu = ctk.CTkOptionMenu(
            self.menu_frame, 
            values=list(MODES.keys()), 
            command=self.change_mode,
            fg_color=COLORS["secondary"],
            button_color=COLORS["secondary"]
        )
        self.mode_menu.set("Gojūon (Hiragana)")
        self.mode_menu.pack(side="left")

        self.endless_switch = ctk.CTkSwitch(
            self.menu_frame, 
            text="Endless", 
            variable=self.endless_var,
            progress_color=COLORS["primary"],
            command=self.reset_session
        )
        self.endless_switch.pack(side="right")

        # --- Progress Bar ---
        self.progress_bar = ctk.CTkProgressBar(
            self, 
            width=300, 
            height=12, 
            fg_color=COLORS["progress_bg"],
            progress_color=COLORS["primary"]
        )
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # --- Main Quiz UI ---
        self.label_title = ctk.CTkLabel(
            self, 
            text="What is this character?", 
            font=("Arial", 20, "bold"), 
            text_color=COLORS["text"]
        )
        self.label_title.pack(pady=(20, 5))

        self.char_display = ctk.CTkLabel(
            self, 
            text="", 
            font=("Arial", 120, "bold"), 
            text_color=COLORS["primary"]
        )
        self.char_display.pack(pady=20)

        self.entry = ctk.CTkEntry(
            self, 
            placeholder_text="Type romaji...", 
            width=250, height=55, 
            font=("Arial", 20),
            corner_radius=15,
            fg_color=COLORS["entry_bg"],
            text_color=COLORS["text"],
            justify="center",
            border_width=2
        )
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_answer())

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20)

        self.btn_check = ctk.CTkButton(
            self.button_frame, 
            text="CHECK", 
            command=self.check_answer, 
            fg_color=COLORS["primary"], 
            width=120, height=45,
            font=("Arial", 16, "bold")
        )
        self.btn_check.grid(row=0, column=0, padx=10)

        self.btn_hint = ctk.CTkButton(
            self.button_frame, 
            text="HINT", 
            command=self.give_hint, 
            fg_color="#E5E5E5", text_color="#AFAFAF",
            width=100, height=45,
            font=("Arial", 16, "bold")
        )
        self.btn_hint.grid(row=0, column=1, padx=10)

        self.result_text = ctk.CTkLabel(self, text="", font=("Arial", 18, "bold"), wraplength=350)
        self.result_text.pack(pady=10)

        # --- Bottom Stats ---
        self.score_label = ctk.CTkLabel(self, text="Accuracy: 0%", font=("Arial", 14), text_color=COLORS["hint"])
        self.score_label.pack(side="bottom", pady=(0, 10))
        
        self.stats_label = ctk.CTkLabel(self, text="", text_color=COLORS["hint"])
        self.stats_label.pack(side="bottom", pady=5)

        # Initialize
        self.reset_session()

    def reset_session(self):
        self.current_data = MODES[self.mode_menu.get()]
        self.chars_to_test = list(self.current_data.keys())
        self.total_in_deck = len(self.chars_to_test)
        random.shuffle(self.chars_to_test)
        self.wrong_answers.clear()
        self.total_correct = 0
        self.total_attempts = 0
        self.update_score()
        
        # Show UI elements if they were hidden
        self.label_title.pack(pady=(20, 5), after=self.progress_bar)
        self.char_display.pack(pady=20, after=self.label_title)
        self.entry.pack(pady=10, after=self.char_display)
        self.button_frame.pack(pady=20, after=self.entry)
        
        self.next_question()

    def change_mode(self, selected_mode):
        self.result_text.configure(text=f"Switched to {selected_mode}!", text_color=COLORS["secondary"])
        self.reset_session()

    def update_score(self):
        if self.total_attempts > 0:
            percentage = int((self.total_correct / self.total_attempts) * 100)
            self.score_label.configure(text=f"Accuracy: {percentage}%")
        else:
            self.score_label.configure(text="Accuracy: 0%")

    def give_hint(self):
        answer = self.current_data[self.current_char]
        actual_ans = answer[0] if isinstance(answer, list) else answer
        hint_letter = actual_ans[0]
        self.result_text.configure(text=f"Hint: Starts with '{hint_letter}'", text_color="#F89E1B")

    def next_question(self):
        self._is_processing = False
        
        if not self.chars_to_test:
            if self.endless_var.get():
                self.chars_to_test = list(self.current_data.keys())
                random.shuffle(self.chars_to_test)
            else:
                self.finish_quiz()
                return 

        self.current_char = self.chars_to_test.pop()
        self.char_display.configure(text=self.current_char)
        self.entry.delete(0, 'end')
        self.entry.focus()
        
        # Update Progress Bar & Text
        if self.endless_var.get():
            self.progress_bar.set(0)
            self.stats_label.configure(text="Endless Mode")
        else:
            remaining = len(self.chars_to_test) + 1
            progress_val = (self.total_in_deck - remaining) / self.total_in_deck
            self.progress_bar.set(progress_val)
            self.stats_label.configure(text=f"{remaining} characters left")

    def check_answer(self):
        if self._is_processing:
            return

        user_input = self.entry.get().lower().strip()
        if not user_input: return

        self.total_attempts += 1
        correct_answer = self.current_data[self.current_char]
        is_correct = user_input in correct_answer if isinstance(correct_answer, list) else user_input == correct_answer
        
        self._is_processing = True

        if is_correct:
            self.total_correct += 1
            self.result_text.configure(text="Correct! ✅", text_color=COLORS["primary"])
            self.after(600, self.next_question)
        else:
            display_ans = "/".join(correct_answer) if isinstance(correct_answer, list) else correct_answer
            self.result_text.configure(text=f"Incorrect: It was '{display_ans}'", text_color=COLORS["wrong"])
            self.wrong_answers.add(self.current_char) 
            self.chars_to_test.insert(0, self.current_char)
            self.after(1400, self.next_question)
        
        self.update_score()

    def finish_quiz(self):
        self.progress_bar.set(1)
        self.char_display.configure(text="🏁")
        self.label_title.pack_forget() 
        self.entry.pack_forget()
        self.button_frame.pack_forget()
        
        acc = int((self.total_correct / self.total_attempts) * 100) if self.total_attempts > 0 else 0
        result_msg = f"Session Complete!\nAccuracy: {acc}%"
        
        if self.wrong_answers:
            result_msg += f"\n\nReview these:\n{', '.join(list(self.wrong_answers)[:10])}..."
            
        self.result_text.configure(text=result_msg, text_color=COLORS["secondary"])

if __name__ == "__main__":
    app = HiraganaQuizApp()
    app.mainloop()