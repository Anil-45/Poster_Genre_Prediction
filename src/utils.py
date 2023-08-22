"""Utils."""

import os
import numpy as np
import cv2

def file_assert(path):
    """Assert path

    Args:
        path (str): Path
    """
    assert os.path.exists(path), "{} not found".format(path)

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
    vector = np.zeros(len(genres_list), dtype=int)
    
    for idx in range(len(genres_list)):
        if genres_list[idx] in movie_genres:
            vector[idx] = 1
    
    return vector

def load_image(path):
    """Load image.

    Args:
        path (str): Path

    Returns:
        array: image array
    """
    file_assert(path)
    try:
        img = cv2.imread(path)
        img = cv2.resize(img, (150, 200))
        return np.array(img, dtype=np.uint8)
    except:
        print(path)
        return np.zeros(shape=(200, 150, 3), dtype=np.uint8)

def load_images(paths):
    """Load all images in paths.

    Args:
        paths (list): Filenames
    """
    images = np.zeros(shape=(len(paths), 200, 150, 3), dtype=np.uint8)
    for idx, path in enumerate(paths):
        file_assert(path)
        images[idx] = load_image(path)
    return images
