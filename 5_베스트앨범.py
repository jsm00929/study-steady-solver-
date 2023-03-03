def solution(genres, plays):
    answer = []
    song_list = []
    for idx in range(len(genres)):
        song_list.append([genres[idx], plays[idx], idx])
    song_list.sort(key=lambda x: (x[0], -x[1], x[2]))

    genres_count = []
    genres = song_list[0][0]
    count = 0
    for idx in song_list:
        if genres != idx[0]:
            genres_count.append([genres, count])
            count = idx[1]
            genres = idx[0]
        else:
            count += idx[1]
    genres_count.append([genres, count])
    genres_count.sort(key=lambda x: -x[1])

    for genres in genres_count:
        for idx in range(len(song_list)):
            if song_list[idx][0] == genres[0]:
                answer.append(song_list[idx][2])
                if idx < len(song_list) - 1 and song_list[idx + 1][0] == genres[0]:
                    answer.append(song_list[idx + 1][2])
                    break
    
    return answer