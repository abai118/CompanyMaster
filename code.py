import csv
import matplotlib.pyplot as plt



def rawdata(filename): #collecting the .csv files and converting into data
    
    with open(filename,"r",errors="ignore") as f :
        csvReader=csv.DictReader(f)
        data=list(csvReader)
        
    return data
   
   

def HistogramOfAuthorizedCap() :
    
    
    data=rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')

    authCapDict={"<= 1L":0,"1L to 10L":0,"10L to 1Cr":0,"1Cr to 10Cr":0,"> 10Cr":0}
    
    for authCap in data :
        
        
        
        try :
            cap=int(authCap["AUTHORIZED_CAP"])
            
            if cap <= 10**5 :
                authCapDict["<= 1L"] += 1
                
            elif cap >10**5 and cap<=10**6 :
                authCapDict["1L to 10L"] += 1
                
            elif cap >10**6 and cap<=10**7:
                authCapDict["10L to 1Cr"] += 1
                
            elif cap >10**7 and cap<=10**8 :
                authCapDict["1Cr to 10Cr"] += 1
                
            else :
                authCapDict["> 10Cr"] += 1

        except :
            authCapDict["> 10Cr"] += 1
            
   
    
    
    plt.bar(authCapDict.keys(),authCapDict.values())
    plt.gcf().autofmt_xdate()
    plt.show()
            

def  BarPlotOfCompanyRegistrationByYear() :
    data=rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')
    yeardict={}
    for years in data :
        
        year=years["DATE_OF_REGISTRATION"][-2:]
        
        if year in yeardict :
            yeardict[year] += 1
        else :
            yeardict[year] =1
        
    #print(yeardict)
    plt.bar(yeardict.keys(),yeardict.values())
    plt.gcf().autofmt_xdate()
    plt.show()
       
            
def CompanyRegistrationInTheYear2015ByTheDistrict():
    pincodes=rawdata("/home/akhil118/Desktop/git/CompanyMaster/maharastra pincodes.csv")
    data=rawdata('/home/akhil118/Desktop/git/CompanyMaster/Maharashtra.csv')
    
    #print(pincodes)
    pincodesDict={}
    for pincode in pincodes :
        
        pincodesDict[pincode["Pin Code"]]=pincode["District"]
      
    #print(pincodesDict)   
    pincodes=list(pincodesDict.keys())
    #print(pincodes)
    districts=list(pincodesDict.values())
    
    values=[0]*len(districts)
    
    companiesPerDistrict=dict(zip(districts,values))
    
    #print(companiesPerDistrict)
    
    for years in data :
        
        year=years["DATE_OF_REGISTRATION"][-2:]
    
        if year =="15" :
            pincode=years["Registered_Office_Address"][-6:]
            if pincode in pincodes :
                district=pincodesDict[pincode]
                companiesPerDistrict[district] += 1
            

            
    print(companiesPerDistrict)
    
def GroupedBarPlot():
    pass


def main():

    HistogramOfAuthorizedCap()
    BarPlotOfCompanyRegistrationByYear()
    CompanyRegistrationInTheYear2015ByTheDistrict()
    GroupedBarPlot()
    
main()