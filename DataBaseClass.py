"""Crates a database object with all the linguistic and non-linguistic information"""


class DatabaseJSON():
    """Takes the category array and the words array from NlgClass and the
    non-linguistic array from EventClass and returns a dictionary for the database"""
    def __init__(self, categories_array, words_array, non_ling_array):
        self.categories_array = categories_array
        self.words_array = words_array
        self.non_ling_keys = ["file_id", "link", "email"]
        self.database_ling_dict = dict(zip(categories_array, words_array))
        self.database_non_ling_dict = dict(zip(self.non_ling_keys, non_ling_array))
        self.database_dict = dict(self.database_ling_dict, **self.database_non_ling_dict)
