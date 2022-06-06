<#

.DESCRIPTION
The script configures the 'conf.json' options.

.EXAMPLE
Generate report:
./trigger.ps1 -startOptions

.EXAMPLE
Generate report:
./trigger.ps1.ps1 -restoreOptions

#>

[CmdletBinding()]
param(
    [Parameter(ParameterSetName="StartOptions", Mandatory=$true)][switch] $startOptions,
    [Parameter(ParameterSetName="RestoreOptions", Mandatory=$true)][switch] $restoreOptions,
    [parameter(ParameterSetName="help", Mandatory=$false)][switch]$help, 
    [parameter(ParameterSetName="help", Mandatory=$false)][switch]$h
)

####### Functions #######

$conf = Get-Content '.\env\conf.json' | ConvertFrom-Json

function startTrigger(){
    $path = "$PWD/logs/continuous-update-enabled.txt"
    if($conf.updateOnce -eq $true){
        if(![System.IO.File]::Exists($path)){
            New-Item -Path $path -ItemType File
        }
    }
    else{
        if([System.IO.File]::Exists($path)){
            Remove-Item -Path $path
        }
    }    
}

function restoreTrigger(){
    $json = $conf
    $json.updateOnce = $false       # Defaul value
    $json = $json | ConvertTo-Json
    $json | Out-File ".\env\conf.json"   # -Encoding utf8BOM
}

####### Handling the input #######
if($PSCmdlet.ParameterSetName -eq 'help') {
    Get-Help $MyInvocation.MyCommand.Path -detailed
    exit
} elseif ($StartOptions.IsPresent) {
    startTrigger
    exit
} elseif ($RestoreOptions.IsPresent) {
    restoreTrigger
}