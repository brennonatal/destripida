*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     Collections

*** Variables ***
${SiteUrl}=     http://localhost:5000/api/
${cli_id}=   1  

*** Test Cases ***
Add_Client
    Create Session   api   ${SiteUrl}                                                        
    &{body}=  Create Dictionary  first_name=John   last_name=Cena   email=johncena@NULL.com   cpf=100.312.554/09  cellphone=11962007151
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /client  json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response}

Add_ExistingClient  
    Create Session   api   ${SiteUrl} #Adiciona clientes repetidos 
    &{body}=  Create Dictionary  first_name=John   last_name=Cena   email=johncena@NULL.com   cpf=100.312.554/09  cellphone=11962007151
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /client  json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 500  ${response}

Get_Client
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /client/${cli_id}  expected_status=200                                   

    Status Should Be                 200  ${response}

Get_ClientDontExists
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /client/-1  expected_status=404                                   

    Status Should Be                 404  ${response}

Update_Client
    Create Session   api   ${SiteUrl}
    &{body}=  Create Dictionary  first_name=John   last_name=Rambo   email=RAMBOKILL@DEATH.DIE   cpf=989.676.545/21  cellphone=11987783445
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  PUT On Session   api   /client/${cli_id}  json=&{body}   headers=${header}   expected_status=anything


    Status Should Be                 200  ${response}

Update_ClientDontExists
    Create Session   api   ${SiteUrl}
    &{body}=  Create Dictionary  first_name=Will   last_name=Smith   email=we@will.smith   cpf=389.696.335/32  cellphone=11973466745
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  PUT On Session   api   /client/NTEX  json=&{body}   headers=${header}   expected_status=anything


    Status Should Be                 404  ${response}

Delete_Client
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api  /client/${cli_id}  expected_status=200 


Delete_ClientDontExists
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api   /client/NTEX   expected_status=404 


 