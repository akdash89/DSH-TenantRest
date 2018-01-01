*** Settings ***
Library     KafkaLibrary
Library     String
Suite Setup     Connect To Kafka    172.22.0.1:9092
Suite Teardown      Close       #close kafka producer

*** Variables ***
${Message1}     Kafka is working
${Message2}     ...for real!
${topic}    first_topic
${partition}    1

*** Test Cases ***
Connect to topics
    connect producer    172.22.0.1:9092
    connect consumer    172.22.0.1:9092     group_id=mygroup

Create topic partition
    create topicpartition  ${topic}     partition=${partition}

Send message
    ${bytes1} =	Encode String To Bytes	  ${Message1} 	UTF-8
    ${bytes2} =	Encode String To Bytes	  ${Message2} 	UTF-8
    send    topic=${topic}      value=${bytes1}
    send    topic=${topic}      value=${bytes2}

Get kafka topics
    ${list_topics}=   get kafka topics
    log to console    ${list_topics}

Get messages in topic
    ${nr_messages}=   Get Number Of Messages in Topics    ${topic}
    log to console    ${nr_messages}

*** Keywords ***
