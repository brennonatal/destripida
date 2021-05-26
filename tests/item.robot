*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     Collections


*** Variables ***
${SiteUrl}=     http://localhost:5000/api/
${qnt}=  1
${qnt2}=  2
${prod_id}=  1
${item_id}=  1

*** Test Cases ***
Add_Item
    Create Session   api   ${SiteUrl} 
    ${result} =	Convert To Integer   ${qnt}	
    &{body}=   Create Dictionary   quantity=${result}   product_code=BLM
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   POST On Session    api   /item   json=&{body}   headers=${header}   expected_status=anything
    
    Status Should Be                 200  ${response} 

Get_Item
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /item/${item_id}   expected_status=200                                   

    Status Should Be                 200  ${response}

Update_Item
    Create Session  api  ${SiteUrl}
    ${result} =	Convert To Integer   ${qnt2}
    &{body}=   Create Dictionary    quantity=${result}   product_code=BLM 
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   PUT On Session    api   /item/${item_id}   json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response}

Delete_Item
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api  /item/${item_id}  expected_status=200   
      
    
   Status Should Be                 200  ${response}