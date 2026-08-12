import math

def EuclidianDistance(X1,Y1,X2,Y2):
    return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)


def ManualKNN(Dataset,new_X,new_Y,k):
    distance =[]


    for point in Dataset:

        name = point["name"]
        X = point["X"]
        Y = point["Y"]
        Label = point["Label"]

        dist = EuclidianDistance(new_X,new_Y,X,Y)
        distance.append({"name": name, "dist": dist, "Label": Label})

    distance.sort(key=lambda item: item["dist"])

    nearest_negibors = distance[:k]

    for neighbor in nearest_negibors:
        name = neighbor["name"]
        dist = neighbor["dist"]
        print(f"{name} - Distance: {dist:.2f}")

    labels = []

    for neghbor in nearest_negibors:
        labels.append(neghbor["Label"])

    red_count = 0
    blue_count = 0

    for color in labels:
        if color == "Red":
            red_count += 1
        if color == "Blue":
            blue_count += 1

    if red_count > blue_count:
        print("Predicted class: Red")
    else:
        print("Predicted class: Blue")
                   

def main():

    Dataset = (
        {"name":"A","X":1 ,"Y":2 ,"Label":"Red"},
        {"name":"B","X":2 ,"Y":3 ,"Label":"Red"},
        {"name":"C","X":3 ,"Y":1 ,"Label":"Blue"},
        {"name":"d","X":6 ,"Y":5 ,"Label":"Blue"}
    )
    k=3

    new_X = int(input("Enter X coordinate: "))
    new_Y = int(input("Enter Y coordinate: "))

    ManualKNN(Dataset,new_X,new_Y,k)

if __name__ == "__main__":
    main()