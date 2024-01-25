
      #Know weekday on any date

date=input("Enter any date (in DDMMYYYY formate seperated by space ) :").split();
day=int(date[0]);
month=int(date[1]);
year=int(date[2]);

def leapYear(year):
    if(((year%100==0) and (year%400==0)) or ((year%100!=0) and (year%4==0))):
        return True;
    else:
        return False;


check=leapYear(year);

year=((year%400)-1);

if(year>300):
    year=year-300;
    oddDays=1;
elif(year>200):
    year=year-200;
    oddDays=3;
elif(year>100):
    year=year-100;
    oddDays=5;
else:
    oddDays=0;

year1=year//4;  #Leap years

year2=year-year1;  #Regular years

daysInYears=(year2*365)+(year1*366);

oddDaysInYears=daysInYears%7;

TotalOddDaysInYears=oddDays+oddDaysInYears;

if(month!=1):
    month = month - 1;
else:
    month=0;

month=str(month);

x=28;  # Days in feb of Normal year

if(check==True):
    x=29;    # Days in feb of Leap year

def countDays(month):
    match month:
        case "0":
            return 0;
        case "1":
            return 31;
        case "2":
            return 31 + x;
        case "3":
            return  31 + x + 31;
        case "4":
            return  31 + x + 31 +30;
        case "5":
            return  31 + x + 31 + 30 + 31;
        case "6":
            return  31 + x + 31 + 30 + 31 + 30;
        case "7":
            return  31 + x + 31 + 30 + 31 + 30 + 31;
        case "8":
            return  31 + x + 31 + 30 + 31 + 30 + 31 + 31;
        case "9":
            return  31 + x + 31 + 30 + 31 + 30 + 31 + 31 + 30;
        case "10":
            return  31 + x + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31;
        case "11":
            return  31 + x + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30;

daysInMonths=countDays(month);

totalDays=daysInMonths+day;

oddDaysInRemainingDays=totalDays%7;

totalOddDays=TotalOddDaysInYears+oddDaysInRemainingDays;

totalOddDays=totalOddDays%7;

print(totalOddDays);
def weekDayCalculator(oddDays):
    match oddDays:
        case 0:
            return "Sunday";
        case 1:
            return "Monday";
        case 2:
            return "Tuesday";
        case 3:
            return "Wednesday";
        case 4:
            return "Thusday";
        case 5:
            return "Friday";
        case 6:
            return "Saturday";
        case 7:
            return "Sunday";

weekDay=weekDayCalculator(totalOddDays);

print(f"The Weekday on an entered date is {weekDay}");                                        
