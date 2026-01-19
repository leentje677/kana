const KATAKANA_DATA = {
 "Katakana Basic": {
    "ア": { romaji: ["a"] }, "イ": { romaji: ["i"] }, "ウ": { romaji: ["u"] }, "エ": { romaji: ["e"] }, "オ": { romaji: ["o"] },
    "カ": { romaji: ["ka"] }, "キ": { romaji: ["ki"] }, "ク": { romaji: ["ku"] }, "ケ": { romaji: ["ke"] }, "コ": { romaji: ["ko"] },
    "サ": { romaji: ["sa"] }, "シ": { romaji: ["shi"] }, "ス": { romaji: ["su"] }, "セ": { romaji: ["se"] }, "ソ": { romaji: ["so"] },
    "タ": { romaji: ["ta"] }, "チ": { romaji: ["chi"] }, "ツ": { romaji: ["tsu"] }, "テ": { romaji: ["te"] }, "ト": { romaji: ["to"] },
    "ナ": { romaji: ["na"] }, "ニ": { romaji: ["ni"] }, "ヌ": { romaji: ["nu"] }, "ネ": { romaji: ["ne"] }, "ノ": { romaji: ["no"] },
    "ハ": { romaji: ["ha"] }, "ヒ": { romaji: ["hi"] }, "フ": { romaji: ["fu"] }, "ヘ": { romaji: ["he"] }, "ホ": { romaji: ["ho"] },
    "マ": { romaji: ["ma"] }, "ミ": { romaji: ["mi"] }, "ム": { romaji: ["mu"] }, "メ": { romaji: ["me"] }, "モ": { romaji: ["mo"] },
    "ヤ": { romaji: ["ya"] }, "ユ": { romaji: ["yu"] }, "ヨ": { romaji: ["yo"] },
    "ラ": { romaji: ["ra"] }, "リ": { romaji: ["ri"] }, "ル": { romaji: ["ru"] }, "レ": { romaji: ["re"] }, "ロ": { romaji: ["ro"] },
    "ワ": { romaji: ["wa"] }, "ヲ": { romaji: ["wo"] }, "ン": { romaji: ["n"] }
  },

  "Katakana Dakuon": {
    "ガ": { romaji: ["ga"] }, "ギ": { romaji: ["gi"] }, "グ": { romaji: ["gu"] }, "ゲ": { romaji: ["ge"] }, "ゴ": { romaji: ["go"] },
    "ザ": { romaji: ["za"] }, "ジ": { romaji: ["ji"] }, "ズ": { romaji: ["zu"] }, "ゼ": { romaji: ["ze"] }, "ゾ": { romaji: ["zo"] },
    "ダ": { romaji: ["da"] }, "ヂ": { romaji: ["ji"] }, "ヅ": { romaji: ["zu"] }, "デ": { romaji: ["de"] }, "ド": { romaji: ["do"] },
    "バ": { romaji: ["ba"] }, "ビ": { romaji: ["bi"] }, "ブ": { romaji: ["bu"] }, "ベ": { romaji: ["be"] }, "ボ": { romaji: ["bo"] },
    "パ": { romaji: ["pa"] }, "ピ": { romaji: ["pi"] }, "プ": { romaji: ["pu"] }, "ペ": { romaji: ["pe"] }, "ポ": { romaji: ["po"] }
  },

  "Katakana Yōon": {
    "キャ": { romaji: ["kya"] }, "キュ": { romaji: ["kyu"] }, "キョ": { romaji: ["kyo"] },
    "シャ": { romaji: ["sha"] }, "シュ": { romaji: ["shu"] }, "ショ": { romaji: ["sho"] },
    "チャ": { romaji: ["cha"] }, "チュ": { romaji: ["chu"] }, "チョ": { romaji: ["cho"] },
    "ニャ": { romaji: ["nya"] }, "ニュ": { romaji: ["nyu"] }, "ニョ": { romaji: ["nyo"] },
    "ヒャ": { romaji: ["hya"] }, "ヒュ": { romaji: ["hyu"] }, "ヒョ": { romaji: ["hyo"] },
    "ミャ": { romaji: ["mya"] }, "ミュ": { romaji: ["myu"] }, "ミョ": { romaji: ["myo"] },
    "リャ": { romaji: ["rya"] }, "リュ": { romaji: ["ryu"] }, "リョ": { romaji: ["ryo"] },
    "ギャ": { romaji: ["gya"] }, "ギュ": { romaji: ["gyu"] }, "ギョ": { romaji: ["gyo"] },
    "ジャ": { romaji: ["ja"] }, "ジュ": { romaji: ["ju"] }, "ジョ": { romaji: ["jo"] },
    "ビャ": { romaji: ["bya"] }, "ビュ": { romaji: ["byu"] }, "ビョ": { romaji: ["byo"] },
    "ピャ": { romaji: ["pya"] }, "ピュ": { romaji: ["pyu"] }, "ピョ": { romaji: ["pyo"] }
  },
  
"Vocabulary (Katakana)": {
    // --- TECHNOLOGY & GADGETS (テクノロジー) ---
    "カメラ": { romaji: ["kamera"], meaning: "camera" },
    "テレビ": { romaji: ["terebi"], meaning: "TV" },
    "ラジオ": { romaji: ["rajio"], meaning: "radio" },
    "パソコン": { romaji: ["pasokon"], meaning: "PC/laptop" },
    "スマホ": { romaji: ["sumaho"], meaning: "smartphone" },
    "エアコン": { romaji: ["eakon"], meaning: "air conditioner" },
    "ビデオ": { romaji: ["bideo"], meaning: "video" },
    "リモコン": { romaji: ["rimokon"], meaning: "remote control" },
    "インターネット": { romaji: ["intaanetto"], meaning: "internet" },

    // --- FOOD & DRINK (たべもの・のみもの) ---
    "コーヒー": { romaji: ["ko-hi-", "koohi", "koohii", "kohi"], meaning: "coffee" },
    "コーラ": { romaji: ["ko-ra", "koora", "kora"], meaning: "cola" },
    "ビール": { romaji: ["bi-ru", "biiru", "biru"], meaning: "beer" },
    "ワイン": { romaji: ["wain"], meaning: "wine" },
    "パン": { romaji: ["pan"], meaning: "bread" },
    "ケーキ": { romaji: ["ke-ki", "keeki", "keki"], meaning: "cake" },
    "アイス": { romaji: ["aisu"], meaning: "ice cream" },
    "サラダ": { romaji: ["sarada"], meaning: "salad" },
    "チーズ": { romaji: ["chi-zu", "chiizu", "chizu"], meaning: "cheese" },
    "パスタ": { romaji: ["pasuta"], meaning: "pasta" },
    "メニュー": { romaji: ["menyu-", "menyuu", "menyu"], meaning: "menu" },
    "ジュース": { romaji: ["ju-su", "juusu", "jusu"], meaning: "juice" },
    "ハンバーグ": { romaji: ["hanba-gu"], meaning: "hamburger steak" },
    "ピザ": { romaji: ["piza"], meaning: "pizza" },
    "サンドイッチ": { romaji: ["sandoitchi"], meaning: "sandwich" },
    "チョコレート": { romaji: ["chokore-to"], meaning: "chocolate" },
    "カレー": { romaji: ["kare-"], meaning: "curry" },
    "スープ": { romaji: ["su-pu"], meaning: "soup" },

    // --- FRUITS & VEGETABLES (くだもの・やさい) ---
    "バナナ": { romaji: ["banana"], meaning: "banana" },
    "オレンジ": { romaji: ["orenji"], meaning: "orange" },
    "リンゴ": { romaji: ["ringo"], meaning: "apple (often katakana)" },
    "メロン": { romaji: ["meron"], meaning: "melon" },
    "パイナップル": { romaji: ["painappuru"], meaning: "pineapple" },
    "トマト": { romaji: ["tomato"], meaning: "tomato" },
    "キャベツ": { romaji: ["kyabetsu"], meaning: "cabbage" },
    "レタス": { romaji: ["retasu"], meaning: "lettuce" },

    // --- HOUSEHOLD & OBJECTS (いえ・もの) ---
    "ドア": { romaji: ["doa"], meaning: "door" },
    "ノート": { romaji: ["no-to", "nooto", "noto"], meaning: "notebook" },
    "ペン": { romaji: ["pen"], meaning: "pen" },
    "ボールペン": { romaji: ["bo-rupen", "boorupen"], meaning: "ballpoint pen" },
    "サンダル": { romaji: ["sandaru"], meaning: "sandals" },
    "ハンカチ": { romaji: ["hankachi"], meaning: "handkerchief" },
    "フォーク": { romaji: ["fo-ku", "fooku", "foku"], meaning: "fork" },
    "ナイフ": { romaji: ["naifu"], meaning: "knife" },
    "スプーン": { romaji: ["supu-n", "supuun", "supun"], meaning: "spoon" },
    "コップ": { romaji: ["koppu"], meaning: "glass/cup" },
    "キッチン": { romaji: ["kitchin"], meaning: "kitchen" },
    "ベッド": { romaji: ["beddo"], meaning: "bed" },
    "ソファ": { romaji: ["sofa"], meaning: "sofa" },
    "シャワー": { romaji: ["shawa-", "shawaa", "shawa"], meaning: "shower" },
    "カレンダー": { romaji: ["karenda-", "karendaa"], meaning: "calendar" },
    "テーブル": { romaji: ["te-buru"], meaning: "table" },
    "カーテン": { romaji: ["ka-ten"], meaning: "curtain" },
    "タンス": { romaji: ["tansu"], meaning: "chest of drawers" },
    "タオル": { romaji: ["taoru"], meaning: "towel" },
    "ブラシ": { romaji: ["burashi"], meaning: "brush" },

    // --- CLOTHING (ふく) ---
    "シャツ": { romaji: ["shatsu"], meaning: "shirt" },
    "ズボン": { romaji: ["zubon"], meaning: "pants" },
    "ネクタイ": { romaji: ["nekutai"], meaning: "necktie" },
    "スカート": { romaji: ["suka-to"], meaning: "skirt" },
    "コート": { romaji: ["ko-to"], meaning: "coat" },
    "セーター": { romaji: ["se-ta-"], meaning: "sweater" },
    "ドレス": { romaji: ["doresu"], meaning: "dress" },
    "ワンピース": { romaji: ["wanpi-su"], meaning: "one-piece dress" },

    // --- PLACES & BUILDINGS (ばしょ) ---
    "ホテル": { romaji: ["hoteru"], meaning: "hotel" },
    "トイレ": { romaji: ["toire"], meaning: "toilet/bathroom" },
    "ビル": { romaji: ["biru"], meaning: "building" },
    "レストラン": { romaji: ["resutoran"], meaning: "restaurant" },
    "デパート": { romaji: ["depa-to", "depaato", "depato"], meaning: "department store" },
    "エレベーター": { romaji: ["erebe-ta-", "erebeetaa"], meaning: "elevator" },
    "スーパー": { romaji: ["su-pa-"], meaning: "supermarket" },
    "コンビニ": { romaji: ["konbini"], meaning: "convenience store" },
    "プール": { romaji: ["pu-ru"], meaning: "pool" },
    "アパート": { romaji: ["apa-to"], meaning: "apartment" },

    // --- TRANSPORTATION (のりもの) ---
    "タクシー": { romaji: ["takushi-", "takushii", "takushi"], meaning: "taxi" },
    "バス": { romaji: ["basu"], meaning: "bus" },
    "トラック": { romaji: ["torakku"], meaning: "truck" },
    "オートバイ": { romaji: ["ootobai"], meaning: "motorcycle" },
    "エンジン": { romaji: ["enjin"], meaning: "engine" },

    // --- SPORTS & ARTS (スポーツ・げいじゅつ) ---
    "テニス": { romaji: ["tenisu"], meaning: "tennis" },
    "サッカー": { romaji: ["sakka-", "sakkaa", "sakka"], meaning: "soccer" },
    "ピアノ": { romaji: ["piano"], meaning: "piano" },
    "ギター": { romaji: ["gita-", "gitaa", "gita"], meaning: "guitar" },
    "スポーツ": { romaji: ["supo-tsu", "supootsu"], meaning: "sports" },
    "ダンス": { romaji: ["dansu"], meaning: "dance" },
    "ドラム": { romaji: ["doramu"], meaning: "drums" },
    "ゴルフ": { romaji: ["gorufu"], meaning: "golf" },
    "スキー": { romaji: ["suki-"], meaning: "skiing" },
    "ジャズ": { romaji: ["jazu"], meaning: "jazz" },

    // --- COUNTRIES & REGIONS (くに) ---
    "アメリカ": { romaji: ["amerika"], meaning: "USA" },
    "イギリス": { romaji: ["igirisu"], meaning: "UK" },
    "フランス": { romaji: ["furansu"], meaning: "France" },
    "ドイツ": { romaji: ["doitsu"], meaning: "Germany" },
    "イタリア": { romaji: ["itaria"], meaning: "Italy" },
    "スペイン": { romaji: ["supein"], meaning: "Spain" },
    "カナダ": { romaji: ["kanada"], meaning: "Canada" },
    "オーストラリア": { romaji: ["oosutoraria"], meaning: "Australia" },
    "ロシア": { romaji: ["roshia"], meaning: "Russia" },
    "アジア": { romaji: ["ajia"], meaning: "Asia" },
    "ヨーロッパ": { romaji: ["yo-roppa"], meaning: "Europe" },

    // --- OCCUPATIONS (しごと) ---
    "エンジニア": { romaji: ["enjinia"], meaning: "engineer" },
    "デザイナー": { romaji: ["dezaina-"], meaning: "designer" },
    "パイロット": { romaji: ["pairotto"], meaning: "pilot" },
    "サラリーマン": { romaji: ["sarari-man"], meaning: "office worker" },
    "モデル": { romaji: ["moderu"], meaning: "model" },

    // --- MISC (そのた) ---
    "ニュース": { romaji: ["nyu-su", "nyuusu", "nyusu"], meaning: "news" },
    "プレゼント": { romaji: ["purezento"], meaning: "present" },
    "クラス": { romaji: ["kurasu"], meaning: "class" },
    "チケット": { romaji: ["chiketto"], meaning: "ticket" },
    "ネコ": { romaji: ["neko"], meaning: "cat (often katakana)" },
    "ルール": { romaji: ["ru-ru"], meaning: "rule" },
    "チャンス": { romaji: ["chansu"], meaning: "chance" },
    "サービス": { romaji: ["sa-bisu"], meaning: "service" },
    "メッセージ": { romaji: ["messe-ji"], meaning: "message" },
    "ページ": { romaji: ["pe-ji"], meaning: "page" }
}
};