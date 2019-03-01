# Google Hashcode 2019
# 01/03/2019 - Extended Round
# Team: AnGry
# Version: 1.1

import math


class Photo:
    def __init__(self, pid, orientation, n_tags, tags):
        self.pid = str(pid)
        self.orientation = str(orientation)
        self.n_tags = int(n_tags)
        self.tags = set(tags)

    def __repr__(self):
        return "ID: {}, N_TAGS: {}, TAGS: {}".format(self.pid, self.n_tags, self.tags)


def score(p1, p2):
    shared = len(p1.tags.intersection(p2.tags))
    min_non_shared = min(p1.n_tags, p2.n_tags) - shared
    return min(shared, min_non_shared)


def merge_vertical(v_photos, mode="max"):
    """
    mergin vertical photos in a simple way
    :param v_photos: list of vertical photos
    :param mode:
    :return: list of slides (each slide is composed of 2 vertical photos)
    """

    V = []
    bound = len(v_photos)

    if mode == "max":
        for i in range(0, bound-1, 2):
            index_1 = v_photos[i].pid
            index_2 = v_photos[i + 1].pid
            tags = v_photos[i].tags.union(v_photos[i + 1].tags)
            V.append(Photo(pid="{} {}".format(index_1, index_2), orientation="V", n_tags=len(tags), tags=tags))

        V.sort(key=lambda x: x.n_tags, reverse=True)

    else:
        if bound % 2 != 0:
            bound = bound - 1

        bound = int(bound/2)
        for i in range(0, bound):
            index_1 = v_photos[i].pid
            index_2 = v_photos[-i - 1].pid
            tags = v_photos[i].tags.union(v_photos[-i - 1].tags)
            V.append(Photo(pid="{} {}".format(index_1, index_2), orientation="V", n_tags=len(tags), tags=tags))

        V.sort(key=lambda x: x.n_tags, reverse=True)

    return V


def sort_slides(slides, k):
    slideshow = [slides[0]]
    del slides[0]

    for j, p1 in enumerate(slideshow):
        best_score = 0
        best_index = None
        c = 0

        for i, p2 in enumerate(slides):
            if c >= k:
                break

            current_score = score(p1, p2)

            if best_score >= math.floor(p2.n_tags/2):
                break

            if current_score > best_score:
                best_score = current_score
                best_index = i

            c += 1

        if best_index is not None:
            slideshow.append(slides[best_index])
            del slides[best_index]
        else:
            # no score > 0 found, adding first element arbitrarily
            if len(slides) == 0:
                break

            slideshow.append(slides[0])
            del slides[0]

    return slideshow


def save_slideshow(slides):
    f = open("results/{}".format(FILENAME), 'w')
    f.write("{}\n".format(len(slides)))

    for slide in slides:
        f.write("{}\n".format(slide.pid))


def main():

    ALBUM = []
    with open("./datasets/{}".format(FILENAME)) as f:

        # skipping first line
        f.readline()
        for i, line in enumerate(f.readlines()):
            proc_line = (line.strip().split(" "))
            photo = Photo(i, proc_line[0], proc_line[1], proc_line[2:])
            ALBUM.append(photo)

    v_photos = [photo for photo in ALBUM if photo.orientation == "V"]
    v_photos.sort(key=lambda x: x.n_tags, reverse=True)
    v_photos = merge_vertical(v_photos, mode="average")

    h_photos = [photo for photo in ALBUM if photo.orientation == "H" and photo.n_tags >= 2]
    h_photos.sort(key=lambda x: x.n_tags, reverse=True)

    # merging horizontal and vertical photos
    slides = v_photos + h_photos
    slides.sort(key=lambda x: x.n_tags, reverse=True)
    # print(slides)

    slideshow = sort_slides(slides, 5000)
    save_slideshow(slideshow)


if __name__ == '__main__':
    filenames = ["a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt", "d_pet_pictures.txt", "e_shiny_selfies.txt"]
    
    for f in filenames:
        FILENAME = f
        main()
