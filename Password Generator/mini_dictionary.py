

def mini_dict(dict):
    """
    This a mini Dictionary, which take one paramiter{ A dictionary }. And user can search from keys...
    """
    print("\nWellcome to Mini-Wiki-Dict.\n")
    for keys, value in dict.items():
        key_list = dict.keys()
        # key_str = str(key_list)
        
        
        while True:
            query = str(input("Search here...\n => "))
           
            if query in key_list:
                result = dict[query]
                print(f"Showing results for {query}\n => {result}")
            else:
                print(f"Sorry {query} is a wrong entry. Please try again")
            
            
if __name__ == '__main__':
    print()
    
        
        



