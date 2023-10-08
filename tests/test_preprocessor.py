from src.chatregex.pipeline.preprocessor import Preprocessor

def test_tokenization(sample_text):
    # given
    preprocessor = Preprocessor()

    # when

    # then


def test_get_protagonist_name(hound_of_the_baskervilles):
    # given
    pre = Preprocessor()

    # when
    result = pre.get_protagonist_name(hound_of_the_baskervilles)

    # then
    assert result == 'Holmes'


def test_get_top_names(hound_of_the_baskervilles):
    # given
    pre = Preprocessor()

    # when
    result = pre.get_top_n_character_names(10, hound_of_the_baskervilles)

    # then
    assert result == ['Holmes',
                      'Henry',
                      'Baskerville',
                      'Watson',
                      'Charles',
                      'Stapleton',
                      'Mortimer',
                      'Barrymore',
                      'Hall',
                      'London']
