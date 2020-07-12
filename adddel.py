def AddDel(original_list,add_list,delete_list):
    final_list=[]
    for i,add_ele in enumerate(add_list):
        if(add_ele not in original_list):
            original_list.append(add_ele)
    for j,del_ele in enumerate(delete_list):
        if(del_ele in original_list):
            original_list.remove(del_ele)
    original_list=sorted(list(dict.fromkeys(original_list)),reverse=True)   
    print(original_list)
    for k, ele in enumerate(original_list):
        flag=0
        if(k==0):
            final_list.append(ele)
        else:
            for m,final_ele in enumerate(final_list):
                if(len(final_ele)<len(ele)):
                    final_list.insert(m,ele)
                    flag=1
                    break    
            if(flag==0):
                final_list.append(ele)
        print(final_list)
    

o=['one','thirteen', 'one','two', 'three','seven','zero']
a=['one', 'two', 'five', 'six']
d=['two', 'five','three']
AddDel(o,a,d)
