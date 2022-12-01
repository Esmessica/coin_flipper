from art import * 

class Texts:
    """Text representation of app responces
    """
    def title(self):
        _title_text = "Flip a coin"
        _f_title_text = _title_text.center(120)
        _f_title_text = text2art(_f_title_text)
        return _f_title_text

    def head(self):
        _head_text = "HEAD"
        _f_head_text = _head_text.center(130)
        _f_head_text = text2art(_f_head_text)
        return _f_head_text

    def tails(self):
        _tails_text = "TAILS"
        _f_tails_text =  _tails_text.center(130)
        _f_tails_text = text2art( _f_tails_text)
        return _f_tails_text
