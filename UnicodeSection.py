class UnicodeSection:
    """
    Unicode區段
    https://zh.m.wikipedia.org/wiki/Unicode%E5%8D%80%E6%AE%B5
    """
    @classmethod
    def show_letter_sample(cls, func, limit=30):
        counter = 0
        for o in range(*func()):
            counter += 1
            if counter > limit and limit != -1:
                break
            print(chr(o), end=" ")

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

    def _():
        pass

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

