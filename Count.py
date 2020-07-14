input_str ='With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy ; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation'
                     
validation_array = ["food", "face", "the", "donation", "coalition", "economy", "sector"]

def freq(input_str):
    
    input_str=input_str.lower()
    input_str = input_str.split()          
    str2 = []
    
    for i in validation_array:

       if i not in str2: 
  
           str2.append(i)
             
    for i in range(0, len(str2)):
    
        print('Frequency of', str2[i], 'is :', input_str.count(str2[i]))     
  
freq(input_str)


      
