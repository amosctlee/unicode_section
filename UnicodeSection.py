import typing
import inspect


class UnicodeSection:
    """
    Unicode區段
    https://zh.m.wikipedia.org/wiki/Unicode%E5%8D%80%E6%AE%B5
    """
    @staticmethod
    def show_letter_sample(funcname, limit=30):
        _instance = UnicodeSection()

        func = getattr(_instance, funcname)
        start = func()[0]
        end = func()[1]

        counter = 0
        for o in range(start, end + 1):
            counter += 1
            if limit != -1 and counter > limit:
                break
            print(chr(o), end=" ")

    @staticmethod
    def which_section(char):
        """
        判斷字元所在的Unicode區段
        """
        for name, func in inspect.getmembers(
            UnicodeSection(), predicate=inspect.ismethod
        ):
            if name not in ("_", "show_letter_sample", "which_section"):
                if func()[0] <= ord(char) <= func()[1]:
                    return name

        return f"{char} ({hex(ord(char))}) not in the sections we mentioned"

    def Basic_Latin(self):
        """
        基本拉丁文 (Unicode區段)
        基本拉丁字母
        """
        return ord("\u0020"), ord("\u007F")

    def Latin_1_Supplement(self):
        """
        Latin-1 Supplement (Unicode區段)
        拉丁字母補充-1
        """
        return ord("\u0080"), ord("\u00FF")

    def Latin_Extended_A(self):
        """
        Latin Extended-A (Unicode區段)
        拉丁字母擴展-A
        """
        return ord("\u0100"), ord("\u017F")

    def Latin_Extended_B(self):
        """
        Latin Extended-B (Unicode區段)
        拉丁字母擴展-B
        """
        return ord("\u0180"), ord("\u024F")

    def IPA_Extensions(self):
        """
        國際音標擴展
        """
        return ord("\u0250"), ord("\u02AF")

    def Spacing_Modifier_Letters(self):
        """
        佔位修飾符號
        """
        return ord("\u02B0"), ord("\u02FF")

    def Combining_Diacritical_Marks(self):
        """
        組合附加符號
        """
        return ord("\u0300"), ord("\u036F")

    def Greek_and_Coptic(self):
        """
        希臘字母及其它 (Unicode區段)
        """
        return ord("\u0370"), ord("\u03FF")

    def Cyrillic(self):
        """
        西里爾字母
        斯拉夫文
        """
        return ord("\u0400"), ord("\u04FF")

    def _():
        pass

    def General_Punctuation(self):
        """
        常用標點
        """
        return ord("\u2000"), ord("\u206F")

    def Letterlike_Symbols(self):
        """
        字母式符號
        """
        return ord("\u2100"), ord("\u214F")

    def Number_Forms(self):
        """
        數字形式
        """
        return ord("\u2150"), ord("\u218F")

    def Mathematical_Operators(self):
        """
        數學運算子
        """
        return ord("\u2200"), ord("\u22FF")

    def Enclosed_Alphanumerics(self):
        """
        帶圈字母和數字
        """
        return ord("\u2460"), ord("\u24FF")

    def Box_Drawing(self):
        """
        制表符
        """
        return ord("\u2500"), ord("\u257F")

    def Block_Elements(self):
        """
        方塊元素
        """
        return ord("\u2580"), ord("\u259F")

    def Geometric_Shapes(self):
        """
        幾何圖形
        """
        return ord("\u25A0"), ord("\u25FF")

    def Miscellaneous_Symbols(self):
        """
        雜項符號
        """
        return ord("\u2600"), ord("\u26FF")

    def CJK_Radicals_Supplement(self):
        """
        中日韓漢字部首補充
        """
        return ord("\u2E80"), ord("\u2EFF")

    def Kangxi_Radicals(self):
        """
        康熙部首
        """
        return ord("\u2F00"), ord("\u2FDF")

    def CJK_Symbols_and_Punctuation(self):
        """
        中日韓符號和標點
        """
        return ord("\u3000"), ord("\u303F")

    def Hiragana(self):
        """
        日文平假名
        """
        return ord("\u3040"), ord("\u309F")

    def Katakana(self):
        """
        片假名
        """
        return ord("\u30A0"), ord("\u30FF")

    def Bopomofo(self):
        """
        注音符號
        """
        return ord("\u3100"), ord("\u312F")

    def Hangul_Compatibility_Jamo(self):
        """
        諺文相容字母
        """
        return ord("\u3130"), ord("\u318F")

    def Kanbun(self):
        """
        漢文訓讀
        """
        return ord("\u3190"), ord("\u319F")

    def Bopomofo_Extended(self):
        """
        注音擴展
        """
        return ord("\u31A0"), ord("\u31BF")

    def CJK_Strokes(self):
        """
        中日韓筆畫
        """
        return ord("\u31C0"), ord("\u31EF")

    def Katakana_Phonetic_Extensions(self):
        """
        片假名語音擴展
        """
        return ord("\u31F0"), ord("\u31FF")

    def Enclosed_CJK_Letters_and_Months(self):
        """
        圍繞中日韓文字及月份
        """
        return ord("\u3200"), ord("\u32FF")

    def CJK_Compatibility(self):
        """
        中日韓相容字元
        """
        return ord("\u3300"), ord("\u33FF")

    def CJK_Unified_Ideographs_Extension_A(self):
        """
        中日韓統一表意文字擴展區A
        """
        return ord("\u3400"), ord("\u4DBF")

    def Yijing_Hexagram_Symbols(self):
        """
        易經六十四卦符號
        """
        return ord("\u4DC0"), ord("\u4DFF")

    def CJK_Unified_Ideographs(self):
        """
        中日韓統一表意文字
        """
        return ord("\u4E00"), ord("\u9FFF")

    def Yi_Syllables(self):
        """
        彝文音節
        """
        return ord("\uA000"), ord("\uA48F")

    def Yi_Radicals(self):
        """
        彝文部首
        """
        return ord("\uA490"), ord("\uA4CF")

    def Hangul_Syllables(self):
        """
        諺文音節
        韓文音節
        """
        return ord("\uAC00"), ord("\uD7AF")

    def Hangul_Jamo_Extended_B(self):
        """
        諺文字母擴展-B
        韓文擴展字母B
        """
        return ord("\uD7B0"), ord("\uD7FF")

    def CJK_Compatibility_Forms(self):
        """
        中日韓相容形式
        """
        return ord("\uFE30"), ord("\uFE4F")

    def Small_Form_Variants(self):
        """
        	小寫變體形式
        """
        return ord("\uFE50"), ord("\uFE6F")

    def CJK_Unified_Ideographs_Extension_B(self):
        """
        中日韓統一表意文字擴展區B
        """
        return 0x20000, 0x2A6DF

    def CJK_Unified_Ideographs_Extension_C(self):
        """
        中日韓統一表意文字擴展區C
        """
        return 0x2A700, 0x2B73F

    def CJK_Unified_Ideographs_Extension_D(self):
        """
        中日韓統一表意文字擴展區D
        """
        return 0x2B740, 0x2B81F

    def CJK_Unified_Ideographs_Extension_E(self):
        """
        中日韓統一表意文字擴展區E
        """
        return 0x2B820, 0x2CEAF

    def CJK_Unified_Ideographs_Extension_F(self):
        """
        中日韓統一表意文字擴展區F
        """
        return 0x2CEB0, 0x2EBEF

    def CJK_Compatibility_Ideographs_Supplement(self):
        """
        中日韓相容表意文字補充區
        """
        return 0x2F800, 0x2FA1F

    def CJK_Unified_Ideographs_Extension_G(self):
        """
        中日韓統一表意文字擴展區G
        """
        return 0x30000, 0x3134F

    def Halfwidth_and_Fullwidth_Forms(self):
        """
        半形及全形字
        """
        return 0xFF00, 0xFFEF

    def Private_Use_Area(self):
        """
        私用區
        """
        return 0xE000, 0xF8FF

    def Supplementary_Private_Use_Area_A(self):
        """
        	補充私人使用區-A
        """
        return 0xF0000, 0xFFFFF


