n, m = map(int, raw_input().split(" "))
tracks = []
for i in range(1, n+1):
    fi, name = raw_input().split(" ")
    fi = int(fi)
    tracks.append({"qi": fi * i, "name": name})
# sort list descending on qi
tracks = sorted(tracks, reverse=True, key=lambda x: x["qi"])
for i in range(m):
    print tracks[i]["name"]
