"""Utils."""

import os
import numpy as np
from PIL import Image

def extract_year(title: str):
    """Extract year from Title.

    Args:
        title (str): Title

    Returns:
        int: year
    """
    try:
        year = int(title.strip()[-5:-1])
    except:
        year = -1
    return year

def genres_to_vector(movie_genres, genres_list):
    """Generate vectors from genres.

    Args:
        movie_genres (list): Movie Genres
        genres_list (list): All possible Genres

    Returns:
        array: vector representation of genres
    """
    vector = np.zeros(genres_list, dtype=int)
    if 0 == set(movie_genres).intersection(set(genres_list)):
        return vector
    
    for idx in range(len(movie_genres)):
        if movie_genres[idx] in genres_list:
            vector[idx] = 1
    
    return vector

def load_image(path):
    """Load image.

    Args:
        path (str): Path

    Returns:
        array: image array
    """
    assert os.path.exists(path), "File {} not found".format(path) 
    img = Image.open(path)
    return np.array(img).transpose(1, 0, 2)

def save_images_to_npy(paths):
    """Load and save all images.

    Args:
        paths (list): Filenames
    """
    images = []
    for path in paths:
        images.append(load_image(path))
    np.save('images.npy', np.array(images))
    
def load_npy_image_array(path):
    """Load image array

    Args:
        path (str): Path

    Returns:
        array: Image array
    """
    assert os.path.exists(path), "File {} not found".format(path)
    return np.load(path)