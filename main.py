# Google Hashcode 2019
# 28/02/2019
# Team: AnGry
# Version: 1.0


def score(p1, p2):
    temp = p1
    temp[-1].intersection(p2[-1])
    l = len(temp[-1])
    diff = min(p1[2], p2[2]) - l

    return min(diff, l)


def find_local_best(S):
    fff = [S[0]]
    l = len(S)
    k=0
    for i in range(l):
        best = None
        #if S[k][2] != 0:
        index = i+1
        best = score(S[k], S[j])
        for j in range(i+1, i+10):
            if j == i and j+1 < l:
                j += 1

            if S[j][2] != 0:

                if S[j][2] >= S[k][2]:
                    temp_score = score(S[k], S[j])
                    if temp_score > best:
                        best = temp_score
                        index = j
                else:
                    break

        # usciti
        if index is not None:
            fff.append(S[index])
            S[index][2] = 0
        k=index

    c = 0
    for x in S:
        if x[2] != 0:
            c +=1

    print(c)
    return fff


def slideshow2txt(S):
    f = open("results/{}".format(FILENAME), 'w')
    f.write("{}\n".format(len(S)))

    for slide in S:
        f.write("{}\n".format(slide[0]))


# COUPLE
def merge_vert(photos):
    V = []
    bound = len(photos)
    for i in range(0, bound, 2):
        if i != bound-1:
            index_1 = photos[i][0]
            index_2 = photos[i+1][0]
            tags    = photos[i][3].union(photos[i+1][3])
            V.append(["{} {}".format(index_1, index_2), "V", len(tags), tags])

    V = sorted(V, key=lambda photo: photo[2], reverse=True)
    return V


# COUPLE2
def slideshow(H, V):
    H.extend(V)
    S = sorted(H, key=lambda photo: photo[2], reverse=True)
    return S



def main():
    ALBUM = []
    with open("./datasets/{}".format(FILENAME)) as f:
        n_photos = f.readline()

        for i, line in enumerate(f.readlines()):
            proc_line = (line.strip().split(" "))

            orientation = proc_line[0]
            n_tags = int(proc_line[1])
            tags = set(proc_line[2:])

            ALBUM.append([str(i), orientation, n_tags, tags])
        # print(ALBUM)

    V_ALBUM = [photo for photo in ALBUM if photo[1] == "V"]
    V_ALBUM = sorted(V_ALBUM, key=lambda photo: photo[2], reverse=True)
    H_ALBUM = [photo for photo in ALBUM if photo[1] == "H"]

    H_SLIDES = sorted(H_ALBUM, key=lambda photo: photo[2], reverse=True)
    V_SLIDES = merge_vert(V_ALBUM)

    S = slideshow(H_SLIDES, V_SLIDES)
    FINAL = find_local_best(S)
    slideshow2txt(FINAL)
    #score(S[0], S[1])


if __name__ == '__main__':

    FILENAME = "b_lovely_landscapes.txt"
    main()

