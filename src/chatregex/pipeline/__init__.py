import re


a_study_in_scarlet = {
    'investigator_pattern': re.compile(r'sherlock holmes|sherlock|holmes|mr\. sherlock holmes', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r'drebber', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'jefferson hope', flags=re.IGNORECASE),
    'suspects_pattern': re.compile(r'elias openshaw|arthur charpentier|joseph stangerson', flags=re.IGNORECASE)
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


book_patterns = {
    'a_study_in_scarlet': a_study_in_scarlet,
    'the_secret_adversary': the_secret_adversary,
    'the_sign_of_four': the_sign_of_four
}
