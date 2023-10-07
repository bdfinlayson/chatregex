import re

from src.chatregex.pipeline.preprocessor import Preprocessor

a_study_in_scarlet = {
    'investigator_pattern': re.compile(r'sherlock holmes', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r'', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'', flags=re.IGNORECASE),
    'suspects_pattern': re.compile(r'', flags=re.IGNORECASE)
}

the_secret_adversary = {
    'investigator_pattern': re.compile(r'sherlock holmes', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r'', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'', flags=re.IGNORECASE),
    'suspects_pattern': re.compile(r'', flags=re.IGNORECASE)
}

the_sign_of_four = {
    'investigator_pattern': re.compile(r'sherlock holmes', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r'', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'', flags=re.IGNORECASE),
    'suspects_pattern': re.compile(r'', flags=re.IGNORECASE)
}