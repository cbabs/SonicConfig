import splinter
import os, sys
import time 

#executable_path = {'executable_path':'C:\\code\\phantomjs-2.1.1-windows\\bin\\phantomjs'}

executable_path = {'executable_path':'C:\\code\\chromedriver-2.29\\chromedriver'}

#web1 = splinter.Browser('phantomjs', **executable_path)
web1 = splinter.Browser('chrome', **executable_path)


class sonicwall():
    
    def webConfig(self):
        
        password = 'password'
        newPassword = 'NewPassword'
        
        try:
            url = ""
                       
            ipAddr = '192.168.168.168'

            web1.visit('https://' + ipAddr + '/' + url)
            
            time.sleep(2)
            
            with web1.get_iframe('authFrm') as iframe:
                if iframe.is_text_present('Username:'):
                    print( "Yes, \"Username:\" exists")
                else:
                    print("No, Username: does not exist :(")
          
            
                web1.fill('userName', 'admin') #<input type="text" id="userName" name="userName" value="" maxlength="32" autocomplete="off" style="width: 180px;">
            
            
                web1.fill('pwd', password) #<input type="password" name="pwd" value="" maxlength="63" autocomplete="off" style="width: 180px;">
            
                #time.sleep(1)
                button = web1.find_by_name('Submit')
                
                button.click()
            
            #<a href="javascript:toggleTree('pnl10','usersStatusView.html');" class="nav_font_head1">Users</a>
            
            print "Get System menu in iframe"
            
            
            with web1.get_iframe('outlookFrame') as iframe2:
                # javaScript = '("document.getElementById(\'\').click()");'
                # web1.execute_script(javaScript)

                iframe2.is_element_present_by_xpath("//a[contains(text(), 'System')]", wait_time=10)
            
                #click user menu
                #<a href="javascript:toggleTree('pnl10','usersStatusView.html');" class="nav_font_head1">Users</a>
                print "Click User Menu"
                user_a_link = iframe2.find_by_xpath("//a[contains(@href, 'systemAdministrationView.html')]")[0]
                user_a_link.click()
                time.sleep(5)

                #click setting menu
                #<a href="usersSettingsView.html" onclick="javascript:hiLight(this);" target="tabFrame" class="nav_sub_sett">Settings</a>
                print "Click Setting Sub Menu"
                settings_link = iframe2.find_by_xpath("//div[@id='nav_head2_textbox']/a[contains(@href, 'systemAdministrationView.html')]")[0]
                settings_link.click()        
                time.sleep(5)

            print "Switch iframe into tabFrame"

            #switch iframe into tabFrame
            with web1.get_iframe('tabFrame') as tabFrame:
                
                #change select option
                #select_obj = tabFrame.find_by_xpath("//select[@name='oPass']")[0]
                
                print "Change Select option as Local ..."
                web1.fill('oPass', password)
                
                web1.fill('nPass', newPassword)
                
                web1.fill('confirmPass', newPassword)                
                
                
                
                print "Click Accept button"
                accept_btn = tabFrame.find_by_xpath("//input[@id='applyButt']")[0]
                accept_btn.click()
                time.sleep(5)
            
            
            
            print "Get User menu in iframe"
             
            
            with web1.get_iframe('outlookFrame') as iframe2:
                # javaScript = '("document.getElementById(\'\').click()");'
                # web1.execute_script(javaScript)

                iframe2.is_element_present_by_xpath("//a[contains(text(), 'Users')]", wait_time=10)
            
                #click user menu
                #<a href="javascript:toggleTree('pnl10','usersStatusView.html');" class="nav_font_head1">Users</a>
                print "Click User Menu"
                user_a_link = iframe2.find_by_xpath("//a[contains(@href, 'usersStatusView.html')]")[0]
                user_a_link.click()
                time.sleep(2)

                #click setting menu
                #<a href="usersSettingsView.html" onclick="javascript:hiLight(this);" target="tabFrame" class="nav_sub_sett">Settings</a>
                print "Click Setting Sub Menu"
                settings_link = iframe2.find_by_xpath("//div[@id='nav_head2_textbox']/a[contains(@href, 'usersSettingsView.html')]")[0]
                settings_link.click()        
                time.sleep(2)
            
            print "Switch iframe into tabFrame"

            #switch iframe into tabFrame
            with web1.get_iframe('tabFrame') as tabFrame:
                
                #change select option
                select_obj = tabFrame.find_by_xpath("//select[@name='userRadiusSelect']")[0]
                
                print "Change Select option as Local ..."
                for option in select_obj.find_by_tag('option'):
                    if "Local Users" == option.text:
                        option.click()               
                        time.sleep(5)
                
               
                print("Try to click Configure RADIUS...")
                
                #tabFrame.find_by_id('authMethodCfgBtn').click()
                
                confRad_btn = tabFrame.find_by_xpath("//div[@id='nav_head2_textbox']/input[@id='authMethodCfgBtn']")[0]
                
                confRad_btn.click()
                              
                
            #Below code doesnt work because the it needs to be opened as via menu.//*[@id=""]
            
            '''
            time.sleep(2)
            
            #<a href="usersSettingsView.html" onclick="javascript:hiLight(this);" target="tabFrame" class="nav_sub_sett">Settings</a>
        
            #<input type="button" name="radiusCfgBtn" class="button" value="Configure..." onclick="if (this.disabled) { return; } else { configRadius(); }" title="">
            
            web1.select("userRadiusSelect", "2")
        
            
            button = web1.find_by_name('applyButt')
            
            button.click()
            
            alert = web1.get_alert()
            alert.accept()
            #=======================================================================
            # title = web1.title
            # 
            # htmlSrc = web1.html
            #=======================================================================
            
            time.sleep(8)
            
            url = 'radiusProps.html'
            web1.visit('https://' + ipAddr + '/' + url)
            
            
            web1.fill('Rad_prm_IP', radServerIP)
            
            web1.fill('primarySecret', radServerKey)
            
            time.sleep(1.5)
            
            #click on Radius tab
            web1.find_by_text('RADIUS Users').click()
            
            #<input type="radio" class="label" id="radiusUserGroupMethod3" name="radiusUserGroupMethod" value="2" onclick="onRadUsrGrpMethClick();" title="">
            web1.choose('radiusUserGroupMethod', '2')
            
            web1.find_option_by_text('SonicWALL Administrators').first.click()
            #<a href="#" class="nolineLabel" onclick="selectTab(1)" title="Users">RADIUS Users</a>
            
            #browser.find_option_by_text('SonicWALL Administrators').first.click() 
            
            button = web1.find_by_name('ApplyBtn')
            
            button.click()
            
            
            '''
        except Exception as e:
            print e

        time.sleep(9)
        #web1.quit()
        
   
        
def main():
    sonic = sonicwall()
    sonic.webConfig()
    


if __name__ == "__main__": 
    main()
