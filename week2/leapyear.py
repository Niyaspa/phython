final_year=int(input("enter the final year"))
for year in range(2024,final_year+1):
        if(year%4==0 and year%100!=0)or(year%400==0):
            print(year)
