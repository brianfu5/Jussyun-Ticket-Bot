
#TODO: Replace these fields with your own configurations
MY_EMAIL = "email@email.com" #email for login
MY_PASSWORD = "password" #password for login
event = "https://ztwen.jussyun.com/pc/content/675b9f3177fe540001200607" #site of ticket page
chromedriver_path = r"C:\Users\brian\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe" #download chromedriver and put the path here
api_url = "https://ztwen.jussyun.com/cyy_gatewayapi/show/pub/v3/show/675b9f3177fe540001200607/sessions_dynamic_data?lang=en" #have to go to network tab in dev tools to find the request api
target_session_id = ["675b9f32b8f2ff00012b5085"] #similar to api_url search through response to find session ids