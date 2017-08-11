def printPascal(n):
    n = n-1
    def bazgashti(n):
        Pascal_List = []
        if n == 0:
            Pascal_List.append([1])
            return Pascal_List

        if n == 1:
            Pascal_List.append([1])
            Pascal_List.append([1,1])
            return Pascal_List

        else:
            new_row = [1]
            final_r = bazgashti(n - 1)
            last_row = final_r[-1]
            for k in range(len(last_row)-1):
                new_row.append(last_row[k] + last_row[k + 1])
            new_row.append(1)

            final_r.append(new_row)
            return final_r
    return bazgashti(n)
print(printPascal(8))