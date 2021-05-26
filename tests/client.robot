*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     Collections


*** Variables ***
${SiteUrl}=     http://localhost:5000/api/
${cli_id}=  1

*** Test Cases ***
Add_Client
    Create Session   api   ${SiteUrl}
    &{body}=  Create Dictionary  first_name=John   last_name=Cena   email=johncena@NULL.com   cpf=100.312.554/09  cellphone=11962007151
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /client  json=&{body}   headers=${header}   expected_status=anything

Get_Client
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /client/${cli_id}  expected_status=200                                   

    Status Should Be                 200  ${response}

Update_Client
    Create Session   api   ${SiteUrl}
    &{body}=  Create Dictionary  first_name=John   last_name=Rambo   email=RAMBOKILL@DEATH.DIE   cpf=989.676.545/21  cellphone=11987783445
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /client  json=&{body}   headers=${header}   expected_status=anything

Delete_Client
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api  /client/${cli_id}  expected_status=200 
