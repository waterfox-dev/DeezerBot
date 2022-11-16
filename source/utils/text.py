import json 

class Text :
    
    def __init__(self, url: str) -> None: 
        
        with open(url, 'r', encoding='utf8') as text :
            self.text = dict(json.load(text))
    
    def get(self, key: str, args_array) -> str:
        
        raw_text = str(self.text[key])
        str_ct = raw_text.count('{str')
        int_ct = raw_text.count('{int')
        cmpt = 0
        
        for i in range(str_ct):
            r_text = '{str.'+str(i+1)+'}'
      
            
            if type(args_array[cmpt]) != str : 
                raise TypeError
    
            raw_text = raw_text.replace(r_text, args_array[cmpt])
            cmpt += 1
        
        for i in range(int_ct):
            r_text = '{int.'+str(i+1)+'}'
            print(cmpt)
            if type(args_array[cmpt]) != int :
                raise TypeError
            
            raw_text = raw_text.replace(r_text, str(args_array[cmpt]))
            cmpt += 1
        
        return raw_text        
        