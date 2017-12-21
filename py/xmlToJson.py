import json
import xml.etree.ElementTree as ET
import sys
#import pprint
from datetime import datetime

# input parameters
# arg = os.environ["WIDGET"]
arg = "apiprodstatus"

fXML = sys.argv[1]
#print(fXML[:-3]+'json')
# xml file to root variable
tree = ET.parse(fXML)
root = tree.getroot()

# setting variables from xml
status = root.find("suite/status").get("status");
passed = root.find("statistics/total/stat[last()]").get("pass");
failed = root.find("statistics/total/stat[last()]").get("fail");

# setting other variables
total = sum([int(passed),int(failed)])
message = passed+"/"+str(total)+" passed"

# setting variables for loop through suites
errorList = []
suiteStatus = []

# ==============================================================#
#   Functions
# ==============================================================#

def short_string(input_string, target_length):
    return (input_string[:target_length] + "...") if len(input_string) > target_length else input_string

def get_all_error_info():
    # set root for suite containing suites
    suitesRoot = root.find("suite")

    for suites in suitesRoot.findall("suite"):
        #looping through all tests in all suites

        testRoot = "suite/test"
        # if suites.findall("suite") == []:
        #     testRoot = "test"

        for test in suites.findall(testRoot):
            # execute only current test status is FAIL
            if test.find("status").get("status") == "FAIL":
                # get test name and status
                testName = short_string(test.get("name"), 35)
                error = test.find("status").text
                error = {"testName": testName, "error": short_string(error, 75)}
                errorList.append(error)

def prepare_suite_status_json():
    # loop through statistics for all suites
    for stat in root.findall("statistics/suite/stat"):

        name = stat.get("name")
        passed = int(stat.get("pass"))
        failed = int(stat.get("fail"))
        total = eval("passed+failed")
        message = str(passed)+"/"+str(total)
        # suite passed or failed
        if (failed > 0):
            status = "FAIL"
        else:
            status="PASS"
            
        # build suite status json with parameters
        suiteStats = {
            "suite": name,
            "pass": passed,
            "failed": failed,
            "total": total,
            "status": status,
            "message": message
        }
        suiteStatus.append(suiteStats)

def prepare_test_info():
    global durationTest
    global lastUpdated

    startTime = root.find("suite/status").get("starttime")
    endTime = root.find("suite/status").get("endtime")
    year = endTime[:4]
    month = endTime[4:-15]
    day = endTime[6:-13]
    time = endTime[9:-4]
    time2 = startTime[9:-4]
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(time, FMT) - datetime.strptime(time2, FMT)

    lastUpdated = "Last update: "+day+"-"+month+"-"+year+" "+time2[:-3]
    durationTest = "Duration: "+(str(tdelta.seconds/60)+" minutes, "+str(tdelta.seconds%60)+" seconds")
    #print(lastUpdated, "\n", durationTest)

def build_final_json():
    # final json (ready to be send to dashboard)
    jsonFile = {
        "auth_token": "YOUR_AUTH_TOKEN",
        "errorAmount": int(failed),
        "errors": errorList,
        "message": message,
        "status": status,
        "suiteStatus": suiteStatus,
        "durationTest": durationTest,
        "lastUpdated": lastUpdated
    }
    #json =  mydict(json) 
    with open(fXML[:-3]+'json', 'w') as f:
     json.dump(jsonFile, f)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(json)

def find_between(string, first, last):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except ValueError:
        return ""

# Actual execution of the script
prepare_suite_status_json()
get_all_error_info()
prepare_test_info()
build_final_json()