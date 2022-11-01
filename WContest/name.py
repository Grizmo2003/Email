"""
Library in use:
    unidecode: pip install unidecode
        Using to convert vietnameese name to email type
    csv: pip install csv
        Using to read CSV file
"""

"""
Required:
    file CSV that contain name and class which delimeter by ","
"""
from unidecode import unidecode
from csv import reader


def data(pathname: str) -> tuple[list[str], list[str]]:
    """
    This method is used to Read data from csv file(Name and class)

    Arguments:
        pathname (str): path to file csv

    Returns:
        Type: tuple[list[str], list[str]]
        Value: A list contain name and a list contain class
    """
    file = open("WContest.csv", "r", encoding="utf-8")
    fileCSV = reader(file, delimiter = ",")
    nameData = []
    classData = []
    for row in fileCSV:
        nameData.append(row[0])
        classData.append(row[1])
    file.close()
    return [convertName(name) for name in nameData], classData


def convertName(name: str) -> str:
    """
    This method is used to convert name from normal to non-space and not contain punctuation
    Example: convert from "Hoàng Tuấn Tú" to "hoangtuantu"

    Arguments:
        name (str): Vietnamese name

    Returns:
        Type: str
        Value: email type
    """
    name = name.lower().replace(" ", "")
    return unidecode(name)


def nameToEmail(pathname: str = "WContest.csv") -> None:
    """
    This method is used to getting email of VNU Hanoi University of Science from csv file that 
    contain name and class data. All data will write in file email.txt.

    Arguments:
        pathname (str): path to CSV file <default = WContest.csv>

    Returns:
        Type: NoneType
        Value: None
    """
    nameData, classData = data(pathname)
    file = open("email.txt", "w")
    for i in range(len(nameData)):
        email = nameData[i] + "_t" + classData[i][1:3]+"@hus.edu.vn\n"
        file.write(email)
    print("Done!")


if __name__ == "__main__":
    nameToEmail()
