def singleMovie():
    mname = input(">>>Enter The Movie Name: ")
    myear = input(">>>Enter the Year of Releaze: ")
    mrating = input(">>>Rate the movie on 5* :")
    return [{'status': 1, 'movieData': [mname, myear, mrating]}]
def addMovie():
    movieData=[]
    movieData.extend(singleMovie())
    flag=True
    while flag:
        userchoice = input(">>>Do you want to add more(y/n):")
        if (userchoice == 'y'):
            movieData.extend(singleMovie())
        elif (userchoice == 'n'):
            flag=False
    return movieData
#main Program
print("---Movie Management System---")
flag=True
movieList=[]
while flag:
    print("--------------------------------------------")
    print("Press 'A' to Add a new Movie:\nPress 'V' to Display All Movies:\nPress 'Q' to Quit the Application:")
    mainMenuOption=input("Enter Your Option: ")
    if(mainMenuOption=='q' or mainMenuOption=='Q'):
        flag=False
        print(">>>Thank You!!!")
    elif(mainMenuOption=='a' or mainMenuOption=='A'):
        movieList.extend([addMovie()])
    elif(mainMenuOption=='v' or mainMenuOption=='V'):
        for movie in movieList[0]:
            print("Name of the Movie: "+movie['movieData'][0],"\nRelease Date:"+movie['movieData'][1],"\nRating:"+movie['movieData'][2])
    else:
        print(">>>Invalid Option!!! Please Try Again!!!")
