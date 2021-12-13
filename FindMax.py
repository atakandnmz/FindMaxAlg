def find_max(t,z):
    answer = "" #initialize
    
    len1, len2 = len(t), len(z)
    for i in range(len1): #t de gez
        match = ""
        for j in range(len2): #j de gez
            if (i + j < len1 and t[i + j] == z[j]): #eşleşme oldupunda z den match ekle 
                match += z[j]
            else:
                if (len(match) > len(answer)): 
                    answer = match
                match = ""          #döngü bittiğinde match sıfırla
    b=(z.count(answer)) #largest common substring in sayısı
    return answer,b

if __name__ == '__main__':
    a,b=find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print ("%s is a substring of T, and it occurs %s time Z len(%s)x%s=%s is the solution" %(a,b,len(a),b,len(a)*b))
    