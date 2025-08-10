import math
#1 [*]
p = [
      [1], 
      [2,5], 
      [3,4,7,5], 
      [8,9,6,10,3,2,1,6]
]

S = 13

'''def piramide(p, S):
    sum = p[0][0]; path = []; result = []; n = len(p); i = 0
    if sum == S and i==n-1:
        result.append(path)
        return
        
    
    if sum < S:
        path.append(element)
        return'''
                
        
        
   
    
            
        
        
                    
               
                    
                    
                    
                    
    


#2 [*]
def doces(crianca, valores):
    n = len(crianca)
    m = len(valores)
    crianca.sort(); valores.sort()
    resultado = [0] * n
    j = 0
    for i in range(0,n):
        while(j<m and crianca[i] > valores[j]):
            j+=1
        if j<m:
            resultado[i] = valores[j]
            j +=1
        else:
            break
    return resultado
        
crianca = [5,3,4,5]
valores = [3,2,1,4,7]
print(doces(crianca,valores))

            
            