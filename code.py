import csv
import matplotlib.pyplot as plt

last10years = ["12", "13", "14", "15", "16",
               "17", "18", "19", "20", "21", "22"]


def rawdata(filename):  # collecting the .csv files and converting into data

    with open(filename, "r", errors="ignore") as file:
        csvReader = csv.DictReader(file)
        data = list(csvReader)

    return data


def HistogramOfAuthorizedCap():

    data = rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')

    authCapDict = {"<= 1L": 0, "1L to 10L": 0, "10L to 1Cr": 0,
                   "1Cr to 10Cr": 0, "> 10Cr": 0}

    for authCap in data:

        try:
            cap = int(authCap["AUTHORIZED_CAP"])

            if cap <= 10**5:
                authCapDict["<= 1L"] += 1

            elif cap > 10**5 and cap <= 10**6:
                authCapDict["1L to 10L"] += 1

            elif cap > 10**6 and cap <= 10**7:
                authCapDict["10L to 1Cr"] += 1

            elif cap > 10**7 and cap <= 10**8:
                authCapDict["1Cr to 10Cr"] += 1

            else:
                authCapDict["> 10Cr"] += 1

        except Exception as e:
            print(e)
            authCapDict["> 10Cr"] += 1

    plt.bar(authCapDict.keys(), authCapDict.values())
    plt.gcf().autofmt_xdate()
    plt.show()


def BarPlotOfCompanyRegistrationByYear():
    data = rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')
    yeardict = {}
    for years in data:

        year = years["DATE_OF_REGISTRATION"][-2:]

        if year in yeardict:
            yeardict[year] += 1
        else:
            yeardict[year] = 1

    # print(yeardict)
    plt.bar(yeardict.keys(), yeardict.values())
    plt.gcf().autofmt_xdate()
    plt.show()


def CompanyRegistrationInTheYear2015ByTheDistrict():
    pinPth = "/home/akhil118/Desktop/git/CompanyMaster/maharastra pincodes.csv"
    pincodes = rawdata(pinPth)
    data = rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')

    # print(pincodes)
    pincodesDict = {}
    for pincode in pincodes:

        pincodesDict[pincode["Pin Code"]] = pincode["District"]

    # print(pincodesDict)
    pincodes = list(pincodesDict.keys())
    # print(pincodes)
    districts = list(pincodesDict.values())

    values = [0]*len(districts)

    companiesPerDistrict = dict(zip(districts, values))

    # print(companiesPerDistrict)

    for years in data:

        year = years["DATE_OF_REGISTRATION"][-2:]

        if year == "15":
            pincode = years["Registered_Office_Address"][-6:]
            if pincode in pincodes:
                district = pincodesDict[pincode]
                companiesPerDistrict[district] += 1

    print(companiesPerDistrict)


def GroupedBarPlot():
    data = rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')
    # print(data)
    principleActivity = []
    for eachitem in data:
        name = "PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"
        principleActivity.append(eachitem[name])

    principleActivityList = list(set(principleActivity))

    principleActivityForLast10Years = {}
    for year in last10years:

        principleActivity = {}
        for i in principleActivityList:
            principleActivity[i] = 0

        principleActivityForLast10Years[year] = principleActivity

    for each in data:

        year = each["DATE_OF_REGISTRATION"][-2:]
        if year in last10years:
            activity = each["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]
            capitalAmount = float(each["PAIDUP_CAPITAL"])
            principleActivityForLast10Years[year][activity] += capitalAmount

    # print(principleActivityForLast10Years)

    years = list(principleActivityForLast10Years.keys())
    count = 0

    topActivitiesOf10years = {}
    for eachItem in principleActivityForLast10Years:
        year = years[count]
        value = principleActivityForLast10Years[year]
        topActivitiesOf10years[year] = dict(sorted(value.items(),
                                                   key=lambda x: x[1])[-5:])
        # print(eachItem)
        count = count+1

    print(topActivitiesOf10years)


def main():

    # HistogramOfAuthorizedCap()
    # BarPlotOfCompanyRegistrationByYear()
    # CompanyRegistrationInTheYear2015ByTheDistrict()
    GroupedBarPlot()


main()
