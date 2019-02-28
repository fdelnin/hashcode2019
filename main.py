# Google Hashcode 2019
# 28/02/2019
# Team: AnGry
# Version: 1.0


# COUPLE
def merge_vert(photos):
    V = []
    bound = len(photos)
    for i in range(0, bound, 2):
        if i != bound-1:
            index_1 = photos[i][0]
            index_2 = photos[i+1][0]
            tags    = photos[i][3].union(photos[i+1][3])
            V.append([(index_1, index_2), "V", len(tags), tags])

    V = sorted(V, key=lambda photo: photo[2], reverse=True)
    return V

# COUPLE
def merge_vert(photos):
    V = []
    bound = len(photos)
    for i in range(0, bound, 2):
        if i != bound-1:
            index_1 = photos[i][0]
            index_2 = photos[i+1][0]
            tags    = photos[i][3].union(photos[i+1][3])
            V.append([(index_1, index_2), "V", len(tags), tags])

    V = sorted(V, key=lambda photo: photo[2], reverse=True)
    return V


def main():

    ALBUM = []
    with open("./datasets/c_memorable_moments.txt") as f:
        n_photos = f.readline()

        for i, line in enumerate(f.readlines()):
            proc_line = (line.strip().split(" "))

            orientation = proc_line[0]
            n_tags = int(proc_line[1])
            tags = set(proc_line[2:])

            ALBUM.append([i, orientation, n_tags, tags])
        # print(ALBUM)

    V_ALBUM = [photo for photo in ALBUM if photo[1] == "V"]
    V_ALBUM = sorted(V_ALBUM, key=lambda photo: photo[2], reverse=True)
    H_ALBUM = [photo for photo in ALBUM if photo[1] == "H"]
    H_ALBUM = sorted(H_ALBUM, key=lambda photo: photo[2], reverse=True)

    V_FINAL = merge_vert(V_ALBUM)
    print(V_FINAL)


if __name__ == '__main__':
    main()

