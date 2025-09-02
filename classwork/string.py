# st="dhrUvin virani"
# print(len(st))

# st="dhrUvin virani"  casefold(unique )
# print(str.lower(st))

# st="dhrUvin virani"
# print(str.upper(st))

# st="dhrUVIN vIRANi"
# print(str.capitalize(st))

# st="dhrUvin virani"
# print(str.title(st))

# st=" dhrUvin virani"
# print(str.strip(st))

# st="dhrUvin virani"
# res=st.startswith("dhrUvin") 
# print(res)

# st="dhrUvin virani"
# res=st.endswith("hjbsd")
# print(res)


#print(str.split("dhru vin vi rani"))

# st="dhruvin pankajbhai virani"
# print(st.replace("i","g",1))



# k="hello dhruvin 7640 virani 5792"

# a=0
# b=0
# for i in k:
#     if str(i).isalpha():
#         a+=1
#     elif str(i).isdigit():
#         b+=1
# print("alpha :-",a)
# print("numbers :-",b)

k="hello dhruvin 7640 virani 5792"
s=""
for i in range(len(k)-1,-1,-1):
    s+=k[i]
print(s)


