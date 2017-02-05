from sys import argv, stderr
from drawer import *
from kmeans import kmeans


def read_vectors(file_name):
    result = None
    with open(file_name, 'r') as input_file:
        vector_length = int(input_file.readline())
        vectors = list(map(lambda line: tuple(map(int, line.split())), input_file.readlines()))
        if all((len(x) == vector_length for x in vectors)):
            result = vectors
    return result


def write_result(vectors, clusters, file_name):
    with open(file_name, 'w') as output:
        for centroid, cluster_items in clusters.items():
            output.write('centroid {}\n'.format(str(centroid)))
            for vector_index in cluster_items:
                output.write('{}\n'.format(str(vectors[vector_index])))


def main():
    vectors = read_vectors(argv[1])
    clusters_count = int(argv[2])
    output_name = argv[3]
    if vectors:
        print('Calculating...')
        clusters = kmeans(vectors, clusters_count=clusters_count)
        if len(vectors[0]) == 2:
            print('Drawing...')
            display_result(vectors, clusters)
        write_result(vectors, clusters, output_name)
    else:
        print('Invalid input', file=stderr)


if __name__ == '__main__':
    main()


