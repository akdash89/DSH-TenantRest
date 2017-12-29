*** Settings ***
Library     MQTTLibrary
Suite Setup       Run Keywords   set username and password     fpvryavs   Noq7_zN69dMe
...              AND     Connect     m12.cloudmqtt.com   port=15805
Suite Teardown  Disconnect

*** Variables ***
${topic}        python/test
${Message}     test message

*** Test Cases ***
Publish
    publish     topic=${topic}  message=${Message}

subscribe
    #${Topic_Message}=   subscribe and validate  topic=${topic}   qos=1   timeout=10  payload=${Message}
    ${Topic_Message}=   subscribe  topic=${topic}   qos=1   timeout=15  limit=0
    log to console    ${Topic_Message}
     #should be equal    ${Topic_Message}   ${Message}
