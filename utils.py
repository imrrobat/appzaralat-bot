import re

START_MESSAGE = """
سلام 👋🏻 
به بات ابزارآلات خوش اومدین. 
اینجا ابزارهای مفیدی وجود داره که میتونید ازشون استفاده کنید که توی منوی پایین میبینید.
برای راهنمایی بیشتر /help رو بزنید. 
"""

HELP_MESSAGE = """
🔩 ابزارهای موجود:

➖➖➖
🎁 محاسبه درصد
/darsad
2000000%5
یعنی 5 درصد از 2 میلیون چقدر میشه؟
➖➖➖
🎁 تبدیل ارقام
/number
123

(ارقام فارسی هم بفرستین انگلیسی میشه)
➖➖➖ 
🎁 رعایت نیم‌فاصله
/nim
text
نکته: text باید فارسی باشه!
➖➖➖
"""

percent_pattern = re.compile(r"^\s*(\d+)\s*%\s*(\d+)\s*$")


def convert_digits(text: str):
    fa_digits = "۰۱۲۳۴۵۶۷۸۹"
    en_digits = "0123456789"

    fa_to_en = str.maketrans(fa_digits, en_digits)
    en_to_fa = str.maketrans(en_digits, fa_digits)

    has_fa = any(ch in fa_digits for ch in text)
    has_en = any(ch in en_digits for ch in text)

    if has_fa and not has_en:
        return text.translate(fa_to_en)

    if has_en and not has_fa:
        return text.translate(en_to_fa)

    return text.translate(fa_to_en).translate(en_to_fa)
