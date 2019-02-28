# Google Hashcode 2019
# 28/02/2019
# Team: AnGry
# Version: 1.0


def main():

    album = []
    with open("./datasets/a_example.txt") as f:
        n_photos = f.readline()

        for line in f.readlines():
            proc_line = (line.strip().split(" "))

            orientation = proc_line[0]
            n_tags = proc_line[1]
            tags = proc_line[2:]

            album.append([orientation, n_tags, tags])
        print(album)





if __name__ == '__main__':
    main()

