"""loaddata is a module for accessing scraped data about movies from
BoxOfficeMojo and Metacritic.
It's built specifically to work with the data collected for the
CapitalOne Metis Data Science Python Bootcamp Pilot Extravaganza 2K15.
"""

# imports
import os
import json
import pprint

# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')
META_DIR = os.path.join(DATA_DIR, 'metacritic')

# Single function to pull data from both sources.
def get_movies(dir_name):
    ''' get_movies pulls data from all the files in directory dir_name,
        then assembles a list of data called movie_list.

        In: dir_name is a path to the data.

        Out: movie_list is a list of dictionaries with data for each movie.
    '''
    file_contents = os.listdir(dir_name)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(dir_name, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)

        movie_list.append(movie_data)

    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list



# Separate functions are not pythonical. Replaced by the above.
# Kept here only for backwards compatibility.

def get_boxofficemojo_movies():
    file_contents = os.listdir(MOJO_DIR)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(MOJO_DIR, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)

        movie_list.append(movie_data)

    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list


def get_metacritic_movies():
    file_contents = os.listdir(META_DIR)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(META_DIR, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)

        movie_list.append(movie_data)

    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list


if __name__ == "__main__":
    # movies_mojo = get_boxofficemojo_movies()
    # movies_meta = get_metacritic_movies()
    movies_mojo = get_movies(MOJO_DIR)
    movies_meta = get_movies(META_DIR)
