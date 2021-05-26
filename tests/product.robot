*** Settings ***
Library     JSONLibrary
Library     RequestsLibrary
Library     Collections
 

*** Variables ***
${SiteUrl}=   http://localhost:5000/api/ 
${code}=   BLM

*** Test Cases ***
Add_Product
    Create Session  api  ${SiteUrl}        
    &{body}=  Create Dictionary  name=balmy  code=${code}  cost_price=50  sell_price=100  stock=100
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /product  json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response} 

Add_ExistingProduct 
    Create Session  api  ${SiteUrl} 
    &{body}=  Create Dictionary  name=balmy  code=${code}  cost_price=50  sell_price=10  stock=100
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  POST On Session   api   /product  json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 500  ${response} 


Get_Product
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /product/${code}  expected_status=200                                   

    Status Should Be                 200  ${response}

Get_ProductDontExists
    Create Session  api  ${SiteUrl} 
    ${response}=   GET On Session  api  /product/NTEX  expected_status=400                                  

    Status Should Be                 400  ${response}

Update_Product
    Create Session  api  ${SiteUrl}
    &{body}=  Create Dictionary  name=balmy  code=BLM  cost_price=55   sell_price=110  stock=200
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  PUT On Session   api   /product/${code}   json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 200  ${response}

Update_ProductDontExists
    Create Session  api  ${SiteUrl}
    &{body}=  Create Dictionary  name=balmy  code=BLM  cost_price=55   sell_price=110  stock=200
    ${header}=  Create Dictionary  Content-Type=application/json
    ${response}=  PUT On Session   api   /product/NTEX    json=&{body}   headers=${header}   expected_status=anything

    Status Should Be                 400  ${response}


# Delete_Product Commentado por ser ultilizado em item
#     Create Session  api  ${SiteUrl} 
#     ${response}=   DELETE On Session  api  /product/${code}  expected_status=200   
      
    
#    Status Should Be                 200  ${response}

Delete_ProductDontExists
    Create Session  api  ${SiteUrl} 
    ${response}=   DELETE On Session  api  /product/DNEX  expected_status=400   
      
    
   Status Should Be                 400  ${response} 