class SentenceChecker:
    def __init__(self):
        # https://docs.python.org/3/howto/unicode.html
        self.unicode_section = UnicodeSection()

    def sentence_langs(self, sentence) -> typing.List[str]:
        langs = []
        for character in sentence:
            lang = self.character_lang(character)
            if lang == "unknown":
                print("unknown character:", character)
            langs.append(lang)

        langs = list(set(langs))
        if "unknown" in langs:
            raise Exception(
                f"There is unknown character in sentence: `{sentence}`"
            )

        return langs

    def character_lang(self, character) -> str:
        if self.chinese(character):
            return "chinese"

        if self.english(character):
            return "english"

        if self.number(character):
            return "number"

        if self.unprintable(character):
            return "unprintable"

        if self.identified_garbled(character):
            return "garbled"

        if self.symbol(character):
            return "symbol"

        if self.other_languages(character):
            return "other_languages"

        return "unknown"

    def _is_between(self, code, start_end: tuple):
        return start_end[0] <= code <= start_end[1]

    def chinese(self, char):
        code = ord(char)

        if self._is_between(code, self.unicode_section.Bopomofo()):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Compatibility_Ideographs_Supplement()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs_Extension_A()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs_Extension_B()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs_Extension_C()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs_Extension_D()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs_Extension_E()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.CJK_Unified_Ideographs_Extension_F()
        ):
            return True
        if self._is_between(code, self.unicode_section.Kangxi_Radicals()):
            return True

        return False

    def english(self, char):
        code = ord(char)

        # Basic Latin 包含標點、數字、英文大小寫
        if self._is_between(code, (ord('A'), ord('Z'))):
            return True
        if self._is_between(code, (ord('a'), ord('z'))):
            return True
        if self._is_between(code, (ord('Ａ'), ord('Ｚ'))):
            return True
        if self._is_between(code, (ord('ａ'), ord('ｚ'))):
            return True
        return False

    def number(self, char):
        code = ord(char)

        if self._is_between(code, (ord('0'), ord('9'))):
            return True
        if self._is_between(code, (ord('０'), ord('９'))):
            return True
        return False

    def unprintable(self, char):
        code = ord(char)
        if self._is_between(code, self.unicode_section.Private_Use_Area()):
            return True
        if self._is_between(
            code, self.unicode_section.Supplementary_Private_Use_Area_A()
        ):
            return True
        return False

    def identified_garbled(self, char):

        if char in "?■□◤�▲◥":
            return True
        return False

    def symbol(self, char):
        code = ord(char)

        section_ranges = [
            # Basic Latin 標點
            (0x0000, 0x002F),
            (0x003A, 0x0040),
            (0x005B, 0x0060),
            (0x007B, 0x007F),
            # 全形標點
            (0xFF01, 0xFF0F),
            (0xFF1A, 0xFF20),
            (0xFF3B, 0xFF40),
            (0xFF5B, 0xFF65),
            (0xFFE0, 0xFFEE),
            self.unicode_section.General_Punctuation(),
            self.unicode_section.Letterlike_Symbols(),
            self.unicode_section.Enclosed_Alphanumerics(),
            self.unicode_section.Number_Forms(),
            self.unicode_section.Mathematical_Operators(),
            self.unicode_section.Block_Elements(),
            self.unicode_section.Geometric_Shapes(),
            self.unicode_section.Box_Drawing(),
            self.unicode_section.Miscellaneous_Symbols(),
            self.unicode_section.Small_Form_Variants(),
            self.unicode_section.Bopomofo_Extended(),
            self.unicode_section.Latin_1_Supplement(),
            self.unicode_section.CJK_Compatibility_Forms(),
            self.unicode_section.CJK_Symbols_and_Punctuation(),
            self.unicode_section.Enclosed_CJK_Letters_and_Months(),
            self.unicode_section.Latin_1_Supplement(),
            self.unicode_section.Combining_Diacritical_Marks(),
            self.unicode_section.Spacing_Modifier_Letters(),
        ]
        for section_range in section_ranges:
            if self._is_between(code, section_range):
                return True

        return False

    def other_languages(self, char):
        code = ord(char)

        if self._is_between(code, (0x0066, 0x009F)):
            return True

        # 半形日文
        if self._is_between(code, (0xFF65, 0xFF9F)):
            return True

        # 斯拉夫
        if self._is_between(code, self.unicode_section.Cyrillic()):
            return True

        # 韓文
        if self._is_between(code, self.unicode_section.Hangul_Syllables()):
            return True
        if self._is_between(
            code, self.unicode_section.Hangul_Jamo_Extended_B()
        ):
            return True
        if self._is_between(
            code, self.unicode_section.Hangul_Compatibility_Jamo()
        ):
            return True

        if self._is_between(code, self.unicode_section.Hiragana()):
            return True
        if self._is_between(code, self.unicode_section.Katakana()):
            return True

        if self._is_between(code, self.unicode_section.Greek_and_Coptic()):
            return True
        if self._is_between(code, self.unicode_section.IPA_Extensions()):
            return True
        if self._is_between(code, self.unicode_section.Latin_Extended_A()):
            return True

        return False
