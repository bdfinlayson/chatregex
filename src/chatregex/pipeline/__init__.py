import re


a_study_in_scarlet = {
    'investigator_pattern': re.compile(r'sherlock holmes|john watson', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r'enoch drebber', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'jefferson hope', flags=re.IGNORECASE),
    'suspects_pattern': re.compile(r'elias openshaw|arthur charpentier|joseph stangerson', flags=re.IGNORECASE)
}

the_secret_adversary = {
    'investigator_pattern': re.compile(r'tommy|tuppence', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r'disappearance of Jane Finn', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'Brown'),
    'suspects_pattern': re.compile(r'Mr Whittington|Rita Vandemeyer|Boris|Julius P Hersheimmer|Sir James Peel Edgerton|Mr Carter', flags=re.IGNORECASE)
}

the_sign_of_four = {
    'investigator_pattern': re.compile(r'sherlock holmes|john watson', flags=re.IGNORECASE),
    'crime_pattern': re.compile(r' poison ', flags=re.IGNORECASE),
    'perpetrator_pattern': re.compile(r'Jonathan Small|Tonga', flags=re.IGNORECASE),
    'suspects_pattern': re.compile(r'Thaddeus Sholto|Bartholomew Sholto', flags=re.IGNORECASE)
}


book_patterns = {
    'a_study_in_scarlet': a_study_in_scarlet,
    'the_secret_adversary': the_secret_adversary,
    'the_sign_of_four': the_sign_of_four
}
