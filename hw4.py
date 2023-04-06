def rep_char(ch, num) :
    print(ch * num)
    

def draw_line_string(msg1, msg2) :
    nstr1= len(msg1)
    nstr2 = len(msg2)
    
    if (len(msg1) > len(msg2) ) :
        rep_char('-', nstr1 +2)
        print(msg1)
        print(msg2)
        rep_char('-', nstr1 +2)
        
    else:
        rep_char('-', nstr2 +2)
        print(msg1)
        print(msg2)
        rep_char('-', nstr2 +2)
    
    
#주 프로그램
name = input('Input his/her name:')
msg1 = f' Hello {name}, '
msg2 = f' Welcome to Seoul. '
draw_line_string(msg1, msg2)

#Jessica Hyunju Ho
#J. H. Ho
