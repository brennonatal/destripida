*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     Collections
# EXECUTAR ESTE ARQUIVO APOS PRODUCT

*** Variables ***
${SiteUrl}=     http://localhost:5000/api/
${qnt}=  2
${qnt2}=  5
${item_id}=  1
${MTA}=  3000

*** Test Cases ***
Add_Item
    Create Session   api   ${SiteUrl} 
    ${result} =	Convert To Integer   ${qnt}	
    &{body}=   Create Dictionary   quantity=${result}   product_code=BLM
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   POST On Session    api   /item   json=&{body}   headers=${header}   expected_status=anything
    
    Status Should Be                 200  ${response}
Add_MoreThanAvailable
    Create Session   api   ${SiteUrl} 
    ${result} =	Convert To Integer   ${MTA}	
    &{body}=   Create Dictionary   quantity=${result}   product_code=BLM
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   POST On Session    api   /item   json=&{body}   headers=${header}   expected_status=400
    
    Status Should Be                 400  ${response}  

Get_Item
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /item/${item_id}   expected_status=200                                   

    Status Should Be                 200  ${response}
Get_ItemDontExists
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /item/DNEX   expected_status=404                                   

    Status Should Be                 404  ${response}    

Update_Item
    Create Session  api  ${SiteUrl}
    ${result} =	Convert To Integer   ${qnt2}
    &{body}=   Create Dictionary    quantity=${result}   product_code=BLM 
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   PUT On Session    api   /item/${item_id}   json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response}

Update_ItemDontExists
    Create Session  api  ${SiteUrl}
    ${result} =	Convert To Integer   ${qnt2}
    &{body}=   Create Dictionary    quantity=${result}   product_code=DNEX 
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   PUT On Session    api   /item/${item_id}   json=&{body}   headers=${header}   expected_status=400

    Status Should Be                 400  ${response}    

Delete_ItemDontExists
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api  /item/DNEX  expected_status=404   
      
    
   Status Should Be                 404  ${response}      

Delete_Item
    Create Session  api  ${SiteUrl} 
    ${id}=   Convert To Integer   ${item_id}
    ${response}=   DELETE On Session   api   /item/${id}   expected_status=200   


