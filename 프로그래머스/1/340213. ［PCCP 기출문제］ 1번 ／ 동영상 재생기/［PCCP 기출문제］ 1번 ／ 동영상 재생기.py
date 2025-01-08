def solution(video_len, pos, op_start, op_end, commands):
    
    def nex(dpos):
        if dpos+10 <= d_video_len:
            return dpos+10
        else:
            return d_video_len
        
    def prev(dpos):
        if 0 <= dpos-10:
            return dpos-10
        else:
            return 0
    
    def stod(string):
        h,m = map(int, string.split(":"))
        return h*60 + m
    
    def dtos(digit):
        h = str(digit//60)
        m = str(digit%60)
        if len(h) == 1:
            h = "0" + h
        if len(m) == 1:
            m = "0" + m
        
        return h + ":" + m
        
    d_pos = stod(pos)
    d_video_len = stod(video_len)
    d_op_end = stod(op_end)
    d_op_start = stod(op_start)
    
    for i in commands:
        if d_op_start <= d_pos <= d_op_end:
            d_pos = d_op_end
        if i == "next":
            d_pos = nex(d_pos)
        elif i == "prev":
            d_pos = prev(d_pos) 
        
        
    if d_op_start <= d_pos <= d_op_end:
        d_pos = d_op_end
    
    return dtos(d_pos)
        