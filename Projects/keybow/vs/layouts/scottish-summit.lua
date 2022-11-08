require "keybow"

function setup() -- Set custom lights up
    keybow.auto_lights(false)
    keybow.clear_lights()

    -- Grey: #404040 / 64,64,64
    -- Pink: #E61873 / 230,24,115
    -- Blue: #29235C / 41,35,92
    
    keybow.set_pixel(0, 230,24,115) -- Pink
    keybow.set_pixel(1, 64,64,64) -- Grey
    keybow.set_pixel(2, 41,35,92) -- Blue

    keybow.set_pixel(3, 230,24,115) -- Pink
    keybow.set_pixel(4, 64,64,64) -- Pink
    keybow.set_pixel(5, 41,35,92) -- Blue

    keybow.set_pixel(6, 230,24,115) -- Pink
    keybow.set_pixel(7, 0,0,0)
    keybow.set_pixel(8, 0,0,0)
    --keybow.set_pixel(7, 64,64,64) -- Grey
    --keybow.set_pixel(8, 41,35,92) -- Blue

    --keybow.set_pixel(9, 230,24,115) -- Pink
    keybow.set_pixel(9, 0,0,0)
    --keybow.set_pixel(10, 64,64,64) -- Grey
    keybow.set_pixel(10, 0,0,0)
    --keybow.set_pixel(11, 41,35,92) -- Blue
    keybow.set_pixel(11, 0,0,0)

end

-- Functions
-- Key mappings --
-- Help: https://learn.pimoroni.com/tutorial/sandyj/using-macros-and-snippets-with-keybow

function handle_key_00(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text([[cd# C:\\Git~tfs$Script£Library"Demos!DemoScripts|Scottish-Summit#Modern-Sample£]])
    end
end

function handle_key_01(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text([[New-AzAutomationModule `
        -AutomationAccountName @ss-demo-automation-modern@ `
        -Name @ImportExcel@ `
        -ContentLink @https://psg-prod-eastus.azureedge.net/packages/importexcel.7.1.1.nupkg@ `
        -ResourceGroupName @ss-demo-rg@]])
    end
end

function handle_key_02(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text([[$pw = (ConvertTo-SecureString -String @demo@ -AsPlainText -Force)]])
    end
end

function handle_key_03(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text("$app = Get-AzADApplication -DisplayName @SSDemo-App-Modern@")
        keybow.sleep(500)
        keybow.text("$appId = $newApp.ApplicationId")
    end
end

function handle_key_04(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text([[Import-AzAutomationRunbook `
        -Name @teamsprivate-channels-report-runbook@ `
        -Path @./teamsprivate-channels-report-runbook.ps1@ `
        -ResourceGroupName @ss-demo-rg@ `
        -AutomationAccountName @ss-demo-automation-modern@ `
        -Type PowerShell]])
    end
end

function handle_key_05(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text([[.\Deploy-AzureAutomation.ps1 -Tenant capadevtest.co.uk -SPTenant capadevtest -CertificatePath @C:\Git\tfs\Script-Library\Demos\DemoScripts\Scottish-Summit\Modern-Sample\SSDemo-App-Modern.pfx@ -AzureAppId $appId -AzureResourceGroupName @ss-demo-rg@ -AzureAutomationName @ss-demo-automation-modern@ -SubscriptionId 2992bdf1-01f8-42bc-b016-c4db6a17cc8a -CertificatePassword $pw]])
    end
end

function handle_key_06(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        keybow.text([[
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fermentum ante ac 
tellus maximus, a tristique ligula sollicitudin. Mauris in molestie purus, a 
dapibus libero. Duis at dolor nulla. Aliquam neque tortor, molestie ut lacus 
sed, cursus gravida enim. Nunc venenatis, metus nec aliquam congue, odio felis 
lobortis lectus, et ullamcorper dolor odio quis sapien. Ut sed pellentesque 
nibh, ac cursus dui. Quisque a porta dui. Nullam eu dui ut lacus convallis 
sagittis. Aenean commodo mauris in nulla placerat semper. Quisque nulla 
sapien, dignissim at semper sit amet, volutpat sit amet dolor. Cras et purus 
pretium nisl laoreet venenatis quis nec nisl. Cras aliquet id nisi vitae porta.
]])
    end
end

function handle_key_07(pressed)
    if pressed then
        --keybow.set_key("", pressed)
    end
end

function handle_key_08(pressed)
    if pressed then
        --keybow.set_key("", pressed)
    end
end

function handle_key_09(pressed)
    if pressed then
        --keybow.set_key("", pressed)
    end
end

function handle_key_10(pressed)
    if pressed then
        --keybow.set_key("", pressed)
    end
end

function handle_key_11(pressed)
    if pressed then
        --keybow.set_key("", pressed)
    end
end
