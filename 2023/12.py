from re import match

print(
    sum(
        (g:=lambda m, d: 
         not d 
         if not m 
         else (m[0]!='#' and g(m[1:],d))+(d and match(r'[#?]{%d}[.?]'%d[0],m) and g(m[d[0]+1:],d[1:]) or 0))
         (s[0]+'.',(*map(int,s[1].split(',')),)) for s in map(str.split,open('2023/input/12.txt'))
        )
    )