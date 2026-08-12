#To calculate Euclidean distance from all dataset points.
def EuclidianDistance(P1,P2):
    Ans = ((P1["X"]-P2["X"])**2 + (P1["Y"]-P2["Y"])**2)**0.5
    return Ans


def AssignmentKNNClassifier(Data,new_point,K):
    Border = "-"*30

    
    print(Border)
    print("Assignment42 KNN Classifier.")
    print(Border)

   
    dataset = [dict(d) for d in Data]
    for d in dataset:
        d["Distance"] = EuclidianDistance(d,new_point)

   

    sorted_data = sorted(dataset,key=lambda item:item["Distance"])
    print(Border)


    nearest = sorted_data[:K]   #Array slicing---> first 3 from sorted_data
  
    
    #Voting
    
    votes = {}
    
    for neighbors in nearest:
        Label = neighbors["Label"]
        votes[Label] = votes.get(Label,0) + 1
    

    max_votes = max(votes.values())
    tied_classes = [label for label, count in votes.items() if count == max_votes]

    if len(tied_classes) > 1:
        
        pred = "Blue"
    else:
        pred = tied_classes[0]

    return pred

    
def main():

    Data = [
            {"Point":"A", "X":1, "Y":2, "Label":"Red"},
            {"Point":"B", "X":2, "Y":3, "Label":"Red"},
            {"Point":"C", "X":3, "Y":1, "Label":"Blue"},
            {"Point":"D", "X":6, "Y":5, "Label":"Blue"}
    ]
    
        

    X1 = int(input("Enter X coordinate of new point: "))
    Y1 = int(input("Enter Y coordinate of new point: "))
    new_point = {"X":X1,"Y":Y1}
    print("\nPrediction result\n")
    K_values = [1,3,5]

    for K in K_values:
        result = AssignmentKNNClassifier(Data, new_point, K)
        print(f"K = {K} → {result}")


if __name__ == "__main__":
    main()