*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     Collections


*** Variables ***
${Browser}=     Chrome
${SiteUrl}=     http://localhost:5000/api/
${Delay}=     3s 


*** Test Cases ***
Add_Product
    Create Session  api  ${SiteUrl} 
    &{body}=  Create Dictionary  name=potato  code=1234  cost_price=100  sell_price=200  stock=10
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /product  json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response} 

Get_Product
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /product/1234  
    ${response}=   GET On Session  api  /product/1234  expected_status=200                                   

    Status Should Be                 200  ${response}

Update_Product
    Create Session  api  ${SiteUrl}
    &{body}=  Create Dictionary  name=chicken wings  code=1234  cost_price=260   sell_price=2300  stock=2
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  PUT On Session   api   /product/1234   json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response}

Delete_Product
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api  /product/1234  expected_status=200   
      
    
   Status Should Be                 200  ${response}